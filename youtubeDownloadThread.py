from PySide6.QtCore import Qt, QRect, QPoint, Signal, QThread, QObject
import subprocess
import yt_dlp
import re
import os
import time

class DownloadThread(QThread):
    status = Signal(str)  # Signal to update status messages
    progress = Signal(int)  # Signal to update progress
    formats_loaded = Signal(list)  # Signal to send available formats to the UI

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
            video_duration = video_info.get('duration', 0)
            formats = video_info.get('formats', [])
            print(f"Video Title: {video_title}")
            print(f"Video Duration: {video_duration} seconds")
            print(f"Available Formats: {formats}")

            # Emit available formats to the UI
            self.formats_loaded.emit(formats)

            # Validate format_id
            if not any(fmt['format_id'] == self.format_id for fmt in formats):
                self.status.emit(f"Error: Invalid format ID '{self.format_id}'")
                return

            # Update the format for downloading
            self.ydl_opts['format'] = f"{self.format_id}+bestaudio"
            self.ytdl = yt_dlp.YoutubeDL(self.ydl_opts)

            # Download the video
            self.ytdl.download([self.url])

            # Merge video and audio using FFmpeg
            video_filename = f"{video_title}.mp4"
            audio_filename = f"{video_title}.m4a"
            merged_filename = f"{video_title}_merged.mp4"

            if os.path.exists(merged_filename):
                os.remove(merged_filename)  # Remove existing merged file to avoid conflicts

            ffmpeg_command = [
                'ffmpeg', '-y', '-i', video_filename, '-i', audio_filename,
                '-c', 'copy', merged_filename
            ]
            try:
                subprocess.run(ffmpeg_command, check=True)
                self.status.emit('Download complete!')
            except FileNotFoundError:
                self.status.emit('Error: FFmpeg not found. Please install FFmpeg and add it to your PATH.')
            except subprocess.CalledProcessError as e:
                self.status.emit(f'FFmpeg error: {str(e)}')

        except yt_dlp.DownloadError as e:
            self.status.emit(f'Error: {str(e)}')
        except Exception as e:
            self.status.emit(f'Unexpected error: {str(e)}')

    def stop(self):
        self._is_stopped = True
        self.ytdl.abort_download()

