from pathlib import Path
from tqdm import tqdm
import whisper


def main():
    # Folders for input media files and output transcripts
    input_dir = Path("input")
    output_dir = Path("output")

    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    # Supported video and audio formats
    media_extensions = (
        ".mp4", ".mkv", ".avi", ".mov", ".flv",
        ".mp3", ".wav", ".m4a"
    )

    # Whisper model size:
    # tiny, base, small, medium, large
    # medium gives a good balance
    model_size = "medium"

    media_files = [
        file for file in input_dir.iterdir()
        if file.is_file() and file.suffix.lower() in media_extensions
    ]

    if not media_files:
        print("No media files found in the input folder.")
        print("Put your video or audio files into the 'input' folder and run the script again.")
        return

    print(f"Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)

    print(f"Found {len(media_files)} file(s). Starting transcription...")

    for media_file in tqdm(media_files, desc="Processing files"):
        output_file = output_dir / f"{media_file.stem}_transcript.txt"

        try:
            result = model.transcribe(
                str(media_file),
                language="en",  # use "uk" for Ukrainian, "en" for English
                verbose=False
            )

            with open(output_file, "w", encoding="utf-8") as file:
                file.write(result["text"].strip())

            tqdm.write(f"Saved: {output_file.name}")

        except Exception as error:
            tqdm.write(f"Error processing {media_file.name}: {error}")

    print("\nAll files processed.")


if __name__ == "__main__":
    main()
