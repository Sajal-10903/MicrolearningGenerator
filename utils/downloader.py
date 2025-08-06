import os
import uuid
import glob
from yt_dlp import YoutubeDL

def download_audio(youtube_url):
    video_id = str(uuid.uuid4())
    os.makedirs("downloads", exist_ok=True)
    output_path = f"downloads/{video_id}.%(ext)s"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        mp3_files = glob.glob(f"downloads/{video_id}*.mp3")
        if not mp3_files:
            raise FileNotFoundError("❌ Audio download failed or not converted to mp3.")
        return mp3_files[0], video_id
    except Exception as e:
        raise FileNotFoundError(f"❌ Failed to download audio: {e}")