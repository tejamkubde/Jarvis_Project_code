import queue
import pyttsx3

import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[1].id)

def speak(audio):
    print("     ")
    Assistant.say(audio)

    print(f":{audio}")
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
                

def TaskExe():

    while True:
        query=takecommand()
        if "hello" in query:
            speak("hello sir i am jarvis")
            speak("your personal assistant")
            speak("How may i help you?")

        elif "how are you" in query:
            speak("I am fine sir")
            speak("what about you")

        elif "you need a break" in query:
            speak("ok sir")
            speak("you can call me anytime")
            break

        elif "bye" in query:
            speak("bye sir")
            speak("have a good day")

        


TaskExe()
