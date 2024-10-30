import datetime
import sys

import pyautogui
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Speech to Text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")

    except Exception as e:
        speak("Say that again please......")
        return "none"
    return query


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak("Good Morning!!!")
    elif 12 < hour < 18:
        speak("Good Afternoon!!!")
    else:
        speak("Good evening!!!")

    speak("I am Comrade. please tell me how can i help you......")


def start():
    wish()
    # logic building for tasks
    while True:
        query = takeCommand().lower()

        if 'volume up' in query:
            pyautogui.press("volumeup")


        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press("volumemute")

        elif 'goodbye' in query:
            speak("Thank you sir for using me and have a good day!!!!")
            sys.exit()
        # speak("sir, do you have any other work......")


if __name__ == "__main__":
    start()
