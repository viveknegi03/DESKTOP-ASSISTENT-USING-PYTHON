import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os

# taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)

# speak function
def speak(text):
    """this function converts text to speech

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()

# speak("hello my name is jarvis, good morning master!")


# speech recognition function
def takeCommand():
    """this functionwill recoganize voice & return text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {query}\n")


        except Exception as e:
            print("say that again plss")
            return "None"
        return query
    
text=takeCommand()
speak(text)