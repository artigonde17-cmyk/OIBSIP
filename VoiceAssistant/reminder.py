import time
import pyttsx3

engine = pyttsx3.init()


def set_reminder(seconds, message):

    time.sleep(seconds)

    print("Reminder:", message)

    engine.say(message)
    engine.runAndWait()