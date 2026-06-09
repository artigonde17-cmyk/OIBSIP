import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import re


def play_youtube_song(command, speak):
    # Clean command
    song = re.sub(r"play|music|song", "", command.lower()).strip()

    if song == "":
        speak("Which song should I play?")
        return

    speak(f"Playing {song} on YouTube")
    pywhatkit.playonyt(song)


def execute_command(command, speak):

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "wikipedia" in command:
        speak("Searching Wikipedia")

        topic = command.replace("wikipedia", "")

        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)

        except:
            speak("No result found")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open chat gpt" in command:
        webbrowser.open("https://chat.openai.com")
        speak("Opening Chat GPT")

    # ✅ NEW: YouTube music
    elif "play" in command:
        play_youtube_song(command, speak)

    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        return True

    else:
        speak("Command not recognized")

    return False