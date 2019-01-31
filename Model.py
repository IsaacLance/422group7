#Chandler Potter 1/21/19 CIS 422
import shelve
import Event

class CalendarModel:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.startup_data()
        self.s = None
        return
    #INIT/EXIT HELPERS
    def startup_data(self):
        print("Model startup")
        print("Year: " +str(self.year))
        print("Month: " +str(self.month))
        self.s = shelve.open("data", writeback = True)
        if not('events' in self.s):
            print("No events key found in shelve. Created new events list.")
            self.s['events'] = []
        return

    def exit_data(self):
        print("Model exit")
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
        print("Added event")
        print(title)
        print(start)
        print(end)
        self.s['events'].append(Event(title, start, end))

        return
    #Getters
    def get_year(self):
        #get the current year
        #print(self.s[event]['year'])
        return self.year

    def get_month(self):
        #get the current month
        #print(self.s[event]['month'])
        return self.month   
    #Helpers
    '''
    These don't work yet
    def search_event(self, event)
        #The format of the event must be "a-b-c"
        #here a means month,b means day, c means year
        if event in self.s['events']:
            return True
        else:
            return False    

    def delete_event(month, day): #deletes an event at specified date (month, day)
        return
    
    def get_event(month, day): #retrieves an event at specified date (month, day) and presents that to the user in the ViewController
        return
    '''