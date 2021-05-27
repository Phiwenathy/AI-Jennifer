import smtplib
import subprocess
import webbrowser
from tkinter.filedialog import *
import pyautogui  # pip install pyautogui
from pyautogui import *
import pyttsx3  # pip install pyttsx3
import pywhatkit  # pip install pywhatkit
import requests  # pip install requests
import speedtest  # pip install speedtest-cli
from bs4 import BeautifulSoup  # pip install beautifulsoup4
import speech_recognition as sr  # pip install SpeechRecognition
import PyPDF2  # pip install PyPDF2
from keyboard import *  # pip install keyboard

sammy = pyttsx3.init()
voices = sammy.getProperty('voices')
sammy.setProperty('voice', voices[0].id)
sammy.setProperty('rate', 180)
sammy.setProperty('volume', 0.7)


# the assistant speak function
def speak(audio):
    x = open('report.txt', 'a')
    print(f"Jennifer: {audio}", file=x)
    print(f"Jennifer: {audio}")
    sammy.say(audio)
    sammy.runAndWait()


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
        print(f"User: {query}")
    except Exception as e:
        print(f"Exception: {str(e)}")
        speak("Sorry, I didn't understand that.")
        return None
    query = query.lower()
    return query


# make note in notepad++
def make_note(text1):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text1)
    notepad = "C:/Program Files (x86)/Notepad++/notepad++.exe"
    subprocess.Popen([notepad, file_name])


# boot up (start up the programme)
def boot_up():
    speak("welcome back sir!")
    speak("Allow me to introduce myself, I am Jennifer, your virtual artificial intelligence Assistant.")
    speak("And I am here to assist you with variety of tasks as best as I can. 24 hours a day, 7"
          " days a week.")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Calibrating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")


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
    print(lyst)
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

    speak(f"Jennifer at your service.")
    speak(f"The date is {c_day} the {c_date}, and the time is currently {c_time}.")
    speak(f"The temperature is {temp}, {total_weather}.")
    speak("Please tell me how can I help you sir?")


# function for closing the assistant
def close_sys():
    # Check if its Morning or Afternoon, or Evening, or Night
    my_timer = time.localtime()
    if 5 <= my_timer.tm_hour <= 11:
        speak("Okay sir, you can call me anytime you need me."
              " Jennifer out, Enjoy your morning.")
        quit()

    elif 12 <= my_timer.tm_hour <= 17:
        speak("Okay sir, you can call me anytime you need me."
              " Jennifer out, Enjoy the rest of the day.")
        quit()

    elif 18 <= my_timer.tm_hour <= 22:
        speak("Okay sir, you can call me anytime you need me."
              " Jennifer out, Have a lovely evening.")
        quit()

    else:
        speak("Okay sir, you can call me anytime you need me. "
              "Jennifer out, Have good night.")
        quit()


# taking screenshots
def screenshot():
    speak('What should I name the screenshot file sir?')
    name = take_command().lower()
    speak('Please hold the screen for a few seconds, i am taking the screenshot sir.')
    time.sleep(3)
    photo = f"{name}.png"
    path = f"C:/Users/zasodozay/Downloads/ScreenShots/{photo}"
    img = pyautogui.screenshot()
    img.save(path)
    speak("I have taken the screenshot, it is saved in screenshot folder under downloads sir.")


