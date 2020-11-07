What is pyttsx3?
 A python library which will help us to convert text to speech. In short, it is a text-to-speech library.
 It works offline, and it is compatible with Python 2 as well the Python 3.

What is sapi5?
 Speech API developed by Microsoft.
 Helps in synthesis and recognition of voice.

What Is VoiceId?
 Voice id helps us to select different voices.
 voice[0].id = Male voice 
 voice[1].id = Female voice 

speech_recognition:
 The speech recognition is one of the most useful features in several applications like home automation, AI etc. 

import pyttsx3                  : a text-to-speech library.
import datetime                 : so that POOPI can greet everyone and tell us live time.
import speech_recognition as sr : used in takeCommand() method.
import wikipedia                : so that POOPI can give us a summary of wikipedia
import webbrowser               : to open all the web poratls which are asked 
import os                       : to acess files,folders,applications,etc.
import random                   : used to randomly play any song

First of all, we have created a wishme() function that gives the functionality of greeting according to the system time to POOPI.
After wishme() function, we have created a takeCommand() function, which helps our POOPI to take command from the user. 
This function is also responsible for returning the user's query in a string format.
We developed the code logic for opening different websites like google, youtube, and github.
Developed code logic for opening VS Code or any other application.