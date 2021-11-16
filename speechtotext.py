import speech_recognition as sr
from speaktext import speak
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
            return "none"   
    return query