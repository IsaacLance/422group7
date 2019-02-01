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
import datetime

#Table of UI's
ui = ['L0-version1.ui', 'AddEventPopup0.ui', 'DayPopup.ui']


class Event_Add_Window(QDialog):
    def __init__(self, model):
        super(Event_Add_Window, self).__init__()
        loadUi(ui[1], self)
        self.pushButton_save.clicked.connect(self.save_event)
        self.m = model

    #Helpers
    def convert_to_datetime_obj(self, day, time):
        print(time)
        print(day)
        time_string = day + " " + time
        datetime_object = datetime.datetime.strptime(time_string, '%a %b %d %Y %H:%M:%S')
        
        return datetime_object
    #Slots
    @pyqtSlot()
    def save_event(self):
        title = self.plainTextEdit.toPlainText()
        #Convert start time entered to dt object
        startTime = self.timeEdit.time().toString()
        #startTime_string = startTime.toString(self.timeEdit.displayFormat())
        startDate = self.dateEdit.date().toString()
        #startDate_string = startDate.toString(self.dateEdit.displayFormat())
        
        start = self.convert_to_datetime_obj(startDate, startTime)
        #convert end time entered to dt object
        endTime = self.timeEdit_2.time().toString()
        #endTime_string = endTime.toString(self.timeEdit_2.displayFormat())
        endDate = self.dateEdit_2.date().toString()
        #endDate_string = endDate.toString(self.dateEdit_2.displayFormat())
        
        end = self.convert_to_datetime_obj(endDate, endTime)
        print()
        self.m.add_event(title, start, end)
        #Self.accept makes the return code of exec "True" otherwise it's false (Like if you exit the window)
        self.accept()
        return


class Day_Window(QDialog):
    def __init__(self):
        super(Day_Window, self).__init__()
        loadUi(ui[2], self)

class MainViewController(QMainWindow):

    def __init__(self):
        #Super and load ui
        super(MainViewController, self).__init__()
        loadUi(ui[0], self)
        #TEST
        self.buttonGroup_days.setExclusive(False)
        #Model
        now = datetime.date.today()
        self.m = Model.CalendarModel(now.month, now.year)

        self.setWindowTitle('Test')
        #Buttons
        self.pushButton_plus.clicked.connect(self.next_year)
        self.pushButton_minus.clicked.connect(self.previous_year)
        self.pushButton_add.clicked.connect(self.add_event_button)
        self.pushButton_next.clicked.connect(self.next_month_button)
        self.pushButton_previous.clicked.connect(self.previous_month_button)
        #Button groups
        self.refresh()

        #for button in self.buttonGroup_days.buttons():
            #button.clicked.connect(lambda: self.day_button(button.objectName()))

    #hello
    def refresh(self):
        #Month, Year
        self.label_year.setText(str(self.m.year))
        self.label_month.setText(calendar.month_name[(self.m.month)])
        for button in self.buttonGroup_days.buttons():
            x = (int(button.objectName().split('_')[1]))
            first_day, month_Days= calendar.monthrange(self.m.year, self.m.month)
            #the example of monthrange
            #>>> calendar.monthrange(2019, 1)
            #>>> (1, 31)

            startDate = first_day + 1
            endDate = month_Days + first_day
            if (x < startDate or x > endDate):
                button.setText('')
                #button.hide()
            else:
                #button.show()
                button.clicked.connect(self.day_button)
                button.setText(str(x - first_day))
        return



    #Slots
    @pyqtSlot()
    def add_event_button(self): #Opens the add_event pop up window
        self.add_window_h()
        return

    @pyqtSlot()
    def next_month_button(self):
        self.m.next_month()
        self.refresh()

    @pyqtSlot()
    def previous_month_button(self):
        self.m.prev_month()
        self.refresh()

    @pyqtSlot()
    def day_button(self):

        #Currently just prints the name of the button
        print(self.buttonGroup_days.checkedButton().objectName())
        Day_Window().exec_()
        self.buttonGroup_days.checkedButton().toggle()
        #This should load the other .ui and pressing save on that .ui should work
        return

    @pyqtSlot()
    def previous_year(self):
        self.year -= 1
        self.label_year.setText(str(self.year))
        self.refresh()

    @pyqtSlot()
    def next_year(self):
        self.year += 1
        self.label_year.setText(str(self.year))
        self.refresh()

    #Window helpers
    def add_window_h(self):
        addDialog = Event_Add_Window(self.m)
        if addDialog.exec():
            print("True")
        else:
            print("False")
        return

    #Helpers

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainViewController()
    widget.show()
    sys.exit(app.exec_())
