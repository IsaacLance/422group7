#Isaac Lance 1-19-19
#Kellie Hawks 1-27-19
#Luyao Wang 1-28-19
#Using https://github.com/mfitzp/15-minute-apps/blob/master/minesweeper/minesweeper.py
#As a starting point to learn how good apps are designed

import sys
from Model import CalendarModel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import calendar
import datetime

"""
Table of UI's used by our app. '.ui' files are created using the QT Designer software
and can be converted to a .py file which can be human-read to determine the available
ui elements. Elements referenced in this code are avaialable due to the call:
'loadUi(ui[x], self)'
This call is responsible for bringing those elements into the scope.
ui = ['L0-version1.ui', 'AddEventPopup0.ui', 'DayPopup.ui']
"""
ui = ['L0-version1.ui', 'AddEventPopup0.ui', 'DayPopup.ui']
"""
This class inherits QDialog. QDialog widgets are usually created by an existing main view
to handle user input or send a specific message, and then are closed. Their lifetime is short.
This window let's the user add a new event to the model.
"""
class Event_Add_Window(QDialog):
    def __init__(self, model):
        #Call super of QDialog
        super(Event_Add_Window, self).__init__()
        #Load the correct ui (and therefore all it's elements)
        loadUi(ui[1], self)
        """
        PyQT uses signals and slots to handle message passing between ui elements/widgets and
        functions. In the following line, a pushButton has it's "clicked" signal connected to the
        slot "save_event"
        The single comment line above shows the relationship between this specific call and the types.
        """
        #   .nameOfButton___.signal_.connect(self.some_slot)
        self.pushButton_save.clicked.connect(self.save_event)

        #These lines just set the date and time selection values to be the current date/time for
        #user convienence
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())
        self.timeEdit.setTime(QTime.currentTime())
        self.timeEdit_2.setTime(QTime.currentTime())
        #The model is passed from the MainView so that the dialog can have the model save user data.
        self.m = model


    #Helpers
    def convert_to_datetime_obj(self, day, time) -> datetime:
        """
        args: day (string) , time (string)
        returns: A datetime object
        description: Storing values at datetime objects means we can easily use datetime methods for various
        functions, ex: easily check if a date falls before or after another date
        """
        #Concatenate strings
        time_string = day + " " + time
        #strptime accepts a string and format to construct a datetime object matching the string information
        datetime_object = datetime.datetime.strptime(time_string, '%a %b %d %Y %H:%M:%S')

        return datetime_object

    #pyqtSlots (the decorator wraps these functions in a function connecting them to signals)
    @pyqtSlot()
    def save_event(self):
        """
        args: N/A
        returns: N/A
        side effects: saves event info from the dialog to the model
        description: This function is called when a user clicks to save the event they are entering in the dialog
        it has no explicit arguments but the input fields are used. The model handles saving the event.
        """
        #Get title from the title text edit
        title = self.plainTextEdit.toPlainText()
        #Get start date/time and convert to datetime object
        startDate = self.dateEdit.date().toString()
        startTime = self.timeEdit.time().toString()
        start = self.convert_to_datetime_obj(startDate, startTime)
        #Get end date/time and convert to datetime object
        endDate = self.dateEdit_2.date().toString()
        endTime = self.timeEdit_2.time().toString()
        end = self.convert_to_datetime_obj(endDate, endTime)
        #Call models add_event function to store the event
        self.m.add_event(title, start, end)
        #Self.accept makes the return code of exec "True" otherwise it's false (if the user were to exit the window)
        self.accept()
        return


class Day_Window(QDialog):
    def __init__(self, model: CalendarModel, day: str, events: []):
        super(Day_Window, self).__init__()
        loadUi(ui[2], self)
        self.m = model
        self.day = day
        self.events = events
        self.label_date.setText(calendar.month_name[(self.m.month)] + ' ' + self.day + ' ' + str(self.m.year))

        if self.events != None:
            for num in range(1, len(self.events)+1):
                label = getattr(self, 'label_{}'.format(num))
                label.show()
                ev = self.events[num-1]

                mystring = ev.title + ev.start.strftime('%a %b %d %Y %H:%M:%S')+ '   to   ' + ev.end.strftime('%a %b %d %Y %H:%M:%S')
                print(mystring)
                label.setText(mystring)
            for num in range(len(self.events)+1, 31):
                label = getattr(self, 'label_{}'.format(num))
                label.hide()

        else:
            for num in range(1, 31):
                label = getattr(self, 'label_{}'.format(num))
                label.hide()






class MainViewController(QMainWindow):

    def __init__(self):
        #Super and load ui
        super(MainViewController, self).__init__()
        loadUi(ui[0], self)
        #TEST
        self.buttonGroup_days.setExclusive(False)
        #Model
        now = datetime.date.today()
        self.m = CalendarModel(now.month, now.year)

        self.setWindowTitle('Calendar')
        #Buttons
        self.pushButton_plus.clicked.connect(self.next_year)
        self.pushButton_minus.clicked.connect(self.previous_year)
        self.pushButton_add.clicked.connect(self.add_event_button)
        self.pushButton_next.clicked.connect(self.next_month_button)
        self.pushButton_previous.clicked.connect(self.previous_month_button)
        #Button groups
        #self.buttonGroup_days.buttonClicked[QAbstractButton].connect(self.day_button)
        self.refresh()
        for button in self.buttonGroup_days.buttons():
            button.clicked.connect(self.day_button)

    #hello
    def refresh(self):
        """
        args: N/A
        returns: N/A
        side effects: show the first weekdate of a month
        description: This function is called for showing first date of a month.
        """
        self.label_year.setText(str(self.m.year))
        self.label_month.setText(calendar.month_name[(self.m.month)])
        for button in self.buttonGroup_days.buttons():
            x = (int(button.objectName().split('_')[1]))                                #x means the day buttons
            first_day, month_Days= calendar.monthrange(self.m.year, self.m.month)       #it will gets weekday of first day of the month and number of days in month, for the specified year and month.
            #the example of monthrange
            #>>> calendar.monthrange(2019, 1)
            #>>> (1, 31)

            startDate = first_day + 1                                                   #the button number start from 0, for matching up you will add 1
            endDate = month_Days + first_day
            if (x < startDate or x > endDate):                                          #set empty button to '', otherwise print the day number
                button.setText('')
                button.setEnabled(False)
            else:
                button.setEnabled(True)
                button.setText(str(x - first_day))
        return



    #pyqtSlots (the decorator wraps these functions in a function connecting them to signals)
    @pyqtSlot()
    def add_event_button(self): #Opens the add_event pop up window
        self.add_window_h()
        return

    @pyqtSlot()
    def next_month_button(self):
        self.m.next_month()
        self.refresh()
        return

    @pyqtSlot()
    def previous_month_button(self):
        self.m.prev_month()
        self.refresh()
        return

    @pyqtSlot()
    def day_button(self):
        abstract_button = self.sender()
        day = abstract_button.text()

        events = self.m.get_day_events(day)
        day_dialog = Day_Window(self.m, day, events)
        day_dialog.exec()

        abstract_button.toggle()
        return

    @pyqtSlot()
    def previous_year(self):
        self.m.year -= 1
        self.refresh()

    @pyqtSlot()
    def next_year(self):
        self.m.year += 1
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
