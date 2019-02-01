#Chandler Potter 1/21/19 CIS 422
import shelve
from Event import CalendarEvent

class CalendarModel:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.startup_data()
        return

    #INIT/EXIT HELPERS
    def startup_data(self):
        print("Model startup")
        print("Year: " +str(self.year))
        print("Month: " +str(self.month))
        s = shelve.open("data", writeback = True)

        if not('events' in s):
            print("No events key found in shelve. Created new events list.")
            s['events'] = []
        else:
            print(s['events'])
        s.close()
        return

    def exit_data(self):
        print("Model exit")
        s.close()
        return

    #Button responses/ setters
    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.year += 1
            self.month = 1
        return

        return
    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.year -= 1
            self.month = 12
        return

    def add_event(self, title, start, end): #adds event at specified date (month, day)
        #EVents should only be added if they are not duplicates
        s = shelve.open("data", writeback = True)
        print("Adding event:")
        print(s['events'])
        e = CalendarEvent(title, start, end)
        print(e.title)
        s['events'].append(e)
        print(s['events'])
        s.close()
        return
    #Getters
    def get_year(self):
        #get the current year
        #print(s[event]['year'])
        return self.year

    def get_month(self):
        #get the current month
        #print(s[event]['month'])
        return self.month

    def get_day_events(self, day_num): #retrieves events and presents that to the user in the ViewController. returns none if no events matched.
        s = shelve.open("data", writeback = True)
        event_list = []
        for event in s['events']:
            '''
            print('Title: ' + event.title)
            print('Event  Input')
            print(str(event.start.day) +'      '+ str(day_num))
            print(str(event.start.month) +'      '+ str(self.month))
            print(str(event.start.year) +'      '+ str(self.year))
            '''
            if event.start.year == self.year and event.start.month == self.month and event.start.day == int(day_num):
                event_list.append(event)
        
        if not event_list:
            return None
            
        #date_time = event_list[0].start.strftime('%a %b %d %Y %H:%M:%S')
        #print(date_time)
        
        return event_list
        
    #Helpers
    def search_event(self, title, start, end):
        #Search for an event and return it's index or None
        s = shelve.open("data", writeback = True)
        index = -1
        for index, event in enumerate(s['events']):
            if event.title == title and event.start == start and event.end == end:
                s.close()
                return index
        s.close()
        return None


    def delete_event(self, title, start, end): #deletes an event at specified date (month, day)

        return
