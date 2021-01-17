import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5') # we will use this to take voices. Window 1 API deti hai jis se hum voices ly sckty han.. inbuilt voice ko use kren gy
voices = engine.getProperty('voices') # windows mein by default 2 voices hoti.. hum aur bhe download kr sckty han..
engine.setProperty('voices',voices[1].id) #female ke voice hai 1 index pe.. 0 pe male ke hai


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant. Please tell me how may I help you")

def takeCommand(): # It takes input from microphone and return string output..
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio =r.listen(source)

    try:
       print("Recognizing...")
       query = r.recognize_google(audio)
       print("User said:", query)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query





if __name__ == '__main__':
    speak("Hello")
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic of executing tsks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir='J:\\mobile backup\\Music (mobile)'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[7]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open premiere pro' in query:
            propath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro CC 2019\\Adobe Premiere Pro.exe"
            os.startfile(propath)
        elif 'open zoom' in query:
            zoompath = "C:\\Users\\dell\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoompath)
        elif 'quit yourself' in query:
            exit()













