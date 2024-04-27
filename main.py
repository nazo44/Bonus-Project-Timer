print("Set up a timer: ")
def timer(hour, minute, second):
  while hour >= 0 and minute >= 0 and second >= 0:
    print(f"{hour:02d}:{minute:02d}:{second:02d}")
    time.sleep(1)
    second = second - 1
    if second == -1:
      minute = minute - 1
      second = 59
    if minute == -1:
      hour = hour - 1
      minute = 59
  print("Time's up! ")
  again = input("Again? (Yes/No) ")
  if again.lower() == "yes":
    timer(int(input("Hours: ")), int(input("Minutes: ")), int(input("Second: ")))
  elif again.lower() == "no":
    print("Okay! ")
    exit()
import time

hour = int(input("Hour: "))
minute = int(input("Minute: "))
second = int(input("Second: "))
timer(hour, minute, second)
