# music_lyrics_generator
Generate music and lyrics with facebook musicgen &amp; GPT models
# MP3 Song Generator

A Streamlit-based web application that generates complete Hindi songs with lyrics and melodies based on user-specified parameters like mood, tempo, genre, and instruments.

## Features

- **AI-Generated Hindi Lyrics**: Uses OpenAI's GPT-4 to create emotional Hindi lyrics
- **Text-to-Speech**: Converts generated lyrics to audio using Google Text-to-Speech (gTTS)
- **AI Music Generation**: Creates instrumental melodies using Facebook's MusicGen model
- **Audio Mixing**: Combines vocals and instrumental tracks into a complete song
- **Interactive Web Interface**: Easy-to-use Streamlit interface
- **Download Capability**: Download generated songs as MP3 files

## Requirements

### Python Dependencies

```bash
streamlit
openai
transformers
torch
torchaudio
pydub
gtts
```

### System Dependencies

- FFmpeg (required for audio processing)
- Internet connection (for OpenAI API and gTTS)

## Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd hindi-song-generator
```

2. **Install Python dependencies**:
```bash
pip install streamlit openai transformers torch torchaudio pydub gtts
```

3. **Install FFmpeg**:
   - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html)
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg`

4. **Set up OpenAI API Key**:
   - Get your API key from [OpenAI Platform](https://platform.openai.com/)
   - Replace `"Xyz"` in the code with your actual API key
   - **Security Note**: Consider using environment variables instead of hardcoding the API key

## Usage

 **Run the application**:
```bash
streamlit run app.py
```

- Temporary files are automatically cleaned up
- Consider using `musicgen-medium` or `musicgen-large` for better quality (requires more resources)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please ensure compliance with the licenses of all dependencies:
- OpenAI API terms of service
- Meta's MusicGen model license
- Google TTS usage policies

## Disclaimer

- Ensure proper licensing for commercial use
- Respect copyright laws when using generated content
- API usage may incur costs (OpenAI)
- Generated content quality may vary

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review dependency documentation
3. Open an issue in the repository

---

**Note**: Remember to replace the placeholder API key with your actual OpenAI API key before running the application.
