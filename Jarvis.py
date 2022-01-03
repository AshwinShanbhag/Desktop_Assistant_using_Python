import pyttsx3


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
if __name__ == '__main__':
    speak("hello Ashwin, How can I help you")
    
    
    