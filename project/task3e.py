import pyttsx3
import speech_recognition as sr


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

def sine():
    import numpy as np

    import matplotlib.pyplot as plot

    time = np.arange(0, 10, 0.1)
    amplitude   = np.sin(time)
    plot.plot(time, amplitude)
    plot.title('Sine wave')
    plot.xlabel('Time')
    plot.ylabel('Amplitude = sin(time)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show() 
    
def cosine():
    import numpy as np

    import matplotlib.pyplot as plot

    time = np.arange(0, 10, 0.1)
    amplitude   = np.cos(time)
    plot.plot(time, amplitude)
    plot.title('cosine wave')
    plot.xlabel('Time')
    plot.ylabel('Amplitude = cosine(time)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show() 
def tan():
    import numpy as np

    import matplotlib.pyplot as plot

    time = np.arange(0, 10, 0.1)
    amplitude = np.tan(time)
    plot.plot(time, amplitude)
    plot.title('tan wave')
    plot.xlabel('Time')
    plot.ylabel('Amplitude = tan(time)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.show()        
         


while True:

    print("which graph you what to see ")
    speak("which graph you what to see ")
    print("speak open graph .. sin, cos, tan or exit to end program")
    
    query = listen().lower()
    

    if 'open' in query:
         
        try:
        
            name= list(query.split()) 
            name= name[name.index('open')+1]


            if name in ("tan","10","tent"):
                speak("opeing tan graph")
                tan()
                break
            if name in ("cos","kos","cost","cose","course","call"):
                speak("opening cosine graph")
                cosine()
                break
            if name in ("sin","sine","sign","science"):
                speak("opening sin graph")
                sine()
                break 
        except Exception as e:
            print(e)
            speak("not able to open.try again")

    elif 'exit' in query:
        break  
            

