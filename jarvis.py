import imports
import cmd
               
def TaskExe():
    cmd.speak("Hello, I am jarvis!")
    cmd.speak("How can i help you? ")

    def speedtest():
        import speedtest
        cmd.speak("Checking Speed")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown= int(downloading/800000)
        uploading= speed.upload()
        correctUpload=int(uploading/800000)

        if 'uploading' in query:
            cmd.speak(f"The uploading speed is {correctUpload} mbps")

        elif 'downloading' in query:
            cmd.speak(f"The downloading speed is {correctDown} mbps")


        else:
            cmd.speak(f"The downloading speed is {correctDown} mbp/s and uploading speed is {correctUpload} mbps")

    def takeHindi():
        cmd = imports.sr.Recognizer()
        with imports.sr.Microphone() as source:
            print("Listening.............")
            cmd.pause_threshold = 1
            audio = cmd.listen(source)
       
        try:
            print("Recognizing............")
            query = cmd.recognize_google(audio,language='en-in')
            print(f'you said : {query}') 
            
        except:
            return "none"
        
        return query.lower()

    def Tran():
        cmd.speak('Tell me the Line!')
        line = takeHindi()
        traslate = imports.Translator()
        result = traslate.translate(line)
        Text = result.text 
        cmd.speak(f"The Translation Of This Line Is:",Text)

    def Temp():
        search="temperature in pune"
        url = f"https://www.google.com/search?q={search}"
        r=imports.requests.get(url)
        data= imports.BeautifulSoup(r.text,"html.parser")
        temperature=data.find("div",class_="BNeawe").text
        cmd.speak(f"the temperature outside is {temperature}")

    def music():
        cmd.speak("Tell me the name of the song!")
        musicname = cmd.takecmd()
        imports.pywhatkit.playonyt(musicname)
        cmd.speak("Your song has been started!, Enjoy sir")

    def whatsapp():
        cmd.speak("Tell me the name of the person")
        name = cmd.takecmd()


        if 'abc' in name:
            cmd.speak("Tell me the message")
            msg=cmd.takecmd()
            cmd.speak("tell me the time sir")
            cmd.speak("time in hour")
            hour=int(cmd.takecmd())
            cmd.speak("time in minutes")
            min=int(cmd.takecmd())
            imports.pywhatkit.sendwhatmsg("+919307665461",msg,hour,min,20)
            cmd.speak("ok sir, sending whatsapp message")

        elif 'about' in name:
            cmd.speak("Tell me the message")
            msg=cmd.takecmd()
            cmd.speak("tell me the time sir")
            cmd.speak("time in hour")
            hour=int(cmd.takecmd())
            cmd.speak("time in minutes")
            min=int(cmd.takecmd())
            imports.pywhatkit.sendwhatmsg("+919730863521",msg,hour,min,20)
            cmd.speak("ok sir, sending whatsapp message")
    
        else:
            cmd.speak("tell me the phone number")
            phone=int(cmd.takecmd())
            ph = "+91" + phone
            cmd.speak("Tell me the message")
            msg=cmd.takecmd()
            cmd.speak("tell me the time sir")
            cmd.speak("time in hour")
            hour=int(cmd.takecmd())
            cmd.speak("time in minutes")
            min=int(cmd.takecmd())
            imports.pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            cmd.speak("ok sir, sending whatsapp message")
    
    def ChromeAuto():
        cmd.speak('Chrome Automation Started!!')
        cmd = cmd.takecmd()

        if 'close this tab' in cmd:
            imports.keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in cmd:
            imports.keyboard.press_and_release('ctrl + t')

        elif 'open new window' in cmd:
            imports.keyboard.press_and_release('ctrl + n')

        elif 'history' in cmd:
            imports.keyboard.press_and_release('ctrl + h')

    def screenshot():
        cmd.speak("Ok sir! What should i name that file? ")
        path = cmd.takecmd()
        path1name  = path + ".png"
        path1 = "C:\\Users\\Ketan\\OneDrive\\Pictures\\Screenshots\\" +path1name
        kk = imports.pyautogui.screenshot()
        kk.save(path1)
        imports.os.startfile("C:\\Users\\Ketan\\OneDrive\\Pictures\\Screenshots")
        cmd.speak("Here is your screenshot")
 
    def Dict():
        cmd.speak('Dictionary Activated !!')
        cmd.speak('Tell me the Word Sir...!')
        prob1 = cmd.takecmd()

        if 'meaning' in prob1:
            # probl = probl.replace("what is the","")
            # probl = probl.replace("jarvis","")
            # probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = imports.diction.meaning(probl)
            cmd.speak(f'The Meaning For {probl} is {result}')
        
        else:
            cmd.speak("tejam")

    def openApps():
        cmd.speak("Ok sir, Wait a second!")

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
        cmd.speak("Ok sir!, Wait a second..")

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
        cmd.speak("This is what i found for your search")
        imports.pywhatkit.playonyt(term)
        cmd.speak("This may also help you Sir")

    def YoutubeAuto():

        cmd.speak("Whats your Cmd ?")
        comm = cmd.takecmd()
        
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

        cmd.speak('Done Sir')

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
            cmd.speak(f":According to your search : {search}")

        else:
            pass

    while True:
        query=cmd.takecmd()

        if "hello" in query:
            cmd.speak("hello sir i am jarvis")
            cmd.speak("your personal assistant")
            cmd.speak("How may i help you?")

        elif "how are you" in query:
            cmd.speak("I am fine sir")
            cmd.speak("what about you")

        elif "you need a break" in query:
            cmd.speak("ok sir")
            cmd.speak("you can call me anytime")
            cmd.speak("Just say Wake Up jarvis!")
            break

        elif "bye" in query:
            cmd.speak("bye sir")
            cmd.speak("have a good day")
            break

        elif "youtube search" in query:
            query = query.replace("youtube search","")
            query = query.replace("jarvis","")
            YoutubeSearch(query)

            
        elif "google search" in query:
            cmd.speak("This is what i found for your search sir!")
            query = query.replace("google search","")
            query = query.replace("jarvis","")
            # pywhatkit.search(query)
            GoogleSearch(query)
            cmd.speak("Done Sir!!")

        elif "website" in query:
            cmd.speak("Ok sir, Launching")
            query = query.replace("website","")
            query = query.replace("jarvis","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = "https://www." + web1 + ".com"
            imports.webbrowser.open(web2)
            cmd.speak("launched sir!")

        elif "launch" in query:
            cmd.speak("Tell me the name of the website!")
            name = cmd.takecmd()
            web = 'https://www.' + name + '.com'
            imports.webbrowser.open(web)
            cmd.speak("Done Sir!")
                
        # elif "whatsapp message" in query:
        #     whatsapp()

        elif "play song" in query:
            music()

        elif "wikipedia" in query:
            cmd.speak("Searching wikipedia")
            query=query.replace("jarvis","")
            query=query.replace("wikipedia","")
            wiki= imports.wikipedia.summary(query,2)
            cmd.speak(f"According to Wikipedia :{wiki}")

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
            cmd.speak("speak sir")
            ab= cmd.takecmd()
            cmd.speak(f"you said : {ab}")

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
            cmd.speak(get)
        
        elif "that was pretty cringe" in query:
            cmd.speak("reaaaalllllly??????????????????")

        elif 'alarm' in query:
            cmd.speak("enter the time")
            time=input(": Enter the time :")


            while True:
                Time_Ac= imports.datetime.datetime.now()
                now=Time_Ac.strftime("%H:%M:%S")



                if now==time:
                    cmd.speak("time to wake up sir")
                    imports.playsound('D:\\jarvis project\\newsound.mp3')
                    cmd.speak("Alarm closed")

                elif now>time:
                    break
        
        elif "remember that" in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = query .replace("jarvis","")
            cmd.speak("You Told me to remind you that :" +rememberMsg)
            remember = open("data.txt","w")
            remember.write(rememberMsg)
            remember.close()

        elif "what do you remember" in query:
            remember = open("data.txt","r")
            cmd.speak("You told me to remind that" +remember.read())

        elif 'please search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            cmd.speak("This is what i found on the web")

            try:
                # pywhatkit.search(query)
                result = googleScrap.summary(query,2)
                cmd.speak(result)

            except:
                cmd.speak("no speakable data available")

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
                cmd.speak(f"Whats the Message For {name}")
                mess = cmd.takecmd()
                whatsapp.whatsapp(numb,mess)
            
            elif 'pretty' in name:
                numb = "9307665461"
                cmd.speak(f"Whats the Message For {name}")
                mess = cmd.takecmd()
                whatsapp.whatsapp(numb,mess)

            elif 'bag' in name:
                numb = "8484037377"
                cmd.speak(f"Whats the Message For {name}")
                mess = cmd.takecmd()
                whatsapp.whatsapp(numb,mess)
       
            elif 'jarvis' in name:
                gro = "KsjFp8jhhPA9UHap9dRHcU"
                cmd.speak(f"Whats the Message for {name} ")
                mess = cmd.takecmd()
                whatsapp.Whatsapp_Grp(gro,mess)



TaskExe()
