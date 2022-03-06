import imports

Assistant = imports.pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[1].id)
Assistant.setProperty("rate",170)

def speak(audio):
    print("     ")
    Assistant.say(audio)

    print(f":{audio}")
    Assistant.runAndWait()
    
def takecommand():
    command = imports.sr.Recognizer()
    with imports.sr.Microphone() as source:
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