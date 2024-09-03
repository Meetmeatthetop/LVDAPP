from PySide6.QtCore import Qt, QRect, QPoint, Signal, QThread, QObject
import subprocess
import yt_dlp
import re
import os
import time

class DownloadThread(QThread):
    status = Signal(str)
    progress = Signal(int)

    def __init__(self, url, format_id, filepath):
        super().__init__()
        self.url = url
        self.format_id = format_id
        self.filepath = filepath
        self._is_stopped = False

        self.ydl_opts = {
            'format': format_id,
            'outtmpl': self.filepath,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'progress_hooks': [self.progress_hook]
        }
        self.ytdl = yt_dlp.YoutubeDL(self.ydl_opts)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent_str = d.get('_percent_str', '0%')
            
            # Remove ANSI escape codes
            percent_str = re.sub(r'\x1b\[[0-9;]*m', '', percent_str).strip()

            # Remove '%' sign and convert to integer
            if percent_str.endswith('%'):
                percent_str = percent_str[:-1].strip()
        
            # Convert to integer if valid
            if percent_str.replace('.', '').isdigit():  # Ensure it's numeric
                percent_int = int(float(percent_str))
            else:
                percent_int = 0  # Handle the case where the string is not a number

            # Prepare the emitted output
            total_bytes_str = d.get('_total_bytes_str', '0')
            speed_str = d.get('_speed_str', '0')
            eta_str = d.get('eta', '00:00')  # Get ETA if available

            # Emit the status string
            ##self.status.emit(percent_str)
            self.progress.emit(percent_int)

                

    def run(self):
        try:
            # Extract video info without downloading to get title and other metadata
            video_info = self.ytdl.extract_info(self.url, download=False)
            video_title = video_info.get('title', 'video')
            video_filename = f"{video_title}.mp4"
            audio_filename = f"{video_title}.m4a"

            # Update the format for downloading
            self.ydl_opts['format'] = f"{self.format_id}+bestaudio"  # Use the user-selected video format and best audio
            self.ytdl = yt_dlp.YoutubeDL(self.ydl_opts)  # Reinitialize with updated options

            # Download the video and audio
            self.ytdl.download([self.url])

            # Merge video and audio using FFmpeg
            subprocess.run(['ffmpeg', '-i', video_filename, '-i', audio_filename, '-c', 'copy', f"{video_title}_merged.mp4"], check=True)

            # Emit success message
            self.status.emit('Download complete!')
        except yt_dlp.DownloadError as e:
            # Emit error message for yt-dlp download issues
            self.status.emit(f'Error: {str(e)}')
        except subprocess.CalledProcessError as e:
            # Emit error message for FFmpeg issues
            self.status.emit(f'FFmpeg error: {str(e)}')


class stop_Download():
    def stop(self):
        self._is_stopped = True
        self.ytdl.abort_download()

