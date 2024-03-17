import time
checkingampm = int(time.strftime("%H"))
if(checkingampm > 11):
    timestamp = time.strftime("It's %H PM : %M Minutes : %S Seconds")
    if(checkingampm <=19):
       print("Good Afternoon :)")
    else:
      print("Good Night :)")
else:
  timestamp = time.strftime("It's %H AM : %M Minutes : %S Seconds")
  if(checkingampm <=3):
    print("Good night :)")
  else:
    print("Good morning:) ")
print(timestamp)
