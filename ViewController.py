#Isaac Lance 1-19-19
#Using https://github.com/mfitzp/15-minute-apps/blob/master/minesweeper/minesweeper.py
#As a starting point to learn how good apps are designed

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

#Table of UI's
ui_list = ['L0-version0.ui']
months = ['January', 'Febuary', 'March', 'April','May','June','July','August','September','November','December']

class MainViewController(QMainWindow):

	def __init__(self):
		super(MainViewController, self).__init__()
		loadUi(ui_list[0], self)
		self.setWindowTitle('Test')
		self.label_month.setText(months[0])
		#Buttons
		self.pushButton_add.clicked.connect(self.add_event_button)
		self.pushButton_next.clicked.connect(self.next_month_button)
		self.pushButton_previous.clicked.connect(self.previous_month_button)


	@pyqtSlot()
	def add_event_button(self):
		self.setWindowTitle('Okay!')

	@pyqtSlot()
	def next_month_button(self):
		self.label_month.setText()

	@pyqtSlot()
	def previous_month_button(self):
		self.label_month.setText()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = MainViewController()
	widget.show()
	sys.exit(app.exec_())
