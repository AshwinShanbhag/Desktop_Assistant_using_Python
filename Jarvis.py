import pyttsx3
import speech_recognition as sr
import wikipedia

import datetime





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
    if hour> 0 and hour<12:
        speak ("Good Morning Sir")

    elif hour>= 12 and hour <6:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Ethina, How can I help you")

'''It take the microphone input from the user and returns string as output'''
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1.2
        r.energy_threshold=250
        audio= r.listen(source)
    
    try:
        print("Recognizing.....")
        word = r.recognize_google(audio , language='en-in')
        print("User said:"+ word)

    except:
        print("Speak that again please")
        return "None"
    
    return word







if __name__ == '__main__':
    wishme()
    #Logic to excecute task based work
    while True:
        word =takeCommand().lower()
        
        if 'wikipedia' in word:
            speak("Searching" + word+ " .....")
            print("Searching  Wikipedia.....please wait")
            word=word.replace("wikipedia","")
            results= wikipedia.summary(word,sentences=2)
            print(results)
            speak("Acccording to Wikipedia")
            speak(results)

        if 'goodbye'in word:
            speak("Good bye Sir, Have a good day")
            break
        
        

