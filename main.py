import speech_recognition as sr
from  time import ctime
import webbrowser
import time
import playsound
import os
import datetime
import random
from gtts import *
from googletrans import Translator
import subprocess
import pywhatkit

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source=source,timeout=5 ,phrase_time_limit=5)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('Sorry,I dont get that')
        except sr.RequestError:
            alexis_speak('Sorry , my speech service is down')
        return voice_data.lower()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name])

def alexis_speak(audio_string):

    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respondme(voice_data):
    if 'What is yor name' in voice_data:
       alexis_speak('My name is alexis')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search for' in voice_data:
        search = record_audio('What do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp:'
        webbrowser.get().open(url)
        alexis_speak('here is the location for ' +  location )
    if 'play' in voice_data:
        music = record_audio('What music you want to listen ')
        pywhatkit.playonyt(music)
        alexis_speak("here your music " + music)
    if 'make a note' in voice_data:
        alexis_speak("what would you like to write down")
        note_text = record_audio()
        note(note_text)
        alexis_speak("I made a note for that")
    if 'quit' in voice_data:
        exit()

wake = "hey alexa"
while True:
    voice_data = record_audio()
    if voice_data.count(wake) > 0 :
        alexis_speak('hello my name is tim Your A.I.how can I help you')
        voice_data = record_audio()
        respondme(voice_data)