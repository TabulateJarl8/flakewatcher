import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from ui_main import Ui_MainWindow

class FlakeWatcherMain(QMainWindow, Ui_MainWindow):
	def __init__(self, *args, obj=None, **kwargs):
		super(FlakeWatcherMain, self).__init__(*args, **kwargs)

		self.setupUi(self)

app = QApplication(sys.argv)
window = FlakeWatcherMain()
window.show()
app.exec()