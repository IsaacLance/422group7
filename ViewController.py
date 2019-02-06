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

'''
Table of UI's used by our app. '.ui' files are created using the QT Designer software
and can be converted to a .py file which can be human-read to determine the available
ui elements. Elements referenced in this code are avaialable due to the call:
'loadUi(ui[x], self)'
This call is responsible for bringing those elements into the scope.
'''
ui = ['L0-version1.ui', 'AddEventPopup0.ui', 'DayPopup.ui']
'''
This class inherits QDialog. QDialog widgets are usually created by an existing main view
to handle user input or send a specific message, and then are closed. Their lifetime is short.
This window let's the user add a new event to the model.
'''
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

    def convert_to_datetime_obj(self, day, time):
        '''
        args: day (string) , time (string)
        returns: A datetime object
        side effects: N/A
        description: Storing values at datetime objects means we can easily use datetime methods for various
        '''
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
        side effects: saves event info from the dialog to the model, or nothing if invalid event
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
        #Test if valid event
        if end < start:
            print("Error: event ends before it starts")
            return
        #Call models add_event function to store the event
        self.m.add_event(title, start, end)
        #Self.accept makes the return code of exec "True" otherwise it's false (if the user were to exit the window)
        self.accept()
        return


class Day_Window(QDialog):
    def __init__(self, model, day, events):
        '''
        The Day_Window class is used whenever the user clicks a specific day button that is active.
        It is passed a pointer to the model so that it can call model functions.
        The window displays the given day and events on that day.
        '''
        super(Day_Window, self).__init__()
        loadUi(ui[2], self)
        self.m = model
        self.day = day
        self.events = events
        self.label_date.setText(calendar.month_name[(self.m.month)] + ' ' + self.day + ' ' + str(self.m.year))
        self.pushButton_delete.clicked.connect(self.delete_event)


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

    @pyqtSlot()
    def delete_event(self):
        for num in range(1, len(self.events)+2):
            label = getattr(self, 'label_{}'.format(num))
            label.setTextInteractionFlags(Qt.TextSelectableByMouse);
            if label.hasSelectedText() != False:
                print("this kind of works")
                label.setStyleSheet('color: blue')
                #ev = self.events[num-1]
                
                label.hide()
                #self.m.delete_event(ev.title, ev.start.strftime('%a %b %d %Y %H:%M:%S'), ev.end.strftime('%a %b %d %Y %H:%M:%S'))
        return







class MainViewController(QMainWindow):
    '''
    The MainViewController is the parent window of every other window. It's GUI is always present and visible,
    but not always clickable when child windows have the focus. The window has 42 day buttons in a grid which
    can be clicked to open a child view, if they are valid buttons for a given month and year. There are also
    buttons to change the displayed month and year, as well as an "add event" button to add events to the calendar.
    '''
    def __init__(self):
        #Super init and load the ui
        super(MainViewController, self).__init__()
        loadUi(ui[0], self)
        #PyQT has bugs when the buttonGroup is set to exclusive
        self.buttonGroup_days.setExclusive(False)
        #Setup Model
        now = datetime.date.today()
        self.m = CalendarModel(now.month, now.year)
        #Set title of window
        self.setWindowTitle('Calendar')
        #Connect Buttons
        self.pushButton_plus.clicked.connect(self.next_year)
        self.pushButton_minus.clicked.connect(self.previous_year)
        self.pushButton_add.clicked.connect(self.add_event_button)
        self.pushButton_next.clicked.connect(self.next_month_button)
        self.pushButton_previous.clicked.connect(self.previous_month_button)
        #Button group buttons
        for button in self.buttonGroup_days.buttons():
            button.clicked.connect(self.day_button)
        #Update based on model data
        self.refresh()

    def refresh(self):
        '''
        args: N/A
        returns: N/A
        side effects: labels and buttons update to match the model
        description: refresh is the function called by the view controller whenever model data
        has changed. This way, the user always sees a representation of the current model.
        '''
        #Set: Month, Year
        self.label_year.setText(str(self.m.year))
        self.label_month.setText(calendar.month_name[(self.m.month)])
        #An example of monthrange, the function that returns the number of days in a month and the day
            #the month starts on:
            #>>> calendar.monthrange(2019, 1)
            #>>> (1, 31)
            # "(1, 31)" is saying: (Tuesday, 31 days in that month)
        first_day, month_Days= calendar.monthrange(self.m.year, self.m.month)
        #Set: days
        for button in self.buttonGroup_days.buttons():
            #This line requires knowledge of the .ui file: the day buttons have names like pushButton_*
            #where "*" is some string of an int 1-42. So this line extracts that int and puts it in x
            x = (int(button.objectName().split('_')[1]))
            #Fixing off by one error
            startDate = first_day + 1
            #Getting last day
            endDate = month_Days + first_day
            #Setting valid days/invalid days
            if (x < startDate or x > endDate):
                button.setText('')
                button.setEnabled(False)
            else:
                button.setEnabled(True)
                events = self.m.get_day_events(x - first_day)
                if events == None:
                    event_str = ""
                else:
                    event_str = "\nEvents: " + str(len(events))
                button.setText(str(x - first_day) + "\n" + event_str)
        return


    #
    #pyqtSlots (the decorator wraps these functions in a function connecting them to signals)
    #
    @pyqtSlot()
    def add_event_button(self): #Opens the add_event pop up window
        #TODO: Either use this sub-wrapper or delete it
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
        day = abstract_button.text().split("\n")[0]

        events = self.m.get_day_events(day)
        day_dialog = Day_Window(self.m, day, events)
        day_dialog.exec()

        abstract_button.toggle()
        return

    @pyqtSlot()
    def previous_year(self):
        '''
        side effects: the model's year goes down by 1 and the view is refreshed
        description:  Call on the model to decrease the year by 1
        '''
        self.m.year -= 1
        self.refresh()

    @pyqtSlot()
    def next_year(self):
        '''
        side effects: the model's year goes up by 1 and the view is refreshed
        description:  Call on the model to increase the year by 1
        '''
        self.m.year += 1
        self.refresh()

    #Window helpers
    def add_window_h(self):
        '''
        side effects: opens
        description: Storing values at datetime objects means we can easily use datetime methods for various
        returns: a boolean whether self.accept() was called or not. (Whether the user clicked save or the "X")
        '''
        addDialog = Event_Add_Window(self.m)
        if addDialog.exec():
            return(True)
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainViewController()
    widget.show()
    sys.exit(app.exec_())
