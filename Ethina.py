import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import time




engine = pyttsx3.init('sapi5')    #Sapi5 is a Microsoft speak API to take voice
voices= engine.getProperty('voices')
#print(voices[2].id)   to print whose voice it is
engine.setProperty('voice',voices[1].id)


#function for the Assistant to speak
def speak(audio):
    engine.say(audio)  #the engine will speak
    engine.runAndWait() #if this is not written the audio will not be audible
    

# Function to wish the user
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak ("Good Morning Sir")

    elif hour>= 12 and hour <6:
        speak("Good Afternoon Sir")
    
    else:
        speak("Good Evening Sir")

    speak("I am Ethina, How can I help you")


# function to take command from the user 
'''It take the microphone input from the user and returns string as output'''
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1.5
        r.energy_threshold=300
        audio= r.listen(source)
    
    try:
        print("Recognizing.....")
        word = r.recognize_google(audio , language='en-in')
        print("User said:"+ word)

    except:
        print("Not able to hear you sir, Can you please repeat?")
        time.sleep(3) #to wait for 3 secs 
        return "None"
    
    return word

#function to search words in wikipedia
def open_wikipedia(word):
    speak("Searching " + word + "in wikipedia .....")
    print("Searching  Wikipedia.....please wait")
    word=word.replace("wikipedia","")
    results= wikipedia.summary(word,sentences=2)
    print(results)
    speak("Acccording to Wikipedia")
    speak(results)
        
    
#function to open youtube
def open_youtube(word):
    webbrowser.open("https://www.youtube.com")
    speak("Opening youtube Sir.....")


#function to open google
def open_google(word):
    webbrowser.open("https://www.google.com")
    time.sleep(2)
    speak("Opening Google.......")
    speak("What would you like to search sir....")
    new_word= takeCommand()
    try:
        open_search(new_word)
    except:
        speak("Sorry sir!! not able to search")


#function to open music
def play_music(word):
    music_dir='C:\\Users\\ashsh\\AppData\\Roaming\\Spotify\\Spotify.exe'
    os.startfile(music_dir)   
    speak("Opening Spotify.....") 


#function to search in google
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
        speak("Sir! would you like me to tell its meaning")
        command= takeCommand()
        time.sleep(3) #will let the user to think yes or no 
        if 'yes'in command:
            open_wikipedia(word)
            return "None"
        else:
            speak("Ok Sir!!")
            return "None"

            
    except:
        speak("No able to find it in wikipedia...")

        
#function if unable to process the task
def cant_process(word):
    if not'sorry' in word:
        whats_next()
    else:
        speak("Sorry!! Unable to process this task Sir....")
        whats_next()

#function to ask user what to do next
def whats_next():
    speak("what would you like me to do next?")
    

# main
if __name__ == '__main__':
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
            speak("Good bye Sir, Have a good day")
            break
        

        elif 'thank you'in word or 'thankyou' in word:
            speak("You are Welcome....... ,Have a good day sir")
            break

        
                

        
        
             
        
