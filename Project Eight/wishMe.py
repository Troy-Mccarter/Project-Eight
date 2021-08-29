import engine_speak, datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)  # getting current hour of time in 24 hour time format
    
    if hour >= 0 and hour < 12:
        engine_speak.speak("Good Morning!")
    elif hour >=12 and hour < 17:
        engine_speak.speak("Good Afternoon!")
    elif hour >=17 and hour < 20:
        engine_speak.speak("Good Evening!")
    elif hour >=20 and hour < 24:
        engine_speak.speak("Night Time!")
        
    engine_speak.speak("I am Eight. How may I help you?")  # speaks after wishMe
    
    
    