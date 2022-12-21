import speech_recognition as sr 
import webbrowser
import time
import playsound
import os 
import random
import datetime 
from time import ctime
from gtts import gTTS           #google text to speech 
import pyttsx3 as p 
# import PyPDF2
from News import *

engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


r = sr.Recognizer()

def record_audio(ask= False):
    with sr.Microphone() as source:
        
        if ask:
            Mo_speak(ask)
        print("listning...")
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Mo_speak("sorry, I didn't get that")
        except sr.RequestError:
            Mo_speak("sorry my speech service is down")
        return voice_data

def Mo_speak(text):
    engine.say(text)
    engine.runAndWait()
   
def Date():
    tim=int(datetime.datetime.now().hour)
    if tim>=0 and tim<12:
        Mo_speak('Good Morining sir')
    else:
        Mo_speak('Good Evening sir')

Date()

def respond(voice_data):
     
    if 'name' in  voice_data: 
        Mo_speak('My Name is Mo')
        print('My Name is Mo')

    if 'time ' in voice_data :
        Mo_speak(ctime())
        print(ctime())

    if 'search' and 'information' in voice_data:
        search = record_audio('What do you want to search for')   
        url = 'https://google.com/search?q=' + search 
        webbrowser.get().open(url)
        Mo_speak('here is what i found for'  + search)
        print('here is what i found for' + " "+ search)
   
    if 'play' and 'video' in voice_data:
        search1 = record_audio('What do you want to search in youtube')   
        url = 'https://www.youtube.com/results?search_query=' + search1 
        webbrowser.get().open(url)
        Mo_speak('here is'  + search1)
        print('here is' +" " + search1)

    if 'get'and'location' in voice_data:
        location = record_audio('What is location')   
        url = 'https://google.nl/maps/place/' + location + '/&amp;' 
        webbrowser.get().open(url)
        Mo_speak('here is location of '+ location)
        print('here is location of '+" "+ location)

    
    if 'open'and'news' in voice_data:
        arr=news()
        Mo_speak("Sure sir , Now I will read news for you")
        for i in range(3):
            Mo_speak(arr[i])
            print(arr[i])

    if 'open download' in voice_data:
        Mo_speak("opeing your download folder")
        os.startfile("C:/Users/Public/Downloads")
        Mo_speak("the download folder is open") 
        print("the download folder is open")

    if 'go' in voice_data:
        Mo_speak('thank you sir')
        exit()   
    

time.sleep(1)
Mo_speak('How can I help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)
