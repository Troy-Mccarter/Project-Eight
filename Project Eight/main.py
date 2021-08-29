from pyttsx3 import speak
import wishMe, take_command, engine_speak, webbrowser as wb, random, time, wikipedia

if __name__ == "__main__":
    wishMe.wishMe()  
    while(True):  # run again and again       
        query = take_command.takeCommand().lower()  # converts query into lowercase
        
        # Normal voice commands
        are_u_okay = ["are you okay", "you okay", "are you ok",
                      "are you OK", "you OK", "you ok",]
        for input_from_user in are_u_okay:  # checking if input_from_user is available in are_you_okay
            if input_from_user in query:  # if yes then check weather input_from_user is available in query
                response = ["As OK as an AI can be.",
                           "In the pink, virtually!",
                           "I am on a roll!",
                           "Feeling at the top of my game!"]
                random_response = random.choice(response)  # if yes, then print and speak the response randomly for input_from_user
                print(random_response)
                engine_speak.speak(random_response)
                
        okay = ["okay", "ok", "OK"]
        for response_for_what in are_u_okay:
            if response_for_what in query:
                response = ["As OK as an AI can be!",
                           "In the pink, virtually!",
                           "I am on a roll!",
                           "Feeling at the top of my game!"]
                random_response = random.choice(response)
                print(random_response)
                engine_speak.speak(random_response)
        
        # to search wikipedia as 'topic here + wikipedia'
        if 'wikipedia' in query:
            engine_speak.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            engine_speak.speak("According to Wikipedia")
            print(results)
            engine_speak.speak(results)
        
        # to visit any website in your browser     
        elif "open" in query:
            query = query.replace("open", "") .replace(" ", "")
            engine_speak.speak("Opening"+query)
            wb.open("https://www."+query)
            
        # to search anything search on google 
        elif "search" in query:
            query = query.replace("search", "")
            engine_speak.speak(f"Searching {query}")
            wb.open("https://www.google.com/search?q="+query)
            
        elif "quit" in query:
            print(quit())
            

            
            
        
            
        
            
    