import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer() 
    
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 0.8  # # seconds of non-speaking audio before a phrase is considered complete
        
        audio = r.listen(source)  # to listen audio from microphone as source
        
        try:
            print("Recognizing ...")
            query = r.recognize_google(audio, language="en-us")  # Perform recognizing of the voice
            print(f"You said: {query}")
        except:
            print("Say that again please ...")  # if not recognize
            return "None"
        return query  
    