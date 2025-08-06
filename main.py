from utils.generator import run_pipeline
from urllib.parse import urlparse, parse_qs

def main():
    print("🎯 Microlearning Generator from YouTube\n")
    youtube_url = input("🔗 Enter YouTube video URL: ").strip()
    if not youtube_url:
        print("❌ No URL entered. Exiting.")
        return
    try:
        # Validate YouTube URL
        parsed_url = urlparse(youtube_url)
        if not parsed_url.netloc in ["www.youtube.com", "youtu.be"]:
            raise ValueError("Invalid YouTube URL.")
        run_pipeline(youtube_url)
        print("✅ Microlearning content generated successfully!")
    except ValueError as ve:
        print(f"❌ Invalid input: {ve}")
    except FileNotFoundError as fnf:
        print(f"❌ File error: {fnf}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()