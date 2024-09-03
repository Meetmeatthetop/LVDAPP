from PySide6.QtWidgets import QApplication
from app import MyDownloadApp 
import sys

app = QApplication(sys.argv)
window = MyDownloadApp()
window.show()
app.exec()  # Call exec() with parentheses
 