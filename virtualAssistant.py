import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"{command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didnt understand")
            return None
        except sr.RequestError:
            print("Request error")
            return None

def main():
    speak("Hello")
    while True:
        command = listen()
        if command:
            command = command.lower()
            if 'Bye' in command:
                speak("Goodbye!")
                break
            elif 'Hello' in command:
                speak("Hi!")
            else:
                speak("I can't help about that right now")

if __name__ == "_main_":
    main()