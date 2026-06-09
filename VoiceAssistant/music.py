import pywhatkit

def play_youtube_song(command, speak):
    # Remove trigger words
    song = command.lower()
    song = song.replace("play", "").replace("song", "").replace("music", "").strip()

    if song == "":
        speak("Please tell me the song name")
        return

    speak(f"Playing {song} on YouTube")

    # Opens YouTube and plays song
    pywhatkit.playonyt(song)