#Isaac Lance 1-19-19
#Using https://github.com/mfitzp/15-minute-apps/blob/master/minesweeper/minesweeper.py
#As a starting point to learn how good apps are designed

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

#Table of UI's
ui_list = ['L0-version0.ui', 'L0-version0a.ui']

class MainViewController(QMainWindow):
	
	def __init__(self):
		super(MainViewController, self).__init__()
		loadUi(ui_list[1], self)
		self.setWindowTitle('Test')
		#Buttons
		self.pushButton_add.clicked.connect(self.add_event_button)
	
	@pyqtSlot()
	def add_event_button(self):
		self.setWindowTitle('Okay!')
		print(len(self.buttonGroup_days.buttons()))
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = MainViewController()
	widget.show()
	sys.exit(app.exec_())