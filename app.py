from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QFileDialog
from ui_lvdApp import Ui_MainWindow
from PySide6.QtCore import Qt, QRect, QPoint, Signal, QThread
from PySide6.QtGui import QCloseEvent, QPixmap
from youtubeDownloadThread import DownloadThread
import yt_dlp
import os


class MyDownloadApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Ensure setupUi is defined in Ui_MainWindow
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Line Video Downloader")

        self.is_maximized = False
        self.start = QPoint(0, 0)  # To store the starting point of the drag
        self.resize_margin = 10  # Margin for resizing

        
        
## This section hold all the hidden element
        self.icon_Widget.setHidden(True)

        self.youtubeThumbnail_Widget.setHidden(True)
        self.facebookThumbnail_Widget.setHidden(True)
        self.instagramThumbnail_Widget.setHidden(True)
        self.tiktokThumbnail_Widget.setHidden(True)
        self.facebook_download_page_button.setHidden(True)
        self.instagram_download_page_button.setHidden(True)
        self.tk.setHidden(True)

        self.youtube_ProgressBar.setHidden(True)
        self.facebookProgressBar.setHidden(True)
        self.instagramProgressBar.setHidden(True)
        self.tiktok_ProgressBar.setHidden(True)

        ##self.max_Button.setHidden(True)
        ##self.minimize_Button.setHidden(True)

