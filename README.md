# **Line Video Downloader**  
_A powerful cross-platform video downloader with a modern UI._  

## **Features**  
✅ Download videos from YouTube and other platforms using `yt-dlp`  
✅ Modern **PySide6 (Qt-based) GUI**  
✅ Supports multi-threaded downloads for better performance  
✅ Video format selection  
✅ FFmpeg integration for merging video and audio  
✅ Platform-independent (Windows, Linux, macOS)  

---

## **Installation**  

### **1️⃣ Install Dependencies**  
Make sure you have Python installed (`>=3.8`). Then, install the required libraries:  

```sh
pip install PySide6 yt-dlp ffmpeg-python
```

You'll also need **FFmpeg**:  
- **Windows:** Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to `PATH`.  
- **Linux/macOS:** Install via package manager:  
  ```sh
  sudo apt install ffmpeg  # Ubuntu/Debian  
  brew install ffmpeg  # macOS  
  ```

---

## **Usage**  

### **Run the App**  
After installing dependencies, run:  

```sh
python main.py
```

This launches the **Line Video Downloader** GUI.  

---

## **How It Works**  

1. **Enter a YouTube (or other platform) URL.**  
2. **Fetch available formats.**  
3. **Select desired video quality.**  
4. **Choose a save location.**  
5. **Start downloading!**  

---

## **Project Structure**  

```
📂 Line Video Downloader  
 ├── app.py                 # Main application logic  
 ├── main.py                # Entry point for running the app  
 ├── youtubeDownloadThread.py  # Background thread for downloading  
 ├── ui_lvdApp.py           # UI components (generated from Qt Designer)  
 ├── resource.qrc           # Resource file (icons, images, etc.)  
 ├── resource_c.py          # Compiled resources for Qt  
 ├── .gitattributes         # Git-related settings  
 └── README.md              # This documentation  
```

---

## **Contributing**  
Feel free to submit issues or contribute via pull requests!  

---

## **License**  
This project is **open-source** under the **MIT License**.  

---

Would you like me to **customize or add more details**? 🚀
