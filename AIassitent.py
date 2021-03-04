import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greeting():
    hours = int(datetime.datetime.now().hour)
    if hours >= 0 and hours < 12:
        speak('Good morning')
    elif hours >=12 and hours<18:
        speak('Good Afternoon')
    else:
        speak('Good evening:')
    speak("Hello Aman sir my name is Monty. How may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listing...')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f'Your query : {query}\n')
        except Exception as e:
            print("Could not recognize. Please say it again")
            speak('Could not recognize. Please say it again')
        
    return query


        
def Number_finder(query):
    lst = []
    for i in query.split(' '):
        try:
            lst.append(float(i))
        except:
            pass
        
    return lst

if __name__ == '__main__':
    greeting()
    lst = []
    while True:
        query = takecommand().lower()
    
        for i in query.split(' '):
            lst = Number_finder(query)
        if 'wikipedia' in query:
            print('Searching wikipedia')
            speak('Searching wikipedia')
            query = query.replace('wikipedia',' ')
            query = wikipedia.summary(query,sentences = 2)
            print(f'Wikipedia : {query}\n')
            speak(query)
            
        elif 'add'in query:
            sum = lst[0] + lst[1]
            print(f"Answer is {sum}")
            speak(f"Answer is {str(sum)}")
            
        elif 'subract' in query:
            ans = lst[0] - lst[1]
            print(f"Answer is {ans}")
            speak(f"Answer is {str(ans)}")
            
        elif 'multiply' in query:
            ans = lst[0] * lst[1]
            print(f"Answer is {ans}")
            speak(f"Answer is {str(ans)}")
        
        elif 'divide' in query:
            ans = lst[0] / lst[1]
            print(f"Answer is {ans}")
            speak(f"Answer is {str(ans)}")
                
            print("Factorial is {fact}")
            speak("Factorial is {str(fact)}")
            
        elif 'open google' in query:
            print('opening google')
            speak('opening google')
            webbrowser.open('google.com')
            
        elif 'open instagram' in query:
            print('opening instagram')
            speak('opening instagram')
            webbrowser.open('instagram.com')
        elif 'open facebook' in query:
            print('opening facebook')
            speak('opening facebook')
            webbrowser.open('facebook.com')
        elif 'open youtube' in query:
            print('opening youtube')
            speak('opening youtube')
            webbrowser.open('youtube.com')
            
        elif 'open sublime text' in query:
            path = '"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"'
            print('opening sublime text')
            speak('opening sublime text')
            os.startfile(path)
        elif 'open chrome' in query:
            path = 'C:\\Users\\asaxe\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
            print('opening chrome')
            speak('opening chrome')
            os.startfile(path)
        elif 'play music' in query:
            path = 'F:\\songs'
            songs = os.listdir(path)
            print('Songs list:')
            for i in songs:
                print(i)
            print('\nWhich song do u want to listen')
            speak('which song do u want to listen')
            song = takecommand().lower()
            print(f'playing {song}')
            speak(f'playing {song}')
            numbers_of_songs = len(songs)
            for i in range(numbers_of_songs):
                songs[i] = songs[i].lower()
            for i in range(numbers_of_songs):
                if song in songs[i]:
                    os.startfile(os.path.join(path,songs[i]))  
                              
        elif 'your developer' in query:
            print("I developed by Aman saxena")
            speak("I developed by Aman saxena") 
        elif 'stop' in query:
            speak('ok sir')
            exit()
    