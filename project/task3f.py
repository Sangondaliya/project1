import pyttsx3
import speech_recognition as sr
import pandas as pd  

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

df=pd.read_excel("C:\python\ml.xlsx")

print(df)

while True :

   # print(" the number of row or coloum to open\n ")
    print("speak open head or speak open tail ")
    
    query = listen().lower()
    

    if 'open' in query:
         
        try:
            p = list(query.split()) 

            p = p[p.index('open')+1]
            

            
            if p =='head':
                speak("opening head")
                print(df.head())
                break
            elif p=='tail':
                speak("opening tail")
                print(df.tail())
                break

        except Exception as e:
            print(e)
            speak("please try again")
    elif 'exit'in query:
        break          





