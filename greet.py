import time , pyttsx3 as pyvoice
hour = int(time.strftime('%H'))
engine = pyvoice.init()

if hour >= 0 and hour < 12:
    timestamp = time.strftime('Its %H AM : %M Minutes : %S Seconds')
    if hour < 4:
       print("Good night sir:) ",timestamp)
       engine.say(f"Good night sir:) {timestamp} ")
    else:
        print("Good morning sir:) ",timestamp)
        engine.say(f"Good morning sir:) {timestamp} ")
elif hour >=12 and hour < 16:
    timestamp = time.strftime('Its %H PM : %M Minutes : %S Seconds')
    print('Good afternoon sir:) ',timestamp)
    engine.say(f"Good afternoon sir:) {timestamp} ")
elif hour >= 16 and hour < 20:
    timestamp = time.strftime('Its %H PM : %M Minutes : %S Seconds')
    print('Good evening sir:) ',timestamp)
    engine.say(f"Good evening sir:) {timestamp} ")
else :
    timestamp = time.strftime('Its %H PM : %M Minutes : %S Seconds')
    print('Good night sir:) ',timestamp)
    engine.say(f"Good night sir:) {timestamp} ")
engine.runAndWait()
