'''
Event class to be used by the model for data storage
'''
class CalendarEvent():
    def __init__(self, title, start, end, recur = False):
        #String
        self.title = title
        #Datetime object
        self.start = start
        #Datetime object
        self.end = end
    def __eq__(self, other):
        return (self.start == other.start) and (self.end == other.end)
        
    def __lt__(self, other):
        return (self.start < other.start)
    
    def __gt__(self, other):
        return (self.start > other.start)
        