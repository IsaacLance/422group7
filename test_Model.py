#Luyao Wang
#Note tests for Model

from Model import CalendarModel
import ViewController
from Event import CalendarEvent
import datetime
#Test_Case for Model.py
#first test add_event

def test_add_event():
    """
    Test the Model 'add_event' method
    """

    title = "test"
    c = CalendarModel(1,2019)
    c.clear_all_events()
    assert(c.amount_of_saving_event() == 0)

    start = datetime.datetime(2019,9,12,0,0)
    end = datetime.datetime(2019,10,12,0,0)
    c.add_event(title, start, end)
    assert(c.amount_of_saving_event() == 1)

    return None

def test_delete_event():
    """
    Tests the Model 'delete_event' method
    """
    title = 'test'
    c = CalendarModel(1,2019)
    start = datetime.datetime(2019,9,12,0,0)
    end = datetime.datetime(2019,10,12,0,0)
    c.delete_event(title, start, end)
    assert(c.amount_of_saving_event() == 0)

    return None

def test_get_day_events():
    """
    Tests the Model 'get_day_events' method
    """
    print("get_day_events")
    c = CalendarModel(1,2019)
    print(c.get_day_events(12))

def test_edit_existing_event():
    """
    Tests the Model 'edit_existing_event' method
    """
    title = "test"
    c = CalendarModel(1,2019)
    start = datetime.datetime(2019,9,12,0,0)
    end = datetime.datetime(2019,10,12,0,0)
    new_start = datetime.datetime(2019,11,5,0,0)
    existing = c.edit_existing_event("test",start,end,None,new_start,None)
    print(existing.start.month)
    print(existing.start.day)
    return None


if __name__ == "__main__":
    print("test1:")
    test_add_event()
    
    print("test2:")
    test_get_day_events()
    
    print("test3:")
    #test_delete_event()
    
    print("test4")
    test_edit_existing_event()
