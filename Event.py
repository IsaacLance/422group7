'''
Event class to be used by the model for data storage
'''
class Event():
    def __init__(self, title, start, end, recur = False):
        #String
        self.title = title
        #Datetime object
        self.start = start
        #Datetime object
        self.end = end