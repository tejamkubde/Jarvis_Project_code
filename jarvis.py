import imports
import speak_take


def TaskExe():
    speak_take.speak("Hello, I am jarvis!")
    speak_take.speak("How can i help you? ")

    def GoogleSearch(term):
        query = term.replace("jarvis","")
        query = query.replace("what is","")
        query = query.replace("how to","")
        query = query.replace("who is","")
        query = query.replace("what do we mean by","")
        query = query.replace("what do you mean by","")
        query = query.replace(" ","")

        Query = str(term)
        imports.pywhatkit.search(Query)
        if "google search" in Query:
            search = imports.wikipedia.summary(Query,2)
            speak_take.speak(f":According to your search : {search}")

        else:
            pass
        
    def speedtest():
        import speedtest
        speak_take.speak("Checking Speed")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown= int(downloading/800000)
        uploading= speed.upload()
        correctUpload=int(uploading/800000)

        if 'uploading' in query:
            speak_take.speak(f"The uploading speed is {correctUpload} mbps")

        elif 'downloading' in query:
            speak_take.speak(f"The downloading speed is {correctDown} mbps")


        else:
            speak_take.speak(f"The downloading speed is {correctDown} mbp/s and uploading speed is {correctUpload} mbps")

    def takeHindi():
        command = imports.sr.Recognizer()
        with imports.sr.Microphone() as source:
            print("Listening.............")
            command.pause_threshold = 1
            audio = command.listen(source)
        
            try:
                print("Recognizing............")
                query = command.recognize_google(audio,language='en-in')
                print(f'you said : {query}') 
                
            except:
                return "none"
            
            return query.lower()

    def Tran():
        speak_take.speak('Tell me the Line!')
        line = takeHindi()
        traslate = imports.Translator()
        result = traslate.translate(line)
        Text = result.text 
        speak_take.speak(f"The Translation Of This Line Is:",Text)

    def Temp():
        search="temperature in pune"
        url = f"https://www.google.com/search?q={search}"
        r=imports.requests.get(url)
        data= imports.BeautifulSoup(r.text,"html.parser")
        temperature=data.find("div",class_="BNeawe").text
        speak_take.speak(f"the temperature outside is {temperature}")

    def music():
        speak_take.speak("Tell me the name of the song!")
        musicname = speak_take.takecommand()
        imports.pywhatkit.playonyt(musicname)
        speak_take.speak("Your song has been started!, Enjoy sir")

    def whatsapp():
        speak_take.speak("Tell me the name of the person")
        name = speak_take.takecommand()


        if 'abc' in name:
            speak_take.speak("Tell me the message")
            msg=speak_take.takecommand()
            speak_take.speak("tell me the time sir")
            speak_take.speak("time in hour")
            hour=int(speak_take.takecommand())
            speak_take.speak("time in minutes")
            min=int(speak_take.takecommand())
            imports.pywhatkit.sendwhatmsg("+919307665461",msg,hour,min,20)
            speak_take.speak("ok sir, sending whatsapp message")

        elif 'about' in name:
            speak_take.speak("Tell me the message")
            msg=speak_take.takecommand()
            speak_take.speak("tell me the time sir")
            speak_take.speak("time in hour")
            hour=int(speak_take.takecommand())
            speak_take.speak("time in minutes")
            min=int(speak_take.takecommand())
            imports.pywhatkit.sendwhatmsg("+919730863521",msg,hour,min,20)
            speak_take.speak("ok sir, sending whatsapp message")
        
        else:
            speak_take.speak("tell me the phone number")
            phone=int(speak_take.takecommand())
            ph = "+91" + phone
            speak_take.speak("Tell me the message")
            msg=speak_take.takecommand()
            speak_take.speak("tell me the time sir")
            speak_take.speak("time in hour")
            hour=int(speak_take.takecommand())
            speak_take.speak("time in minutes")
            min=int(speak_take.takecommand())
            imports.pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            speak_take.speak("ok sir, sending whatsapp message")
        
    def ChromeAuto():
        speak_take.speak('Chrome Automation Started!!')
        command = speak_take.takecommand()

        if 'close this tab' in command:
            imports.keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            imports.keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            imports.keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            imports.keyboard.press_and_release('ctrl + h')

    def screenshot():
        speak_take.speak("Ok sir! What should i name that file? ")
        path = speak_take.takecommand()
        path1name  = path + ".png"
        path1 = "C:\\Users\\Ketan\\OneDrive\\Pictures\\Screenshots\\" +path1name
        kk = imports.pyautogui.screenshot()
        kk.save(path1)
        imports.os.startfile("C:\\Users\\Ketan\\OneDrive\\Pictures\\Screenshots")
        speak_take.speak("Here is your screenshot")
    
    def Dict():
        speak_take.speak('Dictionary Activated !!')
        speak_take.speak('Tell me the Word Sir...!')
        prob1 = speak_take.takecommand()

        if 'meaning' in prob1:
            # probl = probl.replace("what is the","")
            # probl = probl.replace("jarvis","")
            # probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = imports.diction.meaning(probl)
            speak_take.speak(f'The Meaning For {probl} is {result}')
            
        else:
            speak_take.speak("tejam")

    def openApps():
        speak_take.speak("Ok sir, Wait a second!")

        if "code" in query:
            imports.os.startfile("C:\\Users\\Ketan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "brave" in query:
            imports.os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

        elif "whatsapp" in query:
            imports.os.startfile("C:\\Users\\Ketan\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            
        elif "chrome" in query:
            imports.os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "facebook" in query:
            imports.webbrowser.open("https://www.facebook.com/")
                
        elif "youtube" in query:
            imports.webbrowser.open("https://www.youtube.com/")

        elif "instagram" in query:
            imports.webbrowser.open("https://www.instagram.com/")

        elif "maps" in query:
            imports.webbrowser.open("https://www.google.com/maps/@18.6793851,73.8536679,15z")

    def closeApps():
        speak_take.speak("Ok sir!, Wait a second..")

        if "chrome" in query:
            imports.os.system("TASKKILL /F /im chrome.exe")

        elif "brave" in query:
            imports.os.system("TASKKILL /F /im brave.exe")

        elif "code" in query:
            imports.os.system("TASKKILL /F /im Code.exe")

        elif "whatsapp" in query:
            imports.os.system("TASKKILL /F /im WhatsApp.exe")
        
    def YoutubeSearch(term):
        result = "https://www.youtube.com/results?search_query=" + term
        imports.webbrowser.open(result)
        speak_take.speak("This is what i found for your search")
        imports.pywhatkit.playonyt(term)
        speak_take.speak("This may also help you Sir")

    def YoutubeAuto():
        speak_take.speak("Whats your Command ?")
        comm = speak_take.takecommand()
            
        if 'pause' in comm:
            imports.keyboard.press('space bar')

        elif 'restart' in comm:
            imports.keyboard.press('0')

        elif 'mute' in comm:
            imports.keyboard.press('m')

        elif 'skip' in comm:
            imports.keyboard.press('l')

        elif 'back' in comm:
            imports.keyboard.press('j')

        elif 'full screen' in comm:
            imports.keyboard.press('f')

        elif 'film mode' in comm:
            imports.keyboard.press('t')

        speak_take.speak('Done Sir')



    while True:
        query=speak_take.takecommand()

        if "hello" in query:
            speak_take.speak("hello sir i am jarvis")
            speak_take.speak("your personal assistant")
            speak_take.speak("How may i help you?")

        elif "how are you" in query:
            speak_take.speak("I am fine sir")
            speak_take.speak("what about you")

        elif "you need a break" in query:
            speak_take.speak("ok sir")
            speak_take.speak("you can call me anytime")
            speak_take.speak("Just say Wake Up jarvis!")
            break

        elif "bye" in query:
            speak_take.speak("bye sir")
            speak_take.speak("have a good day")
            break

        elif "youtube search" in query:
            query = query.replace("youtube search","")
            query = query.replace("jarvis","")
            YoutubeSearch(query)

            
        elif "google search" in query:
            speak_take.speak("This is what i found for your search sir!")
            query = query.replace("google search","")
            query = query.replace("jarvis","")
            # pywhatkit.search(query)
            GoogleSearch(query)
            speak_take.speak("Done Sir!!")

        elif "website" in query:
            speak_take.speak("Ok sir, Launching")
            query = query.replace("website","")
            query = query.replace("jarvis","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = "https://www." + web1 + ".com"
            imports.webbrowser.open(web2)
            speak_take.speak("launched sir!")

        elif "launch" in query:
            speak_take.speak("Tell me the name of the website!")
            name = speak_take.takecommand()
            web = 'https://www.' + name + '.com'
            imports.webbrowser.open(web)
            speak_take.speak("Done Sir!")
                
        # elif "whatsapp message" in query:
        #     whatsapp()

        elif "play song" in query:
            music()

        elif "wikipedia" in query:
            speak_take.speak("Searching wikipedia")
            query=query.replace("jarvis","")
            query=query.replace("wikipedia","")
            wiki= imports.wikipedia.summary(query,2)
            speak_take.speak(f"According to Wikipedia :{wiki}")

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
            speak_take.speak("speak sir")
            ab= speak_take.takecommand()
            speak_take.speak(f"you said : {ab}")

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

        elif 'stop' in query:
            imports.keyboard.press('spacebar')

        elif 'restart' in query:
            imports.keyboard.press('0')

        elif 'mute' in query:
            imports.keyboard.press('m')

        elif 'skip' in query:
            imports.keyboard.press('l')

        elif 'back' in query:
            imports.keyboard.press('j')

        elif 'full screen' in query:
            imports.keyboard.press('f')

        elif 'film mode' in query:
            imports.keyboard.press('t')

        elif 'pause' in query:
            imports.keyboard.press('k')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'dictionary' in query:
            Dict()

        elif 'joke' in query:
            get = imports.pyjokes.get_joke()
            speak_take.speak(get)
        
        elif "that was pretty cringe" in query:
            speak_take.speak("reaaaalllllly??????????????????")

        elif 'alarm' in query:
            speak_take.speak("enter the time")
            time=input(": Enter the time :")


            while True:
                Time_Ac= imports.datetime.datetime.now()
                now=Time_Ac.strftime("%H:%M:%S")



                if now==time:
                    speak_take.speak("time to wake up sir")
                    imports.playsound('D:\\jarvis project\\newsound.mp3')
                    speak_take.speak("Alarm closed")

                elif now>time:
                    break
        
        elif "remember that" in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = query .replace("jarvis","")
            speak_take.speak("You Told me to remind you that :" +rememberMsg)
            remember = open("data.txt","w")
            remember.write(rememberMsg)
            remember.close()

        elif "what do you remember" in query:
            remember = open("data.txt","r")
            speak_take.speak("You told me to remind that" +remember.read())

        elif 'please search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak_take.speak("This is what i found on the web")

            try:
                # pywhatkit.search(query)
                result = googleScrap.summary(query,2)
                speak_take.speak(result)

            except:
                speak_take.speak("no speakable data available")

        elif 'temperature' in query:
            Temp()

        # elif 'translator' in query:
        #     Tran()

        elif 'downloading speed' in query:
            speedtest()    

        elif 'uploading speed' in query:
            speedtest()    

        elif 'internet speed' in query:
            speedtest()

        elif 'whatsapp message' in query:
            query = query.replace("jarvis","")
            query = query.replace("send","")
            query = query.replace("whatsapp message","")
            query = query.replace("to","")
            name = query
            
            if 'laptop' in name:
                numb = "9067084690"
                speak_take.speak(f"Whats the Message For {name}")
                mess = speak_take.takecommand()
                whatsapp.whatsapp(numb,mess)
            
            elif 'pretty' in name:
                numb = "9307665461"
                speak_take.speak(f"Whats the Message For {name}")
                mess = speak_take.takecommand()
                whatsapp.whatsapp(numb,mess)

            elif 'bag' in name:
                numb = "8484037377"
                speak_take.speak(f"Whats the Message For {name}")
                mess = speak_take.takecommand()
                whatsapp.whatsapp(numb,mess)
       
            elif 'jarvis' in name:
                gro = "KsjFp8jhhPA9UHap9dRHcU"
                speak_take.speak(f"Whats the Message for {name} ")
                mess = speak_take.takecommand()
                whatsapp.Whatsapp_Grp(gro,mess)



TaskExe()
