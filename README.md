# 422 - Calendar

Calendar is an personal calendar application. With it, you have a tool that can help organize your future plans, schedule meetings more efficiently and stay on top of tasks and reminders. 

![alt text](https://github.com/IsaacLance/422group7/blob/master/Calendar.png)


#### Calendar offers many features such as:
- Lightweight and easy to setup
- Add, delete and edit event
- Can run other database files generated by other users of the Calendar application
- Protected from inputting invalid data into event field
- Opens to current day and month
- Runs under 500ms

## Installation

This application is runnable on MacOS and Windows. It is implemented in Python ver 3.6. You need Python and PyQt5 to launch this application.
We recommend using a 64-bit (x64) processor to run the application.
For those without python or pyqt5, they can be downloaded from these links.
Brew can be used to quickly install pyqt5.
https://www.python.org/

https://brew.sh/

https://pypi.org/project/PyQt5/

To install pyqt5 run this bash command:
```bash
$ brew install pyqt5
```
To run the application run this bash command:
```bash
$ python ViewController.py
```

## Usage
On the home page, there are three main choices: save event, change month, change year. 
Home page is shown below: 

![alt text](https://github.com/IsaacLance/422group7/blob/master/Calendar.png)

### To add an event:
On the home page, select button labeled Add Event

This will direct you to a saving page labeled Dialog

Enter the title, MM/DD/YY, HH:MM for the save events 

Select Save button for save events

Check the event has been saved or not, click the close button(red) on the top left page of Dialog, then click the day that

have been saved. For more details, see the Reviewing Events

![alt text](https://github.com/IsaacLance/422group7/blob/master/Add_date_popup.png)

### To view events on a given day:
On the home page, click the day that you want to edit which can be navigated by using "Previous" and "Next" as well as "+" and "-" to change the year.
Choose the day by click the day button
Pop up a window labeled “Dialog”, it shows all events for that day

![alt text](https://github.com/IsaacLance/422group7/blob/master/events.png)

To close the widget, simply close the window

## Running the tests
We have provided two tests to test the functionality of the calendar application.
To run, open the file with python using the following bash command:
```bash
$ python test_Model.py
```
test_model.py tests if a event shows up if the database is cleared, and then added. 
It asserts if the number of entries added is the correct number.
If it is incorrect it will show an error in the terminal. For details:https://docs.google.com/document/d/1Y512gUP_uNcVmjh-EibinXldxwDEUoGd5NDIIyF9q70/edit?usp=sharing



The second test, 
```bash
$ python test_model2.py
```
test_model2.py puts the application under more rigorous tests. 
Testing the order and type of arguments given to the application.

## Contributing
Pull requests are welcome after April 1st, 2019. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Authors
- Isaac Lance
- Jake Beder
- Kellie Hawks
- LuYao Wang
- Chandler Potter

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Support
For any support issues please email khawks996@gmail.com
