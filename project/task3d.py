import pyttsx3
import speech_recognition as sr
import os


engine = pyttsx3.init('sapi5') 

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def listen(): 

    

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Iam listening.....")

        r.pause_threshold=1

        audio = r.listen(source)

    try:

        print("Recognizing.....")

        query = r.recognize_google(audio, language = 'en-in')

        print(f"User said:{query}\n")

        

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return(query)

while True:
    print("speak open notepade ")
    query = listen().lower()
    

    if 'open' in query:
         
        try:
            p = list(query.split()) 

            p = p[p.index('open')+1]

            

            if p=="Notepad"or "notepade":
                speak("Opening Notepad")
                os.system("Notepad") 
            else :
                speak("try again")      
        except Exception as e:
            print(e)
            speak("not able to open.try again")

    elif 'exit' in query:
        break  
