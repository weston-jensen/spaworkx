import requests
import json
import schedule
import time

def job():
    req = requests.get('http://www.hyrumdamcam.com/spaworx/ioFile.html')
    print (req.text)
    
schedule.every(10).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)