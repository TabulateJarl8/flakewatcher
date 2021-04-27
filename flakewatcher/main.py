import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QProcess
from ui.ui_main import Ui_MainWindow
import subprocess
import time
import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

class FlakeWatcherMain(QMainWindow, Ui_MainWindow):
	def __init__(self, *args, obj=None, **kwargs):
		super(FlakeWatcherMain, self).__init__(*args, **kwargs)

		self.process = None

		self.setupUi(self)

		self.StartButton.clicked.connect(self.start_flake_process)

	def start_flake_process(self):
		if self.process is None: # No process running
			self.process = QProcess()
			self.process.readyReadStandardError.connect(self.handle_process_stderr)
			self.process.readyReadStandardOutput.connect(self.update_flake_output_text)
			self.process.stateChanged.connect(self.handle_state)
			self.process.finished.connect(self.process_finished)
			self.process.start('flake8', ['--ignore', 'W191,E501,E266,E402,F403,E261,F405', '/home/tabulate/TabulateCalc/main.py'])
			logging.debug('process started')

	def process_finished(self):
		self.process = None
		logging.debug('Process removed')

	def update_flake_output_text(self):
		logging.debug('stdout')
		data = self.process.readAllStandardOutput().data().decode()
		logging.debug(f"{data=}")
		self.FlakeOutput.setText(data)

	def handle_state(self, state):
		states = {
			QProcess.NotRunning: 'Not running',
			QProcess.Starting: 'Starting',
			QProcess.Running: 'Running',
		}
		state_name = states[state]
		logging.debug(f"State changed: {state_name}")

	def handle_process_stderr(self):
		err = self.process.readAllStandardError().data().decode().strip()
		logging.warning(err)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = FlakeWatcherMain()
	window.show()
	sys.exit(app.exec_())