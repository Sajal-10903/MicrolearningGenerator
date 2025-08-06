import os
import shutil
from .downloader import download_audio
from .transcriber import transcribe_audio
from .processor import summarize_text, generate_flashcards

def clean_previous_outputs():
    for folder in ["downloads", "lecture_notes", "flashcards"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder, exist_ok=True)
    # Clean cache as per README
    cache_dirs = [
        os.path.expanduser("~/.cache/whisper"),
        os.path.expanduser("~/.cache/huggingface"),
    ]
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
    # Clean __pycache__ directories
    for root, dirs, _ in os.walk("."):
        for dir in dirs:
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))
    print("🧹 Old downloads and caches cleaned.")

def run_pipeline(youtube_url):
    try:
        # Step 1: Clean old files
        clean_previous_outputs()
        
        # Step 2: Download audio
        mp3_path, video_id = download_audio(youtube_url)
        print(f"🎧 Downloaded: {mp3_path}")
        
        # Step 3: Transcribe audio
        transcript = transcribe_audio(mp3_path, video_id)
        
        # Step 4: Summarize
        summary = summarize_text(transcript)
        summary_path = os.path.join("lecture_notes", f"{video_id}_notes.txt")
        with open(summary_path, "w") as f:
            f.write(summary)
        print(f"💾 Saved: {summary_path}")
        
        # Step 5: Generate flashcards
        generate_flashcards(transcript, video_id)
    except Exception as e:
        raise RuntimeError(f"❌ Pipeline failed: {e}")