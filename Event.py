'''
Event class to be used by the model for data storage
'''
class Event():
    def __init__(self, title, start, end, recur = False):
        self.title = title
        self.start = start
        self.end = end