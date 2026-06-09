import speech_recognition as sr
import pyttsx3
from commands import execute_command

# Initialize text-to-speech engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

# Create recognizer once (faster performance)
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", command)
        return command.lower()

    except Exception:
        speak("Sorry, I did not understand.")
        return ""


speak("Hello, I am your Voice Assistant")

while True:
    command = take_command()

    if command:
        stop = execute_command(command, speak)

        if stop:
            break