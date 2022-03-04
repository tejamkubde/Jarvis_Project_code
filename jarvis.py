import queue
import pyttsx3
import webbrowser
import speech_recognition as sr
import pywhatkit
import time
import flask
import os 
import wikipedia
import pyautogui
import keyboard
from PyDictionary import PyDictionary as diction




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

    def music():
        speak("Tell me the name of the song!")
        musicname = takecommand()
        pywhatkit.playonyt(musicname)
        speak("Your song has been started!, Enjoy sir")

    def whatsapp():
        speak("Tell me the name of the person")
        name = takecommand()


        if 'abc' in name:
            speak("Tell me the message")
            msg=takecommand()
            speak("tell me the time sir")
            speak("time in hour")
            hour=int(takecommand())
            speak("time in minutes")
            min=int(takecommand())
            pywhatkit.sendwhatmsg("+919307665461",msg,hour,min,20)
            speak("ok sir, sending whatsapp message")

        elif 'about' in name:
            speak("Tell me the message")
            msg=takecommand()
            speak("tell me the time sir")
            speak("time in hour")
            hour=int(takecommand())
            speak("time in minutes")
            min=int(takecommand())
            pywhatkit.sendwhatmsg("+919730863521",msg,hour,min,20)
            speak("ok sir, sending whatsapp message")
    
        else:
            speak("tell me the phone number")
            phone=int(takecommand())
            ph = "+91" + phone
            speak("Tell me the message")
            msg=takecommand()
            speak("tell me the time sir")
            speak("time in hour")
            hour=int(takecommand())
            speak("time in minutes")
            min=int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            speak("ok sir, sending whatsapp message")
    
    def ChromeAuto():
        speak('Chrome Automation Started!!')
        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

    def screenshot():
        speak("Ok sir! What should i name that file? ")
        path = takecommand()
        path1name  = path + ".png"
        path1 = "C:\\Users\\Ketan\\OneDrive\\Pictures\\Screenshots\\" +path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\Ketan\\OneDrive\\Pictures\\Screenshots")
        speak("Here is your screenshot")
 
    def Dict():
        speak('Dictionary Activated !!')
        speak('Tell me the Word Sir...!')
        prob1 = takecommand()

        if 'meaning' in prob1:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = diction.meaning(probl)
            speak(f'The Meaning For {probl} is {result}')
        
        else:
            speak("tejam")

    def openApps():
        speak("Ok sir, Wait a second!")

        if "code" in query:
            os.startfile("C:\\Users\\Ketan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "brave" in query:
            os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

        elif "whatsapp" in query:
            os.startfile("C:\\Users\\Ketan\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        
        elif "chrome" in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            
        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "instagram" in query:
            webbrowser.open("https://www.instagram.com/")

        elif "maps" in query:
            webbrowser.open("https://www.google.com/maps/@18.6793851,73.8536679,15z")

    def closeApps():
        speak("Ok sir!, Wait a second..")

        if "chrome" in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif "brave" in query:
            os.system("TASKKILL /F /im brave.exe")

        elif "code" in query:
            os.system("TASKKILL /F /im Code.exe")

        elif "whatsapp" in query:
            os.system("TASKKILL /F /im WhatsApp.exe")

    def YoutubeAuto():

        speak("Whats your Command ?")
        comm = takecommand()
        
        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'fullscreen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak('Done Sir')

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
            query = query.replace(" ","")
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
                
        elif "whatsapp message" in query:
            whatsapp()

        elif "play song" in query:
            music()

        elif "wikipedia" in query:
            speak("Searching wikipedia")
            query=query.replace("jarvis","")
            query=query.replace("wikipedia","")
            wiki=wikipedia.summary(query,2)
            speak(f"According to Wikipedia :{wiki}")

        elif "screenshot" in query:
            screenshot()

        elif "open facebook" in query:
            openApps()

        elif "open instagram" in query:
            openApps()

        elif "open code" in query:
            openApps()

        elif "open youtube" in query:
            openApps()

        elif "open brave" in query:
            openApps()

        elif "open chrome" in query:
            openApps()

        elif "open map" in query:
            openApps()

        elif "open whatsapp" in query:
            openApps()

        elif "repeat my words" in query:
            speak("speak sir")
            ab= takecommand()
            speak(f"you said : {ab}")

        elif "close chrome" in query:
            closeApps()

        elif "close brave" in query:
            closeApps()

        elif "close whatsapp" in query:
            closeApps()
        
        elif "close code" in query:
            closeApps()

        elif "chrome automation" in query:
            ChromeAuto()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'pause' in query:
            keyboard.press('k')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'dictionary' in query:
            Dict()
TaskExe()