# opening system apps
def open_apps(query):
    name = query
    speak("Ok sir, please wait!")

    # opens notepad (works)
    if 'open system notepad' in name:
        n_path = "C:/WINDOWS/system32/notepad.exe"
        speak("Opening notepad.")
        os.startfile(n_path)
        speak("Notepad opened Sir.")

    # opens pycharm (works)
    if 'open pycharm' in name:
        py_path = "C:/Program Files/JetBrains/PyCharm 2020.2.3/bin/pycharm64.exe"
        speak("Opening pycharm.")
        os.startfile(py_path)
        speak("Pycharm opened Sir.")

    # open word app (works)
    elif 'open word' in name:
        speak('opening microsoft word.')
        os.system('start WINWORD.EXE')
        speak('microsoft word has been opened sir.')

    # open powerpoint app (works)
    elif 'open powerpoint' in name:
        speak('Opening microsoft powerpoint.')
        os.system('start POWERPNT.EXE')
        speak('Microsoft powerpoint has been opened sir.')

    # open excel app (works)
    elif 'open excel' in name:
        speak('opening microsoft excel.')
        os.system('start excel.exe')
        speak('microsoft excel has been opened sir.')

    # opens adobe reader (works)
    elif 'open pdf reader' in name or 'open adobe' in name or 'open adobe reader' in name:
        speak("Opening adobe reader.")
        os.system('start AcroRd32.exe')
        speak("Adobe reader opened Sir.")

    # opens command prompt (works)
    elif 'open command' in name:
        speak("Opening command prompt.")
        os.system("Start cmd")
        speak("Command prompt opened Sir.")

    # opens outlook (works)
    elif 'open outlook' in name:
        speak("Opening outlook.")
        os.system('start OUTLOOK.EXE')
        speak("Outlook opened Sir.")

    # opens teams (works)
    elif 'open teams' in name:
        t_path = "C:/Users/zasodozay/AppData/Local/Microsoft/Teams/current/Teams.exe"
        speak("Opening microsoft teams.")
        os.startfile(t_path)
        speak("Microsoft teams opened Sir.")

    # opens microsoft edge (works)
    elif 'open edge' in name:
        speak("Opening microsoft Edge.")
        os.system('start msedge.exe')
        speak("Microsoft Edge opened Sir.")

    # opens Qt Designer (works)
    elif 'open designer' in name:
        t_path = "C:/Program Files (x86)/Qt Designer/designer.exe"
        speak("Opening Qt designer.")
        os.startfile(t_path)
        speak("Qt designer opened Sir.")

    # opens notepad plus (works)
    elif 'open notepad plus' in name:
        speak("Opening Notepad plus plus.")
        os.system('start notepad++.exe')
        speak("Notepad plus plus opened Sir.")

    # open online telegram (works)
    elif 'open online telegram' in name:
        speak("Opening telegram.")
        webbrowser.open("https://web.telegram.org/#/im?p=@selutpam01_bot")
        speak("Telegram opened Sir.")

    # open desktop telegram (works)
    elif 'open telegram' in name:
        path = "C:/Users/zasodozay/AppData/Roaming/Telegram Desktop/Telegram.exe"
        speak("Opening telegram.")
        os.startfile(path)
        speak("Telegram opened Sir.")

    # open chrome (works)
    elif 'open chrome' in name:
        speak("Opening chrome.")
        os.system('start chrome.exe')
        speak("Chrome opened Sir.")

    # open 4kvideodownloader (works)
    elif 'open video downloader' in name:
        path = "C:/Program Files/4KDownload/4kvideodownloader/4kvideodownloader.exe"
        speak("Opening 4k video downloader.")
        os.startfile(path)
        speak("4k video downloader opened Sir.")

    # open youtube (works)
    elif 'open youtube' in name:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com/")
        speak("YouTube opened Sir.")


