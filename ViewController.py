#Isaac Lance 1-19-19
#Kellie Hawks 1-27-19
#Using https://github.com/mfitzp/15-minute-apps/blob/master/minesweeper/minesweeper.py
#As a starting point to learn how good apps are designed

import sys
import Model
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import calendar

#Table of UI's
ui_list = ['L0-version0.ui', 'AddEventPopup0.ui', 'DayPopup.ui']
months = ['January', 'February', 'March', 'April','May','June','July','August','September','October','November','December']
days = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
leap_month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
leap_years = [2020, 2024]


class Event_Add_Window(QDialog):
    def __init__(self, m):
        super(Event_Add_Window, self).__init__()
        loadUi('AddEventPopup0.ui', self)
        self.pushButton_save.clicked.connect(self.save_event)
        self.Model = m
        self.Model.exit_data()

    @pyqtSlot()
    def save_event(self):
        mytext = self.plainTextEdit.toPlainText()
        StartTime = self.dateTimeEdit.dateTime()

        StartTime_string = StartTime.toString(self.dateTimeEdit.displayFormat())
        EndTime = self.dateTimeEdit_2.dateTime()
        EndTime_string = EndTime.toString(self.dateTimeEdit_2.displayFormat())

        self.Model.add_event(mytext, StartTime_string, EndTime_string)
        self.accept()
        return


class Day_Window(QDialog):
    def __init__(self):
        super(Day_Window, self).__init__()
        loadUi('DayPopup.ui', self)

class MainViewController(QMainWindow):

    def __init__(self):
        #Super and load ui
        super(MainViewController, self).__init__()
        loadUi('L0-version1.ui', self)
        #Model
        self.Model = Model.Model()
        self.Model.startup_data()
        #Setup
        #This should be in the model!
        self.month = 0;
        self.year = 2019;

        self.setWindowTitle('Test')
        self.label_month.setText(months[self.month])
        self.label_year.setText(str(self.year))
        #Buttons
        self.pushButton_plus.clicked.connect(self.next_year)
        self.pushButton_minus.clicked.connect(self.previous_year)
        self.pushButton_add.clicked.connect(self.add_event_button)
        self.pushButton_next.clicked.connect(self.next_month_button)
        self.pushButton_previous.clicked.connect(self.previous_month_button)
        #Button groups
        self.set_up2()

        #for button in self.buttonGroup_days.buttons():
            #button.clicked.connect(lambda: self.day_button(button.objectName()))

    #hello
    def set_up2(self):
        for button in self.buttonGroup_days.buttons():
            x = (int(button.objectName().split('_')[1]))
            first_WeekayOfMonth, month_Days= calendar.monthrange(self.year, self.month+1)
            #the example of monthrange
            #>>> calendar.monthrange(2019, 1)
            #>>> (1, 31)

            startDate = first_WeekayOfMonth + 1
            endDate = month_Days + first_WeekayOfMonth
            if (x < startDate or x > endDate):
                button.setText('')
                #button.hide()
            else:
                #button.show()
                button.clicked.connect(self.day_button)
                button.setText(str(x - first_WeekayOfMonth))
        return



    #Slots
    @pyqtSlot()
    def add_event_button(self): #Opens the add_event pop up window
        self.add_window_h()
        #Event_Add_Window().exec_()
        return

    @pyqtSlot()
    def next_month_button(self):
        if self.month == 11:
            self.year += 1
            self.label_year.setText(str(self.year))
        self.month += 1
        self.month %= 12
        self.label_month.setText(months[self.month])
        self.set_up2()

    @pyqtSlot()
    def previous_month_button(self):
        #Go back one month. Probably calls determine_day_offset
        if self.month == 0:
            self.year -= 1
            self.label_year.setText(str(self.year))   
        self.month -= 1
        self.month %= 12
        self.label_month.setText(months[self.month])
        self.set_up2()

    @pyqtSlot()
    def day_button(self):
        sender = self.sender()

        #Currently just prints the name of the button
        print(self.buttonGroup_days.checkedButton().objectName())
        Day_Window().exec_()
        #This should load the other .ui and pressing save on that .ui should work


    @pyqtSlot()
    def previous_year(self):
        self.year -= 1
        self.label_year.setText(str(self.year))
        self.set_up2()

    @pyqtSlot()
    def next_year(self):
        self.year += 1
        self.label_year.setText(str(self.year))
        self.set_up2()

    #Window helpers
    def add_window_h(self):
        addDialog = Event_Add_Window(self.Model)
        if addDialog.exec():
            print("True")
        else:
            print("False")
        return

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
