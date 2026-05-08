# video_transcriber

A simple Python tool for batch transcription of video and audio files using OpenAI Whisper.

The script scans the `input` folder, transcribes supported media files, and saves clean text transcripts into the `output` folder.

## Features

- Batch transcription of multiple media files
- Supports both video and audio formats
- Saves transcripts as `.txt` files
- Uses OpenAI Whisper for speech recognition
- Supports Ukrainian, English, and other Whisper-supported languages
- Shows progress while processing files
- Keeps input and output files separated for a cleaner workflow

## Supported file formats

The script currently supports:

```text
.mp4
.mkv
.avi
.mov
.flv
.mp3
.wav
.m4a
```

## Project structure

```text
video_transcriber/
│
├── input/
│   └── .gitkeep
│
├── output/
│   └── .gitkeep
│
├── transcribe.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.9+
- FFmpeg
- OpenAI Whisper
- tqdm

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/video_transcriber.git
cd video_transcriber
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## FFmpeg installation

Whisper requires FFmpeg to process video and audio files.

### Windows

Download FFmpeg from the official website and add it to your system PATH.

### macOS

```bash
brew install ffmpeg
```

### Ubuntu/Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

1. Put your video or audio files into the `input` folder.

Example:

```text
input/interview.mp4
input/lecture.m4a
```

2. Run the script:

```bash
python transcribe.py
```

3. Transcripts will be saved into the `output` folder.

Example result:

```text
output/interview_transcript.txt
output/lecture_transcript.txt
```

## Language settings

By default, the script can be configured for a specific language.

For Ukrainian:

```python
language = "uk"
```

For English:

```python
language = "en"
```

For automatic language detection, remove the `language` parameter from the Whisper transcription call.

## Whisper model

The script uses a Whisper model defined in `transcribe.py`.

Example:

```python
model_size = "medium"
```

Available model options include:

```text
tiny
base
small
medium
large
```

Smaller models are faster but may be less accurate. Larger models are more accurate but require more time and system resources.

## Example output

Input file:

```text
input/sample_video.mp4
```

Output file:

```text
output/sample_video_transcript.txt
```

Example transcript:

```text
This is an example of a generated transcript. The script converts spoken content from a media file into plain text.
```

## Notes

- Media files are not included in this repository.
- The `input` and `output` folders are kept with `.gitkeep` files.
- Actual video, audio, and transcript files are ignored by `.gitignore`.
- The first run may take longer because Whisper needs to download the selected model.

## Use cases

This tool can be used for:

- Transcribing lectures
- Creating notes from video recordings
- Processing interviews
- Converting speech into text
- Preparing text data from audio/video sources

## License

This project is licensed under the MIT License.
