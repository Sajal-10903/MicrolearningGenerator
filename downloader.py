# downloader.py
import os
import uuid
import yt_dlp

def download_audio(youtube_url):
    video_id = str(uuid.uuid4())
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{video_id}.mp3")

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

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        title = info.get('title', '')

    return output_path, video_id, title  # 👈 This is why we need to unpack 3 values