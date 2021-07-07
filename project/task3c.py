import pyttsx3
import speech_recognition as sr
import webbrowser as web 
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

while(True): 
    print("\n\nspeak open google ... blog ,hangouts ,podcasts ,travel ,classrom ,keep\n") 
    print("speak exit ... to exit the program ")

    query = listen().lower()

    if 'open google' in query:
         
        try:
            name = list(query.split()) 

            name = name[name.index('google')+1]
            
            if name =="blog":
                web.open("https://www.blogger.com/about/?tab=oj&bpli=1")

            elif name =="hangouts"or"hangout":               
                 web.open("https://hangouts.google.com/?authuser=6")

            elif name =="keep": 
                web.open("https://keep.google.com/u/6/")  

            elif name =="classrom"or"classroms":   
                web.open("https://classroom.google.com/u/6/h")  

            elif name =="travel":  
                web.open("https://www.google.com/travel/?dest_src=al&authuser=6")

            elif name =="podcasts"or"podcast":
                web.open("https://podcasts.google.com/u/6/")

        except Exception as e:

            print(e)

            speak("sorry unable to open it please .Try again")
    elif 'exit' in query:
        break        