# closing system apps
def close_apps():
    speak("Which app should I close sir?")
    name = take_command().lower()
    speak("Ok sir,please wait a moment!")

    # close notepad
    if 'close notepad' in name:
        speak("Closing notepad.")
        os.system("taskkill /f /im notepad.exe")
        speak("Notepad closed Sir.")

    # close word app
    elif 'close word' in name:
        speak("Closing microsoft word.")
        os.system("taskkill /f /im WINWORD.EXE")
        speak("Microsoft word has been closed Sir.")

    # close powerpoint app
    elif 'close powerpoint' in name:
        speak("Closing microsoft powerpoint.")
        os.system("taskkill /f /im POWERPNT.EXE")
        speak("Microsoft powerpoint has been  closed Sir.")

        # close excel app

    # close excel app
    elif 'close excel' in name:
        speak("Closing microsoft excel.")
        os.system("taskkill /f /im excel.exe")
        speak("microsoft excel has been closed Sir.")

    # close adobe reader
    elif 'close pdf reader' in name or 'close adobe' in name or 'close adobe reader' in name:
        speak("Closing adobe reader.")
        os.system("taskkill /f /im AcroRd32.exe")
        speak("Adobe reader closed Sir.")

    # close pycharm
    elif 'close pycharm' in name:
        speak("Closing pycharm.")
        os.system("taskkill /f /im pycharm64.exe")
        speak("pycharm closed Sir.")

    # close command prompt
    elif 'close command' in name:
        speak("Closing command prompt.")
        os.system("taskkill /f /im cmd.exe")
        speak("command prompt closed Sir.")

    # opens teams
    elif 'close outlook' in name:
        speak("Closing outlook.")
        os.system("taskkill /f /im OUTLOOK.EXE")
        speak("Outlook closed sir.")

    # close teams
    elif 'close teams' in name:
        speak("Closing microsoft teams.")
        os.system("taskkill /f /im Teams.exe")
        speak("Microsoft teams closed Sir.")

    # close microsoft edge
    elif 'close edge' in name:
        speak("Closing microsoft Edge.")
        os.system("taskkill /f /im msedge.exe")
        speak("Microsoft Edge closed Sir.")

    # close Qt Designer edge
    elif 'close designer' in name:
        speak("Closing Qt designer.")
        os.system("taskkill /f /im designer.exe")
        speak("Qt designer closed Sir.")

    # Close notepad plus
    elif 'close notepad plus' in name:
        speak("Closing Notepad plus plus.")
        os.system("taskkill /f /im notepad++.exe")
        speak("Notepad plus plus clsoed Sir.")

    # close online telegram (works)
    elif 'close online telegram' in name:
        speak("Opening telegram.")
        webbrowser.open("https://web.telegram.org/#/im?p=@selutpam01_bot")
        speak("Telegram opened Sir.")

    # close telegram (works)
    elif 'close telegram' in name:
        speak("Closing telegram.")
        os.system("taskkill /f /im Telegram.exe")
        speak("Telegram closed Sir.")

    # close chrome (works)
    elif 'close chrome' in name:
        speak("Closing chrome.")
        os.system('taskkill /f /im chrome.exe')
        speak("Chrome closed Sir.")

    # close 4kvideodownloader (works)
    elif 'close video downloader' in name:
        speak("Closing 4k video downloader.")
        os.system("taskkill /f /im 4kvideodownloader.exe")
        speak("4k video downloader closed Sir.")

    # close youtube (works)
    elif 'close youtube' in name:
        speak("Closing YouTube.")
        webbrowser.open("https://www.youtube.com/")
        speak("YouTube closed Sir.")


# temperature in Cape Town
def temperature():
    search = 'weather in cape town'
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    timer_1 = data.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    lyst = timer_1.split()
    weather1 = lyst[2]
    weather2 = lyst[3]
    total_weather = f"{weather1} {weather2}"

    speak(f"The temperature outside is currently {temp}, {total_weather}.")


# get current time
def current_time():
    c_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak(f"The current time is {c_time}")


# Get current date
def current_date():
    c_date = datetime.datetime.now().strftime("%d-%B-%Y")
    c_day = datetime.datetime.now().strftime("%A")
    speak(f"The current date is {c_day}, {c_date}.")


# Speed test
def speed_test(query):
    speak("Checking speed...")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correct_down = int(downloading / 800000)
    uploading = speed.upload()
    correct_upload = int(uploading / 800000)

    if 'uploading' in query:
        speak(f"the uploading speed is {correct_upload} mbps")

    elif 'downloading' in query:
        speak(f"the uploading speed is {correct_down} mbps")

    else:
        speak(f"The downloading speed is {correct_down} mbps and the uploading speed is "
              f"{correct_upload} mbps.")


