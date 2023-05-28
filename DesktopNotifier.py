# Task 1: Desktop Notifier in Python

import time
from winotify import Notification, audio

toast = Notification(app_id="Project",
                     title="Rest",
                     msg="Your Time is Over",
                     duration = "long",
                     icon = "F:/IT IT/Z _MY_PROJECTS/Desktop Notifier/notification.png")

toast.set_audio(audio.LoopingAlarm, loop=True)

toast.show()

