#Isaac Lance 1-19-19
#Kellie Hawks 1-27-19
#Using https://github.com/mfitzp/15-minute-apps/blob/master/minesweeper/minesweeper.py
#As a starting point to learn how good apps are designed

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

#Table of UI's
ui_list = ['L0-version0.ui']
months = ['January', 'February', 'March', 'April','May','June','July','August','September','October','November','December']
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
leap_years = [2020, 2024]


class Event_Add_Window(QDialog):
	def __init__(self):
		super(Event_Add_Window, self).__init__()
		loadUi('AddEventPopup0.ui', self)
		self.pushButton_save.clicked.connect(self.save_event_button)


	def save_event_button(self):
		mytext = self.plainTextEdit.toPlainText()
		StartTime = self.dateTimeEdit.dateTime()

		StartTime_string = StartTime.toString(self.dateTimeEdit.displayFormat())
		EndTime = self.dateTimeEdit_2.dateTime()
		EndTime_string = EndTime.toString(self.dateTimeEdit_2.displayFormat())

		with open('data.txt', 'w') as f:
			f.write(mytext)
			f.write(StartTime_string)
			f.write('\n')
			f.write(EndTime_string)




class Day_Window(QDialog):
	def __init__(self):
		super(Day_Window, self).__init__()
		loadUi('DayPopup.ui', self)

class MainViewController(QMainWindow):

	def __init__(self):
		self.month = 0;
		self.year = 2019;

		super(MainViewController, self).__init__()
		loadUi(ui_list[0], self)
		self.setWindowTitle('Test')
		self.label_month.setText(months[self.month])
		#Buttons
		self.pushButton_add.clicked.connect(self.add_event_button)
		self.pushButton_next.clicked.connect(self.next_month_button)
		self.pushButton_previous.clicked.connect(self.previous_month_button)
		#Button groups
		self.set_up()

		#for button in self.buttonGroup_days.buttons():
			#button.clicked.connect(lambda: self.day_button(button.objectName()))

	#hello
	def set_up(self):
		x = 1
		for button in self.buttonGroup_days.buttons():
			if (x > month_days[self.month]):
				button.setText('')
			else:
				button.clicked.connect(self.day_button)
				if (not self.year in leap_years):
					day = month_days[self.month];
					button.setText(str(x))
				else:
					day = leap_month_days[self.month];
					button.setText(str(x))
				x += 1


	#Slots
	@pyqtSlot()
	def add_event_button(self): #Opens the add_event pop up window
		Event_Add_Window().exec_()

	@pyqtSlot()
	def next_month_button(self):
		self.month += 1
		self.month %= 12
		self.label_month.setText(months[self.month])
		self.set_up()

	@pyqtSlot()
	def previous_month_button(self):
		#Go back one month. Probably calls determine_day_offset
		self.month -= 1
		self.month %= 12
		self.label_month.setText(months[self.month])
		self.set_up()

	@pyqtSlot()
	def day_button(self):
		sender = self.sender()

		#Currently just prints the name of the button
		print(self.buttonGroup_days.checkedButton().objectName())
		Day_Window().exec_()
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
