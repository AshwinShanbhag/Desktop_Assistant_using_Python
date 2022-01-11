# Desktop_Assistant_using_Python
In this Project , A Desktop assistant is designed using python and is customize for personal use 
#	What is a Desktop Assistant?
A Desktop Assistant helps with time and daily management of meetings correspondence and note taking. The role of personal assistant can be varied such as taking notes, opening apps , browsing etc. Upon a user's choice, it would share jokes and facts, manage downloads, sing songs, and talk, among other functions.

#	Working:
In this Project , A Desktop assistant is designed using python and is customize for personal use. For the assistant to speak “Microsoft Speech API”  is used. After taking input from the user, the audio input is converted from “Speech-to-Text” using “Google Speech Recognition API” and basic commands are executed using different python functions and programs.

#	Packages Required to be installed:
## 1.Pyttsx3: 
pyttsx3 is a text-to-speech conversion library in Python. An application invokes the pyttsx3.init() factory function to get a reference ta pyttsx3. Engine instance. it is a very easy to use tool which converts the entered text into speech.
The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.
It supports three TTS engines :
•sapi5 – SAPI5 on Windows
•nsss – NSSpeechSynthesizer on Mac OS X
•espeak – eSpeak on every other platform

Installation: To install the pyttsx3 module, first, you have to open the terminal and write:

    pip install pyttsx3


## 2.Speech Recognition:
Speech Recognition is a library for performing speech recognition, with support for several engines and APIs, online and offline.From theselibraries, we will be working with SpeechRecognition library because of it’s low barrier to entry and it’s compatibility with much availablespeech recognition APIs. 
Installation:
We can install SpeechRecogntion library by running the following line in our terminal window:

    pip install SpeechRecognition

Note : For the speechrecognition to work pyaudio is to be installed


## 3.Pyaudio:
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play andrecord audio on a variety of platforms.

Installation:
We can install PyAudio library by running the following line in our terminal window:

    pip  install pyaudio 

or 

    pip install pipwin
    pipwin install pyaudio


## 4.Wikipedia:
Wikipedia is a multilingual online encyclopedia created and maintained as an open collaboration project by a community of volunteer editorsusing a wiki-based editing system.

Installation:
In order to extract data from Wikipedia, we must first install the Python Wikipedia library, which wraps the official Wikipedia API. This canbe done by entering the command below in your command prompt or terminal:
    
    pip install wikipedia


#   Packages Used in the program:
    1.Pyttsx3
    2.Speech Recognition
    3.Wikipedia
    4.Web browser
    5.Datetime
    6.OS
    7.Time