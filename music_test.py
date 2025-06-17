import streamlit as st
import openai
from transformers import MusicgenForConditionalGeneration, AutoProcessor
import torchaudio
from pydub import AudioSegment
from gtts import gTTS
import os
import tempfile

# Set OpenAI API key
openai.api_key = "Xyz"

# Load MusicGen model
@st.cache_resource
def load_musicgen():
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    return model, processor

model, processor = load_musicgen()

# Streamlit UI
st.title("Hindi MP3 Song Generator")
st.markdown("Enter your mood, tempo, genre and instruments to create a Hindi song with melody!")

# User inputs
genre = st.text_input("Genre", "carnatic")
tempo = st.selectbox("Tempo", ["slow", "medium", "fast"])
mood = st.text_input("Mood", "devotional")
instruments = st.text_input("Instruments", "Harmonium,tabla")

# Button to generate
if st.button("Generate MP3 Song"):
    with st.spinner("Generating lyrics and music..."):

        # STEP 1: Generate Hindi lyrics using GPT
        prompt = f"""
        generate {genre} a song whose {tempo} this, mood is this {mood} and instruments played are {instruments} 
        Please keep the language of song as Hindi and also make this song more emotional
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "you are a experienced and well trained Hindi  singer।"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=200
            )
            lyrics = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            st.error(f"OpenAI error: {e}")
            st.stop()

        st.subheader("Generated Hindi Lyrics")
        st.write(lyrics)

        # STEP 2: Convert lyrics to audio using Google TTS
        try:
            tts = gTTS(lyrics, lang='hi')
            tts_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(tts_audio.name)
        except Exception as e:
            st.error(f"TTS Error: {e}")
            st.stop()

        # STEP 3: Generate melody using MusicGen
        try:
            description = f"{genre} music with {instruments} in {mood} mood, {tempo} tempo"
            inputs = processor(text=[description], return_tensors="pt")
            audio_values = model.generate(**inputs, max_new_tokens=1024)
            melody_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
            torchaudio.save(melody_path, audio_values[0], 32000)
        except Exception as e:
            st.error(f"MusicGen Error: {e}")
            st.stop()

        # STEP 4: Mix voice + melody using pydub
        try:
            voice = AudioSegment.from_file(tts_audio.name, format="mp3")
            melody = AudioSegment.from_file(melody_path, format="wav")

            combined = melody - 10  # lower music volume
            final_mix = combined.overlay(voice)

            final_path = os.path.join(tempfile.gettempdir(), "final_song.mp3")
            final_mix.export(final_path, format="mp3")
        except Exception as e:
            st.error(f"Mixing error: {e}")
            st.stop()

        st.success("Your Hindi song is ready!")
        st.audio(final_path, format="audio/mp3")
        st.download_button("Download MP3", data=open(final_path, "rb"), file_name="generated_song.mp3")
