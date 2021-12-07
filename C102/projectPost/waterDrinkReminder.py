import time
from win10toast import ToastNotifier
import datetime


def getTimeInput():
	hour = int(input("hours of interval :"))
	minutes = int(input("Mins of interval :"))
	seconds = int(input("Secs of interval :"))
	time_interval = seconds+(minutes*60)+(hour*3600)
	return time_interval


def log():
	now = datetime.datetime.now()
	start_time = now.strftime("%H:%M:%S")
	with open("log.txt", 'w') as f:
		f.write(f"You drank water {now} \n")
        print(f"You drank water at {now} \n")

def logFalse():
    	now = datetime.datetime.now()
	start_time = now.strftime("%H:%M:%S")
	with open("log.txt", 'w') as b:
         b.write(b"You did not drank water {now} \n")
         print(b"You drank water at {now} \n")
    

def askIfDrinked():
    askedIFdrinkTaken = input("Did you drink the water(Y/N)")
    if(askedIFdrinkTaken,'==',"Y"):
        log()
    elif(askedIFdrinkTaken,'==',"N"):
        logFalse()
    else:
        print("Please write a valid input next time write now in log it has been mentioned as water not drinked")

def notify():
	notification = ToastNotifier()
	notification.show_toast("Time to drink water")
	askIfDrinked()
	return 0


def starttime(time_interval):
	while True:
		time.sleep(time_interval)
		notify()


if __name__ == '__main__':
	time_interval = getTimeInput()
	starttime(time_interval)
