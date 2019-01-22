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


class Event_Add_Window(QDialog):
	def __init__(self):
		super(Event_Add_Window, self).__init__()
		loadUi('AddEventPopup0.ui', self)

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
		#Button groups
		self.buttonGroup_days.buttonClicked.connect(self.day_button)

		#for button in self.buttonGroup_days.buttons():
			#button.clicked.connect(lambda: self.day_button(button.objectName()))

	#Slots
	@pyqtSlot()
	def add_event_button(self): #Opens the add_event pop up window
		Event_Add_Window().exec_()

	@pyqtSlot()
	def next_month_button(self):
		self.label_month.setText()

	@pyqtSlot()
	def previous_month_button(self):
		#Go back one month. Probably calls determine_day_offset
		self.label_month.setText()

	@pyqtSlot()
	def day_button(self):
		#Currently just prints the name of the button
		print(self.buttonGroup_days.checkedButton().objectName())
		#This should load the other .ui and pressing save on that .ui should work
	#Helpers
	def determine_day_offset(date):
		#Should fiugre out what button should be 1 and what button should be the last day of month etc.
		#The unused buttons should be hidden
		return


if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = MainViewController()
	widget.show()
	sys.exit(app.exec_())
