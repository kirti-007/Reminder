from plyer import notification
import time
t_h = float(input("Set the time(in hours): "))
while True:
    time.sleep(3600*t_h)
    notification.notify(
        title = 'Reminder',
        message = 'Hey, Drink water',
        app_icon = "notify.ico",
        timeout = 2,
    )