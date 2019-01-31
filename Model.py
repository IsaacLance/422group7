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
        #EVents should only be added if they are not duplicates
        print("Adding event:")
        self.s['events'].append(Event(title, start, end))
        print(self.s['events'][-1].title)
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
    
    def get_day_events(month, day): #retrieves events and presents that to the user in the ViewController
        return
        
    #Helpers
    def search_event(self, title, start, end):
        #Search for an event and return it's index or None
        index = -1
        for index, event in enumerate(self.s['events']):
            if event.title == title and event.start == start and event.end == end:
                return 
                    
                
    def delete_event(self, title, start, end): #deletes an event at specified date (month, day)
        
        return
        
        
        
        
        
        
        
        
        
        
    