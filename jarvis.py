import queue
import pyttsx3
import webbrowser
import speech_recognition as sr
import pywhatkit

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[1].id)
Assistant.setProperty("rate",170)

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
            break

        elif "youtube search" in query:
            speak("Ok sir, This is what i found for your search!")
            query = query.replace("youtube search","")
            query = query.replace("jarvis","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("Done Sir")
            
        elif "google search" in query:
            speak("This is what i found for your search sir!")
            query = query.replace("google search","")
            query = query.replace("jarvis","")
            pywhatkit.search(query)
            speak("Done Sir!!")

        elif "website" in query:
            speak("Ok sir, Launching")
            query = query.replace("website","")
            query = query.replace("jarvis","")
            web1 = query.replace("open","")
            web2 = "https://www." + web1 + ".com"
            webbrowser.open(web2)
            speak("launched sir!")

        elif "launch" in query:
            speak("Tell me the name of the website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")
                


TaskExe()
