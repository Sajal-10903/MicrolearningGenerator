import whisper
import os

def transcribe_audio(mp3_path, video_id):
    print("📝 Transcribing...")
    try:
        model = whisper.load_model("base")
        result = model.transcribe(mp3_path)
        text = result["text"]
        output_dir = "lecture_notes"
        os.makedirs(output_dir, exist_ok=True)
        transcript_path = os.path.join(output_dir, f"{video_id}_transcript.txt")
        with open(transcript_path, "w") as f:
            f.write(text)
        print(f"💾 Saved: {transcript_path}")
        return text
    except Exception as e:
        raise RuntimeError(f"❌ Transcription failed: {e}")