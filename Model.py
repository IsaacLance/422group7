#Chandler Potter 1/21/19 CIS 422
#Luyao Wang 1/28/2019
#

import shelve
from Event import CalendarEvent

class CalendarModel:         										#CalendarModel class
    """
    This is a class that will handle our CalendarModel.
    """
    def __init__(self, month, year):     								#init
        """
        args: month, year
        returns: N/A
        side effects: sets up month and year and calls startup_data()
        description: The __init__ function sets up the month and the
        year and calls startup_data() to get everything ready to go.
        """
        self.month = month  										#assign the month
        self.year = year                								#assign the year
        self.startup_data()             								#call startup data to get set up
        return

    #INIT/EXIT HELPERS
    def startup_data(self):           									#startup_data function

        """
        args: N/A
        returns: N/A
        side effects: creates and/or modifys s with key 'events'
        description: This functions sets up the pickle file to hold a 'events' key
        that will store events that are added by the user
        """
        print("Model startup")            								#print to terminal confirming Model startup
        print("Year: " +str(self.year))   								#print the year the calendar is set to
        print("Month: " +str(self.month)) 								#print the month the calendar is set to
        s = shelve.open("data", writeback = True)  						        #open the pickled file

        if not('events' in s):   									#if there is no events key in "s", create one
            print("No events key found in shelve. Created new events list.")                            #print that a new "events" key was created to store events to
            s['events'] = []  										#create events key
        else:
            print(s['events'])  									#prints saved events
        s.close()   											#close pickled file
        return

    def exit_data(self):   										#exit_data function
        """
        args: N/A
        returns: N/A
        side effets: prints "Model exit" and closes the pickle
        description: this file was used when exiting the program.
        It would print "Model exit" and close down the pickle file.
        """
        print("Model exit") 										#prints that model is exiting
        s.close()           										#close picked file
        return

    #Button responses/ setters
    def next_month(self):    										#moves to next month
        """
        args: N/A
        returns: N/A
        side effects: modifies month and/or year
        description: advances the month by 1 and will wrap back
        around to month 1 if the month is 13. If this happens,
        the year will advance as well.
        """
        self.month += 1      										#advance month by 1
        if self.month == 13:  										#if the month is 13, the next 3 lines will advance the year and then reset month to be 1
            self.year += 1
            self.month = 1
        return

    def prev_month(self):  										#moves to the previous month
        """
        args: N/A
        return: N/A
        side effects: modifies month and/or year
        description: This will go to th previous month. If the
        month becomes 0, it will reset it to be 12 and it will
        set the year to be the previous year.
        """
        self.month -= 1		 									#move the month back by 1
        if self.month == 0:  										#if the month is 0, the next 3 lines will change the year to the prevous year and then reset the month to be 12
            self.year -= 1
            self.month = 12
        return

    def add_event(self, title, start, end): 							        #adds event at specified date (month, day)
        """
        args: title, start, end
        returns: N/A
        side effects: adds an event to the "events" key
        description: This function will take a title,
        a start time, and an end time and save it as
        an event in the "events" key.
        """
        												#Events should only be added if they are not duplicates
        s = shelve.open("data", writeback = True)  						        #open pickle file
        print("Adding event:")  									#print out "Adding event:" and print current events
        print(s['events'])
        e = CalendarEvent(title, start, end) 							        #get event set up to be added
        print(e.title)      										#print title of event
        s['events'].append(e) 										#append event to s with events key
        print(s['events']) 										#print new current events
        s.close()  											#close pickle file
        return

    #Getters
    def get_year(self):   										#get the current year
        """
        args: N/A
        returns: self.year
        side effects: N/A
        description: This function is a getter
        that will return self.y
        """


        return self.year 										#return the year

    def get_month(self):  										#get the current month
        """
        args: N/A
        returns: self.month
        side effects: N/A
        description: This function is a getter
        that will return self.month.
        """


        return self.month  										#return the month

    def get_day_events(self, day_num): #retrieves events and presents that to the user in the ViewController. returns none if no events matched.
        """
        args: day_num
        returns: None or a list of events on a current day, month, year
        side effects: N/A
        description: This function checks to see if there is an event on a given day_num.
        It does this by checking for the year, month, and day of the event and matches it to
        the current day, month, and year. If it finds and event, it will return it. Otherwise,
        it will return None.
        """
        s = shelve.open("data", writeback = True)  						        #open pickle file
        event_list = []  										#set up a new list called event_list
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

        if not event_list:  										 #return none if nothing is in the event list
            return None

        #date_time = event_list[0].start.strftime('%a %b %d %Y %H:%M:%S')
        #print(date_time)

        return event_list  										 #return the event list if something is in it.

    #Helpers
    def search_event(self, title, start, end): 							         #Search for an event and return it's index or None
        """
        args: title, start, end
        return: None or the index of an event
        side effects: N/A
        description: This function will search for an event given the title, start, and end.
        If it finds an event, it will return its index. If nothing is found, it will return None.
        """

        s = shelve.open("data", writeback = True)  						         #open pickle file
        index = -1 											 #set index to be -1
        for index, event in enumerate(s['events']):
            if event.title == title and event.start == start and event.end == end:                       #search for event based on title, start, and end
                s.close()										 #if an event is found, close the pickle
                return index   										 #return the index
        s.close() 											 #if an event is not found, close the pickle
        return None 											 #return None


    def delete_event(self, title, start, end): 							         #deletes an event at specified date (month, day)
        """
        args: title, start, end
        return: N/A
        side effects: This will remove an event from the events key
        description: This function should remove an event from
        the "events" key.
        """

        s = shelve.open("data", writeback = True)                                                        #open pickle file
        index_delete_event = self.search_event(title,start,end)                                          #gets index of event using seatch_event function
        del s['events'][index_delete_event]                                                              #delete the event
        return None

    def edit_existing_event(self,title, start, end, new_title=None, new_start=None, new_end=None):
        s = shelve.open("data", writeback = True)
        index_existing_event = self.search_event(title,start,end)                                        #search for edit event
        
        if not (new_title is None):                                                                      #change the title of edit event
            s['events'][index_existing_event].title = new_title
        
        if not (new_start is None):                                                                      #change the start time of edit event
            s['events'][index_existing_event].start = new_start
            
            
        if not (new_end is None):                                                                        #change the end time of edit event 
            s['events'][index_existing_event].end = new_end
        
        #return s['events'][index_existing_event]                                                        #return the index of changing event for testing
        return None
    
    def clear_all_events(self):
        """
        args:none
        returns: N/A
        side effects: clear all events
        description: This function should clear all events that been
        saved by user
        """
        s = shelve.open("data", writeback = True)
        s['events'].clear()
        return None

    def amount_of_saving_event(self):
        """
        args:none
        returns:integer
        side effects: return the length of saving Events
        description: This funciton should return the length of all saving events
        """
        s = shelve.open("data", writeback = True)
        return len(s['events'])
