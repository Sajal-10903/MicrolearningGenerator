# generator.py
import os
import shutil

from downloader import download_audio
from transcriber import transcribe_audio
from processor import summarize_text, generate_flashcards


def clean_previous_outputs():
    for folder in ["downloads", "output", "lecture_notes", "flashcards"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder, exist_ok=True)
    print("🧹 Old downloads cleaned.")


def run_pipeline(youtube_url):
    # Step 1: Clean old files
    clean_previous_outputs()

    # Step 2: Download audio
    mp3_path, video_id, _ = download_audio(youtube_url)  # 👈 Fixed: now unpacks 3 values
    print(f"🎧 Downloaded: {mp3_path}")

    # Step 3: Transcribe audio
    print("📝 Transcribing...")
    transcript = transcribe_audio(mp3_path, video_id)

    # Step 4: Summarize
    summary = summarize_text(transcript, video_id)

    # Step 5: Generate flashcards
    generate_flashcards(summary, video_id)