import wolframalpha
import webbrowser as wb
import pyttsx3
import pyaudio
import speech_recognition as sr 
import wikipedia
import sys

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('LX3VUJ-P5KRT24VJA')

class assistant:
    def say(audio):
        print('Computer: '+audio)
        engine.say(audio)
        engine.runAndWait()
    class search:
        def wikipedia(queryWiki):
            outcome = wikipedia.search(queryWiki)
            print("Computer: "+outcome)
            engine.say(outcome)
            engine.runAndWait()

        def wolframalpha(query):
            res = client.query(query) 
            output = next(res.results).text
            output = str(output)
            print("Computer: "+output)
            engine.say(output)
            engine.runAndWait()

        def Engine(w3Address):
            wb.open(w3Address)
            print("Computer: opening "+w3Address)
    class control:
        def exit():
            sys.exit()
        


    class Voice:
        class get:
         


            def myCommand():

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('LISTENING......')
                    audio2 = r.listen(source)
        
    
                    try:
                        text = r.recognize_google(audio2)
                        print(text)
                    except:
                        print("sorry! Unable to connect")
                        engine.say('sorry! Unable to connect')
                        engine.runAndWait()
    
    
