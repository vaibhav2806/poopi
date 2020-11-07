import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

# We are using sapi5 to take the inbuilt voice.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')     # Getting details of current voice
engine.setProperty('voice', voices[1].id)
# We have set voice of our assistant above genrally we have 2 built in voices, open readme.


# Defining speak function
def speak(audio):
    '''
    Whatever we will write inside this speak() function it will be converted into speech.
    Without engine.runAndWait() command, speech will not be audible to us.
    '''
    engine.say(audio)
    engine.runAndWait() 


# Defining wish me function
def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("My name is poopi. How can i help you.")


def takeCommand():
    '''
    It takes microphone input from the user and returns string output.
    PAUSE_THRESHOLD is seconds of non-speaking audio before a phrase is considered complete.
    we will use recogninze_google to recognize the audio, we will put this in try block.
    an exception might occure so we will not ignore that so if an exception pccurs we will ask the user 
    to say it again.

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        print(e)
        print("Say that again please.")
        return None
    return query
         


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing task
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia' , "")
            results = wikipedia.summary(query,sentences = 3)
            speak("According to wikipedia...")
            print(results)
            speak(results)
            '''
            query = query.replace('wikipedia' , "") esme check kiya ki query me wikipedia hai ki ni agr 
            hai toa hata denge usse vaha se, hatane ke baad search karke results me store karenge
            [results = wikipedia.summary(query,sentences = 3)]......explanation of above 2 statements.
            '''
        elif 'youtube' in query:
            speak(f"Opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'google' in query:
            speak(f"Opening google")
            webbrowser.open("https://www.google.co.in/")

        elif 'facebook' in query:
            speak(f"Opening facebook")
            webbrowser.open("https://www.facebook.com/")

        elif 'github' in query:
            speak(f"Opening github")
            webbrowser.open('https://github.com/')        

        elif 'music' in query:
            speak(f"Playing music")
            music_dir = 'C:\\Users\\Vaibhav\\Music\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
            # song and music_dir ko join kara deya hai es leye ki randomly song uthaye and path follow karke 
            # play kar de.

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"It is {strTime}")

        elif 'code' in query:
            speak(f"Opening VS code")
            codePath = 'C:\\Users\\Vaibhav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'quite' in query or 'thank you' in query:
            speak("Your welcome")
            exit()
        else:
            pass
