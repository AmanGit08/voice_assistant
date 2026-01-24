import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import requests

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your voice assistant. How can I help you?")

# Main Program
if __name__ == "__main__":
    wish_user()

    while True:
        command = take_command()

        # Greeting
        if "hello" in command:
            speak("Hello! Nice to meet you.")

        # Time
        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        # Date
        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        # Wikipedia Search
        elif "wikipedia" in command:
            speak("Searching Wikipedia")
            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=2)
            speak(result)

        # Google Search
        elif "search" in command:
            speak("Searching on Google")
            query = command.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # Weather
        elif "weather" in command:
            speak("Please tell me the city name")
            city = take_command()
            api_key = "YOUR_API_KEY"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            data = requests.get(url).json()

            if data["cod"] != "404":
                temp = data["main"]["temp"]
                speak(f"The temperature in {city} is {temp} degree Celsius")
            else:
                speak("City not found")

        # Exit
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break
