from datetime import datetime
from time import sleep

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
while True:
    if current_time != "12:00:00":
        print("Current Time =", current_time)
        sleep(60)
        
        
