import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ", 1)
        if len(parts) > 1:
            song = parts[1].strip()
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                print("Sorry, I couldn't find that song.")
        else:
            speak("Please say the song name after play.")

if __name__ == "__main__":
    speak("Initialising broVA...")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "hey" in word.lower() and "bro" in word.lower() :
                with sr.Microphone() as source:
                    print("broVA active, listening for command...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processCommand(command) 

        except Exception as e:
            print("Error:", e)


