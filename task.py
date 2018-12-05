import schedule
import time
def job():
    print(time.time())

def jobMinute():
    print("It runs per minute")


schedule.every().seconds.do(job)
schedule.every().minutes.do(jobMinute)


while True:
	schedule.run_pending()
	time.sleep(1)
