#This is the code for shutting down computer after a certain time passes. 

import time
import os

print("Running ;)")
current_time = time.ctime()
current_time = current_time.split(" ")
current_hour = current_time[3].split(":")
while current_hour[0] != "04":
    current_time = time.ctime()
    current_time = current_time.split(" ")
    current_hour = current_time[3].split(":")
os.system("shutdown /s /t 1")

