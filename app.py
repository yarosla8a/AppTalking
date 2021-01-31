import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    print(words)
    # os.system("say " + words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Hello, ask me something")

def command():
    r=sr.Recognizer()

    with sr.Microphone() as source :
        print("you can talk")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        zadanie= r.recognize_google(audio, language="ru-RU").lower()
        print("you say: "+ zadanie)
    except sr.UnknownValueError:
        talk("I don't understant")
        zadanie = command()
    return  zadanie

def makeSomething(zadanie):
    if 'open'.lower() in zadanie:
        talk("allrady doing")
        url='https://sweet.tv/ru/movie/'
        webbrowser.open(url)
    elif 'stop' in zadanie:
        talk("yes, ofcouse")
        sys.exit()

while True:
    makeSomething(command())





