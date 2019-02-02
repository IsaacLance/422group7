#Chandler Potter 1/21/19 CIS 422
import shelve
from Event import CalendarEvent

class CalendarModel:         											#CalendarModel class
    def __init__(self, month, year):     								#init
        self.month = month  											#assign the month
        self.year = year                								#assign the year
        self.startup_data()             								#call startup data to get set up
        return

    #INIT/EXIT HELPERS
    def startup_data(self):           									#startup_data function
        print("Model startup")            								#print to terminal confirming Model startup
        print("Year: " +str(self.year))   								#print the year the calendar is set to 
        print("Month: " +str(self.month)) 								#print the month the calendar is set to
        s = shelve.open("data", writeback = True)  						#open the pickled file

        if not('events' in s):   										#if there is no events key in "s", create one
            print("No events key found in shelve. Created new events list.")  #print that a new "events" key was created to store events to
            s['events'] = []  											#create events key
        else:
            print(s['events'])  										#prints saved events
        s.close()   													#close pickled file
        return

    def exit_data(self):   												#exit_data function
        print("Model exit") 											#prints that model is exiting
        s.close()           											#close picked file
        return

    #Button responses/ setters
    def next_month(self):    											#moves to next month
        self.month += 1      											#advance month by 1
        if self.month == 13:  											#if the month is 13, the next 3 lines will advance the year and then reset month to be 1
            self.year += 1
            self.month = 1
        return

        return
    def prev_month(self):  												#moves to the previous month
        self.month -= 1		 											#move the month back by 1
        if self.month == 0:  											#if the month is 0, the next 3 lines will change the year to the prevous year and then reset the month to be 12
            self.year -= 1
            self.month = 12
        return

    def add_event(self, title, start, end): 							#adds event at specified date (month, day)
        																#Events should only be added if they are not duplicates
        s = shelve.open("data", writeback = True)  						#open pickle file
        print("Adding event:")  										#print out "Adding event:" and print current events
        print(s['events'])
        e = CalendarEvent(title, start, end) 							#get event set up to be added
        print(e.title)      											#print title of event
        s['events'].append(e) 											#append event to s with events key
        print(s['events']) 												#print new current events
        s.close()  														#close pickle file
        return

    #Getters
    def get_year(self):   												#get the current year
        
        
        return self.year 												#return the year

    def get_month(self):  												#get the current month
        
       
        return self.month  												#return the month

    def get_day_events(self, day_num): #retrieves events and presents that to the user in the ViewController. returns none if no events matched.
        s = shelve.open("data", writeback = True)  						#open pickle file
        event_list = []  												#set up a new list called event_list
        for event in s['events']:
            '''
            print('Title: ' + event.title)
            print('Event  Input')
            print(str(event.start.day) +'      '+ str(day_num))
            print(str(event.start.month) +'      '+ str(self.month))
            print(str(event.start.year) +'      '+ str(self.year))
            '''
            if event.start.year == self.year and event.start.month == self.month and event.start.day == int(day_num):   #check if an event matches
            																											# the year, month, and day
                event_list.append(event) 																				#if it does, add it to event_list
        	
        if not event_list:  										    #return none if nothing is in the event list
            return None
            
        #date_time = event_list[0].start.strftime('%a %b %d %Y %H:%M:%S')
        #print(date_time)
        
        return event_list  												#return the event list if something is in it.
        
    #Helpers
    def search_event(self, title, start, end): 							#Search for an event and return it's index or None
       
        s = shelve.open("data", writeback = True)  						#open pickle file
        index = -1 														#set index to be -1
        for index, event in enumerate(s['events']):
            if event.title == title and event.start == start and event.end == end:       #search for event based on title, start, and end
                s.close()												#if an event is found, close the pickle
                return index   											#return the index
        s.close() 														#if an event is not found, close the pickle
        return None 													#return None


    def delete_event(self, title, start, end): 							#deletes an event at specified date (month, day)

        return