# Email function
def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user="sodozaasenathi@gmail.com", password="Phiwenathi_2020#")
    server.sendmail("sodozaasenathi@gmail.com", to, content)
    server.close()


# function for playing music
def music():
    speak("Please tell me the name of the song")
    music_name = take_command().lower()

    if "lover" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Sponono.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "work" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Umsebenzi.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "brother" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Sbali.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "come" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Uzobuya.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "come back" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Woza.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "girls" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Banyana.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "other" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Omunye.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "love" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "uThando.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    elif "others" in music_name:
        m_dir = "C:/Users/zasodozay/Downloads/Music"
        rc = "Nabanye.mp3"
        os.startfile(os.path.join(m_dir, rc))
        speak('Playing music Sir! Enjoy!')

    else:
        pywhatkit.playonyt(music_name)
        speak('Playing music on youtube Sir! Enjoy!')


# whatsapp messages
def whatsapp():
    speak("Do you want to send it now or do you want to schedule it?")
    command = take_command()
    if 'now' in command:
        speak("Who should I send it to? Please insert the number.")
        number = input("Enter number: ")

        speak("What should I say?")
        message = take_command()

        speak("Enter the wait time in seconds you want to send the message")
        wait_time = int(input("Enter the time in minutes: "))

        pywhatkit.sendwhatmsg_instantly(phone_no=number, message=message, wait_time=wait_time)

    else:
        speak("Who should I send it to? Please insert the number.")
        number = input("Enter number: ")
        speak("What should I say?")
        message = take_command()

        speak("Enter the time in hours you want to send the message")
        time_hour = int(input("Enter the time in hours: "))

        speak("Enter the time in minutes you want to send the message")
        time_min = int(input("Enter the time in minutes: "))

        speak("Enter the wait time in seconds you want to send the message")
        wait_time = int(input("Enter the time in minutes: "))

        pywhatkit.sendwhatmsg(phone_no=number, message=message, time_hour=time_hour, time_min=time_min,
                              wait_time=wait_time)


# whatsapp automation
def whatsapp_auto():
    speak("Who should I send it to? Please insert the name of the person.")
    name = input("Enter the name: ")
    speak("What should I say?")
    # message = take_command()
    message = input("Enter the message: ")

    os.startfile("C:/Users/zasodozay/AppData/Local/WhatsApp/WhatsApp.exe")
    time.sleep(10)
    click(x=271, y=184)  # click the search box

    time.sleep(1)
    write(name)  # write the name you want to search for

    time.sleep(0.5)
    click(x=401, y=380)  # select the name

    time.sleep(0.5)
    click(x=953, y=1024)  # click to type the message

    time.sleep(0.5)
    write(message)  # type the message
    press('enter')

    speak("Message successfully sent sir")
    os.system("taskkill /f /im WhatsApp.exe")


# whatsapp call automation
def whatsapp_cal_auto():
    speak("Who should I send it to? Please insert the name of the person.")
    name = input("Enter the name: ")
    os.startfile("C:/Users/zasodozay/AppData/Local/WhatsApp/WhatsApp.exe")
    time.sleep(10)
    click(x=271, y=184)  # click the search box

    time.sleep(1)
    write(name)  # write the name you want to search for

    time.sleep(0.5)
    click(x=401, y=380)  # select the name

    time.sleep(0.5)
    click(x=1694, y=80)  # select the phone icon to make a call


# whatsapp call automation
def whatsapp_video_auto():
    speak("Who should I send it to? Please insert the name of the person.")
    name = input("Enter the name: ")
    os.startfile("C:/Users/zasodozay/AppData/Local/WhatsApp/WhatsApp.exe")
    time.sleep(10)
    click(x=271, y=184)  # click the search box

    time.sleep(1)
    write(name)  # write the name you want to search for

    time.sleep(0.5)
    click(x=401, y=380)  # select the name

    time.sleep(0.5)
    # click(x=1559, y=80)  # select the video icon to make a call
    click(x=1559, y=119)  # select the video icon to make a call


