
from time import time
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()
while True:
    toaster.show_toast("Drink Water",
                    "Neeram Prajwalitam",
                    duration=10) 
    time.sleep(15*60)