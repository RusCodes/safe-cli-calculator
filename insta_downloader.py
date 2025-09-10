import os
import yt_dlp

def download_instagram_video(url, output_path=None):
    """Downloads an Instagram video using yt-dlp and saves it to the specified directory."""

    # Default to the Downloads folder if no output path is provided
    if output_path is None:
        output_path = os.path.join(os.path.expanduser("~"), "Downloads")  # Resolves to ~/Downloads

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Download complete! Saved to: {output_path}")
    except yt_dlp.DownloadError as e:
        print(f"❌ Download failed: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Example usage
video_url = input("🎥 Enter Instagram video URL: ").strip()
download_instagram_video(video_url)

