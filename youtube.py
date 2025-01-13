import yt_dlp
import os

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")

    # Set up options for downloading
    download_path = os.path.expanduser("~/Documents/ytDownloads")
    os.makedirs(download_path, exist_ok=True)  # Create directory if it doesn't exist

    # Options for yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Set output file template
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio
        'merge_output_format': 'mp4',  # Merge video and audio into mp4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract video information
        info_dict = ydl.extract_info(url, download=True)

        # Print video title and views
        print("Title:", info_dict.get('title', 'N/A'))
        print("Views:", info_dict.get('view_count', 'N/A'))
        print("Download complete.")

except Exception as e:
    print("An error occurred:", str(e))
 