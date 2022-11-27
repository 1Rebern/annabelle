#модуля
#from goto_plus import *
#gotoconfig(__file__)
import os
import speech_recognition as sr
import time
from rapidfuzz import fuzz 
import pyttsx3
from gtts import gTTS
from playsound import playsound
#import datetime
import webbrowser
import pyautogui as pg


opts = {
    "alias": ('annabelle','anna','animal', 'annabel', 'edible', 'enable', 'anibal', 'hannibal'),
    "ex": ('exit','stop','clouth'),
    "tbr": ('tell','me','what','расскажи','покажи','сколько','say','for','когда','как','open','start','please','police','create','play'),
    "cmds": {
        "music": ('music'),
        "youtube": ('youtube','video'),
        "calc": ('calculator','cake'),
        "telega": ('telegram','telegram'),
        "task_manager": ('task', 'manager', 'desk', 'manager'),
        "his": ('history','history'),
        "lov": ('love', 'you'),
    }
}
#функції
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language= 'en-US').lower()
        print('[log] Detected: ' + voice)

        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            #роспознаємо і виконуємо команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

        elif voice.startswith(opts["ex"]):
            exit = voice

            for x in opts['ex']:
                exit = exit.replace(x, "").strip()

            for x in opts['tbr']:
                exit = exit.replace(x, "").strip()

            #роспознаємо і виконуємо команду
            exit = recognize_exit(exit)
            execute_exit(exit['cmd'])



    except sr.UnknownValueError:
            print("[log] Voice no detected!")
    except sr.RequestError as e:
        print("[log] Unknown error, see you internet")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC

def recognize_exit(exit):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(exit, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC

def execute_exit(exit):
    if exit == 'calc':
        os.system('taskkill /IM calculator.exe /F')
    else:
        print("Please repeat comand!")




def execute_cmd(cmd):
    if cmd == 'youtube':
        webbrowser.open('https://www.youtube.com/')

    elif cmd == 'music':
        webbrowser.open('https://www.youtube.com/watch?v=FEP60Kd6D9I&list=PLyIO4BvNN3nG6LgLt0hQHyfBBGRlWwRUP&index=1&ab_channel=MIXsnake',new=1)
        #speak("Pleasant listening")
        

    elif cmd == 'calc':
        os.system('C:/Windows/System32/calc.exe')
        #speak("I start the calculator")
        
    elif cmd == 'telega':
        os.system('C:/Users/SanSanych/AppData/Roaming/"Telegram Desktop"/Telegram.exe')

    elif cmd == 'task_manager':
        pg.hotkey("Ctrl", "Shift", "Esc")

    elif cmd == 'his':
        os.system('E:/"обща папка"/книги/history.pdf')
#місце проблеми:
    elif cmd == 'lov':
        pass
        #tts = gTTS('I love you to', lang='en')
        #tts.save('love.mp3')
        #playsound.playsound('love.mp3')

         
    else:
        print("Please repeat comand!")
#запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)
    
speak_engine = pyttsx3.init()
speak_engine.runAndWait()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', 'en')

for voice in voices:
    if voice.name == 'Slt':
        speak_engine.setProperty('voice', voice.id)

speak("Hi my lord")
speak("Annabelle listening")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)