## This section hold all the connected element
        self.max_Button.clicked.connect(self.toggle_maximize)

        ## Main page connections
        self.home_Button.clicked.connect(self.switch_to_home)
        self.home_Button_2.clicked.connect(self.switch_to_home)

        self.my_file_Button.clicked.connect(self.switch_to_myFile)
        self.my_file_Button_2.clicked.connect(self.switch_to_myFile)

        self.tolls_Button.clicked.connect(self.switch_to_tool)
        self.tools_Button_2.clicked.connect(self.switch_to_tool)

        ## Download page connection
        self.youtube_download_page_button.clicked.connect(self.switch_to_youtubePage)
        self.facebook_download_page_button.clicked.connect(self.switch_to_facebookPage)
        self.instagram_download_page_button.clicked.connect(self.switch_to_instagramPage)
        self.tk.clicked.connect(self.switch_to_tiktokPage)

        # Button Connection
        self.youtubeFetchVideo_Button.clicked.connect(self.fetch_formats)
        self.youtubeDownload_Button.clicked.connect(self.start_download)
        self.youtubeBrowseFileLocation_Button.clicked.connect(self.choose_save_location)

    ## This sections holds the Checked button
        self.home_Button_2.setChecked(True)
        self.home_Button.setChecked(True)



    ## Main page Switching functions
    def switch_to_home(self):
        self.mainPage_stackedWidget.setCurrentIndex(0)

    def switch_to_myFile(self):
        self.mainPage_stackedWidget.setCurrentIndex(1)
    
    def switch_to_tool(self):
        self.mainPage_stackedWidget.setCurrentIndex(2)
    
    ## Download page Switching functions
    def switch_to_youtubePage(self):
        self.downloadPage_stackedWidget.setCurrentIndex(0)
    
    def switch_to_facebookPage(self):
        self.downloadPage_stackedWidget.setCurrentIndex(1)
    
    def switch_to_instagramPage(self):
        self.downloadPage_stackedWidget.setCurrentIndex(2)

    def switch_to_tiktokPage(self):
        self.downloadPage_stackedWidget.setCurrentIndex(3)


    def toggle_maximize(self):
        if self.is_maximized:
            self.showNormal()  # Restore to normal size
        else:
            self.showMaximized()  # Maximize the window
        self.is_maximized = not self.is_maximized  # Toggle the state

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.top_menu_widget.underMouse():
            self.start = event.globalPosition().toPoint()  # Store the start point
            self.setCursor(Qt.CursorShape.ClosedHandCursor)  # Change cursor to indicate dragging

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.top_menu_widget.underMouse():
            delta = event.globalPosition().toPoint() - self.start
            self.move(self.pos() + delta)  # Move the window by the delta
            self.start = event.globalPosition().toPoint()  # Update the start point

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.CursorShape.ArrowCursor)  # Restore cursor after dragging


    def is_resizing(self, event):
        """Check if the cursor is near the window edges for resizing."""
        margin = self.resize_margin
        rect = QRect(self.rect())
        rect.setSize(self.size())
        rect.adjust(0, 0, -margin, -margin)
        return not rect.contains(event.pos())

    def resize_window(self, pos):
        """Resize the window based on the cursor position."""
        delta = pos - self.start
        new_rect = self.rect()
        if self.cursor().shape() == Qt.CursorShape.SizeBDiagCursor:
            new_rect.setBottomRight(new_rect.bottomRight() + delta)
        elif self.cursor().shape() == Qt.CursorShape.SizeFDiagCursor:
            new_rect.setBottomLeft(new_rect.bottomLeft() + QPoint(delta.x(), -delta.y()))
        elif self.cursor().shape() == Qt.CursorShape.SizeVerCursor:
            new_rect.setBottomLeft(new_rect.bottomLeft() + QPoint(0, delta.y()))
        elif self.cursor().shape() == Qt.CursorShape.SizeHorCursor:
            new_rect.setBottomLeft(new_rect.bottomLeft() + QPoint(delta.x(), 0))

    def fetch_formats(self):
        url = self.youtubeURL_Lineedit.text()
        if not url:
            self.youtubeStatus_Label.setText('Please enter a URL.')
            return
        
        self.youtubeStatus_Label.setText('Fetching available formats...')
        QApplication.processEvents()

        try:
            ydl_opts = {
                'quiet': True,
                'noplaylist': True,
                'extractor_args': {'youtube': {'skip': ['webpage']}},
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                formats = info_dict.get('formats', [])
                thumbnail_url = info_dict.get('thumbnail', '')

                # Get and display the video title
                video_title = info_dict.get('title', 'Unknown Title')
                self.youtube_VideoName_Label.setText(video_title)

                duration = info_dict.get('duration', 0)  # Get video duration in seconds

                # Convert duration to HH:MM:SS format
                hours, remainder = divmod(duration, 3600)
                minutes, seconds = divmod(remainder, 60)
                duration_str = f'Duration: {int(hours):02}:{int(minutes):02}:{int(seconds):02}'
                self.youtube_duration_Label.setText(duration_str)

                if thumbnail_url:
                    thumbnail_pixmap = QPixmap()
                    thumbnail_pixmap.loadFromData(ydl.urlopen(thumbnail_url).read())
                    
                    # Scale the pixmap to fit the label's size
                    label_size = self.youtubeThumbnail_Image_Label.size()
                    thumbnail_pixmap = thumbnail_pixmap.scaled(label_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    
                    self.youtubeThumbnail_Image_Label.setPixmap(thumbnail_pixmap)

                if not formats:
                    self.youtubeStatus_Label.setText('No formats available.')
                    return

                self.youtubeFormatSelection_ComboBox.clear()
                self.youtubeFormatSelection_ComboBox.addItem('Select Quality')

                # Filter for HTML5-compatible formats (MP4 and WebM)
                html5_formats = [f for f in formats if f.get('ext') in ['mp4', 'webm']]

                for f in html5_formats:
                    quality = f.get('format_note', 'Unknown Quality')
                    
                    # Retrieve the file size
                    filesize = f.get('filesize', None)
                    if not filesize:
                        # Calculate the file size if not provided
                        ydl_opts_size = ydl_opts.copy()
                        ydl_opts_size['format'] = f.get('format_id')
                        with yt_dlp.YoutubeDL(ydl_opts_size) as ydl_size:
                            size_info = ydl_size.extract_info(url, download=False)
                            filesize = size_info.get('filesize')

                    # Ensure only valid file sizes are processed
                    if filesize is not None and filesize > 0:
                        filesize_mb = f'{filesize / (1024 * 1024):.2f} MB'
                        self.youtubeFormatSelection_ComboBox.addItem(f"{quality} ({f.get('format_id', 'N/A')}) - {filesize_mb}", userData=f.get('format_id'))
                    else:
                        # Skip unknown or invalid file sizes
                        continue
                
                self.youtubeThumbnail_Widget.setHidden(False)
                self.youtubeStatus_Label.setText('Formats fetched.')
        
        except Exception as e:
            self.youtubeStatus_Label.setText(f'Error fetching formats: {str(e)}')


    def start_download(self):
        url = self.youtubeURL_Lineedit.text()
        format_id = self.youtubeFormatSelection_ComboBox.currentData()
        if not url or not format_id:
            self.youtubeStatus_Label.setText('Please enter a URL and select a format.')
            return
        
        if not self.filepath:
            self.youtubeStatus_Label.setText('Please choose a save location.')
            return
        
        self.youtubeStatus_Label.setText('Downloading...')
        self.download_thread = DownloadThread(url, format_id, self.filepath)
        self.download_thread.status.connect(self.update_status)
        self.download_thread.progress.connect(self.progress_update)
        self.youtube_ProgressBar.setHidden(False)
        self.download_thread.start()

    def choose_save_location(self):
                              
        # Ensure video_title is a valid string
        video_title_new = self.youtube_VideoName_Label.text()  # Get the video title from the label text
        if not isinstance(video_title_new, str) or not video_title_new.strip():
            QMessageBox.warning(self, "invali title", "Invalid video title!",)
            return None

        # Set the default file name using the video title
        default_filename = f"{video_title_new.strip()}.mp4"

        # Open the dialog to select a directory only
        directory = QFileDialog.getExistingDirectory(self, "Choose Save Location")

        if directory:  # If a directory is selected
            # Combine the selected directory path with the default file name
            file_path = os.path.join(directory, default_filename)

            # Check if the file already exists
            if os.path.exists(file_path):
                response = QMessageBox.question(
                    self,
                    "File Exists",
                    f"The file '{default_filename}' already exists in the selected location. Do you want to overwrite it?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
                if response == QMessageBox.No:
                    return None  # User chose not to overwrite

            # Save the file path
            self.filepath = file_path  # Save the file path
            self.youtubeLocationURL_Label.setText(file_path)  # Update the label
            return file_path  # Return the complete file path
        else:
            QMessageBox.warning(self, "No Directory Selected", "No directory was selected. Please choose a valid save location.")
            return None  # Return None if no directory is selected


    def update_status(self, status_text):
        pass
    
    def progress_update(self, progress_value):
        self.youtube_ProgressBar.setValue(progress_value)
        




