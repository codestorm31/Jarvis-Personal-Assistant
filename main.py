import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import requests
from bs4 import BeautifulSoup

recognizer=sr.Recognizer()
ttsx=pyttsx3.init()

def searchWeb(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the first result
    result = soup.find("div", class_="BNeawe").get_text()
    
    return result

def speak(text):
     ttsx.say(text)
     ttsx.runAndWait()
     
def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.in")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLib.music[song]
        webbrowser.open(link)
        
    elif c.lower().startswith("search"):
        query=c.lower()
        searchRes=searchWeb(query)
        print("Search Result opening.....")
        speak("Here's what I found:"+searchRes)
        webbrowser.open(f"https://www.google.com/search?q={c}")

if __name__=="__main__":
    speak("Hello, Sir! I am Jarvis, your personal assistant. How can I assist you today?")
    #Listen for the wake word "Jarvis"
    while True:
        r = sr.Recognizer()
        print("Recognizing....")

        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes Sir")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis ON...")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                command=r.recognize_google(audio)
                    
                processCommand(command)
                    
        except Exception as e:
            print("Error; {0}".format(e))