# audiobooks
def audiobooks():
    filename = askopenfilename()
    file = open(filename, 'rb')
    pdf_reader1 = PyPDF2.PdfFileReader(file)
    num = int(input("Enter Page Number: "))
    pdf_page = pdf_reader1.getPage(num)
    pdf_text = pdf_page.extractText()
    speak(pdf_text)


# chrome automation
def chrome_auto(command):
    while True:
        query = str(command)

        # open a new window
        if 'new window' in query:
            press_and_release('ctrl + n')

        # Open a new window in Incognito mode
        elif 'incognito' in query:
            press_and_release('ctrl + shift + n')

        # Open a new tab, and jump to it
        elif 'new tab' in query:
            press_and_release('ctrl + t')

        # Reopen previously closed tabs in the order they were closed
        elif 'reopen closed tab' in query:
            press_and_release('ctrl + shift + t')

        # Jump to the next open tab
        elif 'next tab' in query:
            press_and_release('ctrl + Tab')

        # Jump to the previous open tab
        elif 'previous tab' in query:
            press_and_release('ctrl + shift + Tab')

        # Open your home page in the current tab
        elif 'home page' in query:
            press_and_release('Alt + Home')

        # close current tab
        elif 'close tab' in query:
            press_and_release('ctrl + w')

        # close current window
        elif 'close window' in query:
            press_and_release('ctrl + shift')

        # Minimize the current window
        elif 'minimize window' in query:
            press_and_release('Alt + Space')
            press('n')

        # Maximize the current window
        elif 'maximize window' in query:
            press_and_release('Alt + Space')
            press('x')

        # Quit Google Chrome
        elif 'close chrome' in query:
            press_and_release('Alt + f')
            press('x')

        # Open the History page in a new tab
        elif 'show history' in query:
            press_and_release('ctrl + h')

        # Open the Downloads page in a new tab
        elif 'show downloads' in query:
            press_and_release('ctrl + j')

        # Show or hide the Bookmarks bar
        elif 'show bookmarks' in query:
            press_and_release('ctrl + shift')
            press('b')

        # Make everything on the page bigger
        elif 'resize page' in query:
            press_and_release('ctrl and +')

        # Make everything on the page smaller
        elif 'resize page' in query:
            press_and_release('ctrl and -')

        # Reset page zoom level
        elif 'resize page' in query:
            press_and_release('ctrl + 0')

        elif 'switch tab' in query:
            tab = query.replace('switch tab', '')
            Tab = tab.replace('to', '')
            num = Tab
            bb = f"ctrl + {num}"
            press_and_release(bb)
            # speak("To which tab sir?")
            # tab = take_command()
            # Tab = int(tab)
            # if '1' in Tab:
            #     press_and_release('ctrl + 1')
            #
            # elif '2' in Tab:
            #     press_and_release('ctrl + 2')
            #
            # elif '3' in Tab:
            #     press_and_release('ctrl + 3')
            #
            # elif '4' in Tab:
            #     press_and_release('ctrl + 4')
            #
            # elif '5' in Tab:
            #     press_and_release('ctrl + 5')
            #
            # elif '6' in Tab:
            #     press_and_release('ctrl + 6')
            #
            # elif '7' in Tab:
            #     press_and_release('ctrl + 7')
            #
            # elif '8' in Tab:
            #     press_and_release('ctrl + 8')
            #
            # elif '9' in Tab:
            #     press_and_release('ctrl + 9')


# reminder:
def remind_me():
    speak("What do you want me to remember sir?")
    data = take_command()
    remember = open("data.txt", "w")
    speak("You said I should remember: " + data)
    remember.write(data)
    remember.close()
