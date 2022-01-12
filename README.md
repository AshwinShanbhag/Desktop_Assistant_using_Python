#  <div align='center'>Desktop Assistant Using Python</div>

&nbsp;
#	What is a Desktop Assistant?
A Desktop Assistant helps with time and daily management of meetings correspondence and note taking. The role of personal assistant can be varied such as taking notes, opening apps , browsing etc. Upon a user's choice, it would share jokes and facts, manage downloads, sing songs, and talk, among other functions.

&nbsp;
#	Working:
**In this Project,** A Desktop assistant is designed using python and is customize for personal use. For the assistant to speak “Microsoft Speech API”  is used. After taking input from the user, the audio input is converted from “Speech-to-Text” using “Google Speech Recognition API” and basic commands are executed using different python functions and programs.

&nbsp;
#   Packages Used in the program:
   1. Pyttsx3
   2. Speech Recognition
   3. Wikipedia
   4. Web browser
   5. Datetime
   6. OS
   7. Time

&nbsp;
&nbsp;
#	Packages Required to be installed:
## 1. Pyttsx3: 
pyttsx3 is a text-to-speech conversion library in Python. An application invokes the pyttsx3.init() factory function to get a reference ta pyttsx3. Engine instance is a very easy to use tool which converts the entered text into speech.The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.  
It supports three TTS engines :
   - sapi5 – SAPI5 on Windows
   - nsss – NSSpeechSynthesizer on Mac OS X
   - espeak – eSpeak on every other platform

### Installation: 
To install the pyttsx3 module, first, you have to open the terminal and write:

    pip install pyttsx3

### For more information : 
    https://pypi.org/project/pyttsx3

## 2. Speech Recognition:
Speech Recognition is a library for performing speech recognition, with support for several engines and APIs, online and offline.From theselibraries, we will be working with SpeechRecognition library because of it’s low barrier to entry and it’s compatibility with much availablespeech recognition APIs. 

### Installation:
We can install SpeechRecogntion library by running the following line in our terminal window:

    pip install SpeechRecognition

Note : For the speechrecognition to work pyaudio is to be installed

### For more information : 
    https://pypi.org/project/SpeechRecognition/

## 3. Pyaudio:
PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play andrecord audio on a variety of platforms.

### Installation:
We can install PyAudio library by running the following line in our terminal window:

    pip  install pyaudio 

or 

    pip install pipwin
    pipwin install pyaudio

### For more information : 
    https://pypi.org/project/PyAudio/

## 4. Wikipedia:
Wikipedia is a multilingual online encyclopedia created and maintained as an open collaboration project by a community of volunteer editorsusing a wiki-based editing system.

### Installation:
In order to extract data from Wikipedia, we must first install the Python Wikipedia library, which wraps the official Wikipedia API. This can be done by entering the command below in your command prompt or terminal:
    
    pip install wikipedia

### For more information : 
    https://pypi.org/project/wikipedia/

&nbsp;
&nbsp;

# PROGRAM
```python
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import time



engine = pyttsx3.init('sapi5')    #Sapi5 is a Microsoft speak API to speak voice
voices= engine.getProperty('voices')
#print(voices[2].id)   to print whose voice it is
engine.setProperty('voice',voices[1].id)


# function for the Assistant to speak
def speak(audio):
    engine.say(audio)  #the engine will speak
    engine.runAndWait() #if this is not written the audio will not be audible

# addressing the user 
def open_address(addre): 
    if 'sir'in addre:
        return 'sir'
    elif 'madam' in addre:
        return 'madam'   

# Function to wish the user
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak ("Good Morning "+ address ) 

    elif hour>= 12 and hour <18:
        speak("Good Afternoon "+ address )
    
    else:
        speak("Good Evening "+ address)

    speak("How can I help you")

# function to take command from the user 
'''It take the microphone input from the user and returns string as output'''
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1.3
        r.energy_threshold=300
        audio= r.listen(source)
    
    try:
        print("Recognizing.....")
        word = r.recognize_google(audio , language='en-in').lower()
        print("User said:"+ word)

    except:
        print("Not able to hear you, Can you please repeat?")
        time.sleep(2) #to wait for 3 secs 
        return "None"
    
    return word

# function to search words in wikipedia
def open_wikipedia(word):
    speak("Searching " + word + " in wikipedia .....")
    print("Searching  Wikipedia.....please wait")
    word=word.replace("wikipedia","")
    results= wikipedia.summary(word,sentences=2)
    print(results)
    speak("Acccording to Wikipedia")
    speak(results)
        
    
# function to open youtube
def open_youtube(word):
    webbrowser.open("https://www.youtube.com")
    speak("Opening youtube "+ address +"...")


# function to open google
def open_google(word):
    webbrowser.open("https://www.google.com")
    time.sleep(2)
    speak("Opening Google.......")
    speak("What would you like to search "+ address +"....")
    new_word= takeCommand()
    try:
        if new_word=="None":
            speak("Sorry "+address+ "!! not able to search")
        
    except:
        open_search(new_word)


# function to open music
def play_music(word):
    music_dir='C:\\Users\\ashsh\\AppData\\Roaming\\Spotify\\Spotify.exe'
    os.startfile(music_dir)   
    speak("Opening Spotify.....") 


# function to search in google
def open_search(word):
    if 'search' in word:
        word= word.replace('search',"")
    else:
        word=word.replace('define',"")
    if word == "":
        return "sorry"
    speak("Searching " + word + " .....")
    results= webbrowser.open("https://www.google.com/search?q=meaning+of "+ word )
    try:
        speak(""+address +"!!! would you like me to tell its meaning")
        command= takeCommand()
        time.sleep(3) #will let the user to think yes or no 
        if 'yes'in command:
            open_wikipedia(word)
            return "None"
        else:
            speak("Ok "+address)
            return "None"

            
    except:
        speak("Sorry "+ address +", I am unable to find its meaning in wikipedia...")
        return "None"

        
# function if unable to process the task
def cant_process(word):
    if not'sorry' in word:
        whats_next()
    else:
        speak("Sorry!! Unable to process this task " + address +"..")
        whats_next()

# function to ask user what to do next
def whats_next():
    time.sleep(2)
    speak("what would you like me to do next?")
    

#  main
if __name__ == '__main__':
    speak("Welcome to Desktop Assistant...")
    speak("I am Ethina")
    print("How would you like me to address you? By Sir.... or By Madam...")
    speak("How would you like me to address you? By Sir.... or By Madam...")
    addre=takeCommand().lower()
    if 'sir' in addre or 'madam' in addre:
        address=open_address(addre)
    else:
        address='sir'
    
    wishme()
    #Logic to excecute task based work
    while True:
        word =takeCommand().lower()
        
        if 'wikipedia' in word:
            open_wikipedia(word)
            whats_next()

        
        elif 'open youtube' in word:
            open_youtube(word)
            whats_next()

        
        elif 'open google' in word:
            open_google(word)
            whats_next()

            
        elif 'play music' in word or 'open spotify' in word:
            play_music(word)
            whats_next()      


        elif 'search' in word or 'define' in word:
            word=open_search(word)
            cant_process(word)
            

        elif 'goodbye' in word or 'good bye' in word: 
            speak("Good bye "+address+"!!, Have a good day")
            break
        

        elif 'thank you'in word or 'thankyou' in word:
            speak("You are Welcome....... ,Have a good day "+ address +"")
            break

        elif word=='open':
            speak("Sorry "+ address +", Can you please specify the command ")        

```