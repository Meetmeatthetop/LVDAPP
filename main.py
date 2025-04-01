import sys
import auto_update  # Import the auto-update script
from PySide6.QtWidgets import QApplication
from app import MyDownloadApp 

# Run the auto-update before starting the app
auto_update.update_dependencies()  
# Initialize the application
app = QApplication(sys.argv)
window = MyDownloadApp()
window.show()
app.exec()
