import datetime
import os

import pyttsx3
import requests
import speech_recognition as sr
from bs4 import BeautifulSoup

sammy = pyttsx3.init()
voices = sammy.getProperty('voices')
sammy.setProperty('voice', voices[0].id)
sammy.setProperty('rate', 180)
sammy.setProperty('volume', 0.7)


# the assistant speak function
def speak(audio):
    print(f"Jennifer: {audio}")
    x = open('report.txt', 'a')
    print(f"Jennifer: {audio}", file=x)
    sammy.say(audio)
    sammy.runAndWait()


# boot up (start up the programme)
def boot_up():
    speak("welcome back sir!")
    speak("Allow me to introduce myself, I am Jennifer, your virtual artificial intelligence Assistant.")
    speak("And I am here to assist you with variety of tasks as best as I can. 24 hours a day, 7"
          " days a week.")
    speak("Starting all systems applications.")
    speak("Installing and checking all drivers.")
    speak("Calibrating and examining all the core processors.")
    speak("Checking the internet connection.")
    speak("Wait a moment sir.")
    speak("All drivers are up and running.")
    speak("All systems have been activated.")
    speak("Now I am online.")


# start up (greet me)
def start_up():
    boot_up()
    # Temperature
    search = 'weather in cape town'
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    timer_1 = data.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    lyst = timer_1.split()
    weather1 = lyst[2:]
    total_weather = ' '.join([str(item) for item in weather1]).lower()

    # current time
    c_time = datetime.datetime.now().strftime("%I:%M:%S %p")

    # current date
    c_date = datetime.datetime.now().strftime("%d-%B-%Y")
    c_day = datetime.datetime.now().strftime("%A")

    # current hour
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    elif 18 <= hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")

    speak(f"Jennifer at your service."
          f"\nThe date is {c_day} the {c_date}, and the time is currently {c_time}."
          f"\nThe temperature is {temp}, {total_weather}."
          f"\nPlease tell me how can I help you sir?")


# take command function
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-US")
        x = open('report.txt', 'a')
        print(f"User: {query}", file=x)
    except Exception as e:
        print(f"Exception: {str(e)}")
        speak("Sorry, I didn't understand that.")
        return None
    query = query.lower()
    return query

#
# if __name__ == "__main__":
#     start_up()
#
#     while True:
#         query = take_command()
#
#         if 'hello' in query:
#             speak("Hi")
