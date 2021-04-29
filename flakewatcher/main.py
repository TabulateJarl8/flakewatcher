import sys
import time
import logging
import subprocess

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

try:
	from ui.ui_main import Ui_MainWindow
except ModuleNotFoundError:
	from .ui.ui_main import Ui_MainWindow

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)


class Worker(QObject):
	finished = pyqtSignal()
	intReady = pyqtSignal(str)

	def start_flake_process(self):
		try:
			p = subprocess.check_output(['flake8', '--ignore', 'W191,E501,E266,E402,F403,E261,F405', '/home/tabulate/flakewatcher/flakewatcher/main.py']).decode('utf-8')
		except Exception as e:
			p = str(e.output.decode('utf-8'))

		logging.debug(f'{p=}')
		return p

	@pyqtSlot()
	def procCounter(self): # A slot takes no params
		while True:
			self.intReady.emit(self.start_flake_process())
			time.sleep(2)

		self.finished.emit()


class FlakeWatcherMain(QMainWindow, Ui_MainWindow):
	def __init__(self, *args, obj=None, **kwargs):
		super(FlakeWatcherMain, self).__init__(*args, **kwargs)

		self.process = None

		self.obj = Worker()
		self.thread = QThread()
		self.obj.intReady.connect(self.update_label)
		self.obj.moveToThread(self.thread)
		self.obj.finished.connect(self.thread.quit)
		self.thread.started.connect(self.obj.procCounter)
		self.thread.start()

		self.setupUi(self)

	def update_label(self, text):
		self.FlakeOutput.setText('{}'.format(text))


def startQtApp():
	app = QApplication(sys.argv)
	window = FlakeWatcherMain()
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	startQtApp()
