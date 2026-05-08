# video_transcriber

A Python tool for batch transcription of video and audio files using OpenAI Whisper.

The script scans the `input` folder, transcribes supported media files, and saves clean `.txt` transcripts into the `output` folder.

By default, the project is configured for English transcription. The language can be changed manually to Ukrainian or other Whisper-supported languages. Automatic language detection can also be enabled if needed.

## Features

- Batch transcription of multiple media files
- Supports both video and audio formats
- Saves transcripts as `.txt` files
- Uses OpenAI Whisper for speech recognition
- Default language is set to English
- Ukrainian transcription can be enabled manually
- Automatic language detection can be enabled by removing the language parameter
- Shows file-level progress with `tqdm`
- Keeps input and output files separated
- Suitable for lectures, tutorials, interviews, notes, and text data preparation

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

You can clone this repository either with Git or GitHub Desktop.

### Option 1: Clone with Git

```bash
git clone https://github.com/tponomarenko/video_transcriber.git
cd video_transcriber
```

### Option 2: Clone with GitHub Desktop

1. Open GitHub Desktop.
2. Go to `File` → `Clone repository`.
3. Select `video_transcriber`.
4. Choose a local folder.
5. Click `Clone`.

After cloning the repository, open the project folder in your terminal or code editor.

## Create a virtual environment

### macOS / Linux / WSL / Ubuntu

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, you should see `(.venv)` at the beginning of your terminal line.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
python -m venv .venv
.venv\Scripts\activate
```

## Install Python dependencies

After activating the virtual environment, install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
openai-whisper
tqdm
```

## FFmpeg installation

Whisper requires FFmpeg to process video and audio files.

### Windows

Download FFmpeg and add it to your system PATH.

To check if FFmpeg is available, run:

```bash
ffmpeg -version
```

### macOS

```bash
brew install ffmpeg
```

### Ubuntu / WSL / Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

To verify installation:

```bash
ffmpeg -version
```

## Usage

1. Put your video or audio files into the `input` folder.

Example:

```text
input/interview.mp4
input/lecture.m4a
```

2. Run the script from the project root:

```bash
python transcribe.py
```

On some Linux, Ubuntu, or WSL systems, use:

```bash
python3 transcribe.py
```

3. Transcripts will be saved into the `output` folder.

Example result:

```text
output/interview_transcript.txt
output/lecture_transcript.txt
```

## Language settings

By default, the script is configured for English transcription:

```python
language = "en"
```

For Ukrainian transcription, change the language value in `transcribe.py` to:

```python
language = "uk"
```

Whisper uses ISO language codes, so other supported languages can also be configured manually.

Recommended setup:

| Use case | Setting |
|---|---|
| English audio/video | `language = "en"` |
| Ukrainian audio/video | `language = "uk"` |
| Mixed or unknown language | remove the `language` argument |

### Automatic language detection

Automatic language detection is not enabled by default. This keeps the transcription behavior predictable and avoids unwanted language detection issues.

To enable automatic language detection, remove the `language` argument from the transcription call.

Change this:

```python
result = model.transcribe(
    str(media_file),
    language=language,
    verbose=False
)
```

to this:

```python
result = model.transcribe(
    str(media_file),
    verbose=False
)
```

## Whisper model settings

The script uses a Whisper model defined in `transcribe.py`.

Example:

```python
model_size = "medium"
```

Available model options:

```text
tiny
base
small
medium
large
```

Recommended options:

| Model | Best for |
|---|---|
| `tiny` | Very quick testing |
| `base` | Fast local testing |
| `small` | Better quality with reasonable speed |
| `medium` | Good balance between speed and quality |
| `large` | Higher accuracy, slower processing |

Smaller models are faster but may be less accurate. Larger models are more accurate but require more time and system resources.

For the first local test, it is recommended to use:

```python
model_size = "base"
```

After confirming that everything works, you can switch back to:

```python
model_size = "medium"
```

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

## Local test example

A successful run should look similar to this:

```text
Loading Whisper model: medium
Found 1 file(s). Starting transcription...
Saved: sample_video_transcript.txt
Processing files: 100%|██████████| 1/1
All files processed.
```

The first run may take longer because Whisper needs to download the selected model.

## Troubleshooting

### `python: command not found`

On some Linux, Ubuntu, or WSL systems, the `python` command may not be available.

Use:

```bash
python3 --version
python3 transcribe.py
```

instead of:

```bash
python --version
python transcribe.py
```

Optional fix:

```bash
sudo apt install python-is-python3
```

### `The virtual environment was not created successfully because ensurepip is not available`

This can happen on Debian, Ubuntu, or WSL if the virtual environment package is missing.

Install it with:

```bash
sudo apt update
sudo apt install python3.10-venv
```

If your Python version is different, use:

```bash
sudo apt install python3-venv
```

Then remove the incomplete virtual environment and create it again:

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

### `.venvScriptsactivate: command not found`

This usually happens when a Windows activation command is used inside Linux, Ubuntu, or WSL.

For Linux, Ubuntu, WSL, and macOS, use:

```bash
source .venv/bin/activate
```

For Windows PowerShell, use:

```powershell
.venv\Scripts\Activate.ps1
```

For Windows CMD, use:

```cmd
.venv\Scripts\activate
```

### `ffmpeg: command not found`

Install FFmpeg:

```bash
sudo apt update
sudo apt install ffmpeg
```

Then verify it:

```bash
ffmpeg -version
```

### `No media files found in the input folder`

Make sure your media files are placed inside the `input` folder:

```text
input/your_file.mp4
```

Also make sure the file extension is supported.

### The installation takes a long time

This is normal. Whisper depends on packages such as PyTorch, which can be large.

The first installation may take several minutes depending on your internet speed and system.

### The first transcription takes a long time

The first run may be slower because Whisper downloads the selected model.

Processing time also depends on:

- media file length
- selected Whisper model
- CPU or GPU availability
- system resources
- audio quality

### Git pull error: local changes would be overwritten

If Git shows an error like this:

```text
Your local changes to the following files would be overwritten by merge
```

You can temporarily save local changes, pull updates, and then restore your work:

```bash
git stash
git pull
git stash pop
```

If you do not need your local changes, you can discard them:

```bash
git restore README.md
git pull
```

## Notes

- Media files are not included in this repository.
- The `input` and `output` folders are kept with `.gitkeep` files.
- Actual video, audio, and transcript files are ignored by `.gitignore`.
- YouTube subtitles are not required.
- The script transcribes the audio track from the media file.
- Transcript quality depends on audio clarity.
- Long files may take significant time to process.

## Use cases

This tool can be used for:

- Transcribing lectures and tutorials
- Creating notes from video recordings
- Processing interviews
- Converting speech into text
- Preparing text data from audio/video sources
- Building searchable text notes from recorded content
- Creating draft transcripts for further editing

## Limitations

- Transcript quality depends on audio clarity.
- Background noise, overlapping speakers, and low-quality recordings may reduce accuracy.
- Long files may take significant time to process.
- The script currently saves plain text only.
- Speaker separation is not included.
- Subtitle formats such as `.srt` or `.vtt` are not generated yet.
- The script does not extract existing YouTube subtitles; it transcribes the audio track.

## Possible future improvements

- Add command-line arguments for language and model size
- Add optional automatic language detection
- Add `.srt` subtitle export
- Add timestamps
- Add speaker diarization
- Add logging to a separate file
- Add option to skip existing transcript files
- Add support for custom output filenames

## License

This project is licensed under the MIT License.
