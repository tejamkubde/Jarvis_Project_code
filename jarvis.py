import queue
import pyttsx3

import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)

def speak(audio):
    print("     ")
    Assistant.say(audio)
    print("     ")
    Assistant.runAndWait()
    
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.............")
        command.pause_threshold = 1
        audio = command.listen(source)
       
        try:
            print("Recognizing............")
            query = command.recognize_google(audio,language='en-in')
            print(f'you said : {query}') 
            
        except Exception as Error:
            return "none"
        
        return query.lower()
                
speak('Hello sir')
# takecommand()

query = takecommand()

if 'hello' in query:
    speak("Good Morning Sir")

else:
    speak("Sorry, No command found") 