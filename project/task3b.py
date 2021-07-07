import speech_recognition as sr
import pyttsx3
import webbrowser as web 
engine = pyttsx3.init('sapi5') 

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def main():

    #path =  str("https://docs.google.com/")+str(site)+str("/u/6/")

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("for opening google sites,docs,sheets,forms respectively\n\n")
        print("speak anyone from this presentation,document,spreadsheets,forms\n")
        print("listing .. ")
        
  
        audio = r.listen(source)

        print("Recognizing ...")

        try:
            site=r.recognize_google(audio)
            print("Did you say  "+ site)
            path =  str("https://docs.google.com/")+str(site)+str("/u/6/")

            a=web.open(path)
            b="opeing google"+str(site)
            speak(b)
            open(a)
        except Exception as e:
            print("Error.."+str(e))  

if __name__ =="__main__":
    main()
            