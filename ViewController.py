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

    @pyqtSlot()
    def save_event(self):
        title = self.plainTextEdit.toPlainText()
        
        StartTime = self.dateTimeEdit.dateTime()
        StartTime_string = StartTime.toString(self.dateTimeEdit.displayFormat())

        month = StartTime_string.split(' ')[0].split('/')[0]
        year = StartTime_string.split(' ')[0].split('/')[2]
        day = StartTime_string.split(' ')[0].split('/')[1]
        
        EndTime = self.dateTimeEdit_2.dateTime()
        EndTime_string = EndTime.toString(self.dateTimeEdit_2.displayFormat())

        self.m.add_event(title, StartTime_string, EndTime_string)
        #self.m.add_event(title, year, month, StartTime_string, EndTime_string)
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
