import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS

google_API_KEY ="AIzaSyCgadZYDrzkMg9b7LiV5IU8FaZXl-QyGT4"
os.environ["GOOGLE_API_KEY"] = google_API_KEY


def voice_input():
    """this functionwill recoganize voice & return text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        

        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
            
        except sr.UnknownValueError:
            print("Sorry,could not recognize voice")
        except sr.RequestError as e:
            print("Could not request results from google speech Recognition server; {0}",format(e))

def text_to_speech(text):
    #Create a gTTS object
    tts=gTTS( text=text, lang='en')
    #save the audio as MP3
    tts.save("speech.mp3")

def llm_model_object(user_text):
    genai.configure(api_key=google_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(user_text)

    result=response.text

    return result






