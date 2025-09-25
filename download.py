import yt_dlp
import os
import sys


playlist_url = sys.argv[1]
output_folder = "musicas"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'ignoreerrors': True,
    }

try:
    print(f"Downloading: {playlist_url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
    print("Download done")
except Exception as e:
    print(f"error: {e}")
