import pyttsx3
import time
import webbrowser
import wikipedia
import datetime

import pyaudio
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
import speech_recognition as sr
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Say something....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said {query}\n")
    except Exception as e:
        print(e)
        return("sorry i cant help u")
    return query
def wish():
    return("namaste i am mogambo i am here to help u ")
if __name__== "__main__":
    speak(wish())
    time.sleep(1)

    query = takecommand()
    query=query.lower()
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    if 'open youtube' in query:
        webbrowser.open_new('youtube.com')
    elif 'wikipedia' in query:
        speak("searching wikipedia...")
        query=query.replace("wikipedia"," ")
        results=wikipedia.summary(query,sentences=3)
        speak("according to wikipedia")
        speak(results)
    elif 'song' in query:

        webbrowser.get('chrome').open("https://www.youtube.com/watch?v=yUu26tcUri0&ab_channel=SonotekMusic")
    elif 'codechef' in query:
        webbrowser.open_new('https://www.codechef.com/')
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
