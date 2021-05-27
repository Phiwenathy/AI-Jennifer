import random
import keyboard
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes
import wikipedia
from tkinter import *
from pytube import YouTube  # pip install pytube
from tkinter import messagebox, filedialog
import pathlib
from Functions import *


def task_execution():
    start_up()
    while True:
        query = take_command()
        if 'hello' in query:
            speak("hello sir, Jennifer at your service.")

        elif "temperature" in query:
            temperature()

        elif 'time' in query:
            current_time()

        elif 'date' in query:
            current_date()

        elif 'send whatsapp' in query:
            whatsapp()

        elif 'send message' in query:
            whatsapp_auto()

        elif 'whatsapp call' in query:
            whatsapp_cal_auto()

        elif 'video call' in query:
            whatsapp_video_auto()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence=2)
            speak(f"wikipedia says: \n{result}")

        elif 'offline' in query:
            close_sys()

        # playing music that is in the desktop
        elif 'play music' in query or 'play a song' in query:
            music()

        # make a note
        elif "make a note" in query or "write this down" in query or "remember this" in query:
            speak("What would you like me to write down?")
            text1 = take_command()
            make_note(text1)
            speak("I've made a note of that sir")

        # close note
        elif "close the note" in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad++.exe")

        # Asking how are you
        elif 'how are you' in query or 'how’s everything' in query or 'how is everything' in query \
                or 'how’s it going' in query or 'how are things' in query or 'you all right' in query \
                or 'What’s new' in query or 'what’s up' in query or 'how are you doing' in query \
                or 'how have you been' in query or 'how are things going' in query or 'are you well' in query:
            responses = ["I’m fine sir, thank you. how about you?", "I’m good. how have you been?",
                         "Pretty good, how are things going?", "I’m well. what's up?",
                         "Yeah, all right. you all right sir?", "Not too bad. How's it going on your side?",
                         "Same old, same old. what's new?"]
            speak(random.choice(responses))

        # tell me about yourself
        elif 'about yourself' in query or 'who are you' in query:
            speak("I am a virtual artificial intelligence assistant named Jennifer for Mr Sodoza."
                  "\nI am a work in progress,like anything else, the ingredients for success are hard work, "
                  "time and a positive attitude, so I have no doubt that my maker will strive for me to be "
                  "able to think on my own.\nOn a serious note though, I can open and close programs such "
                  "as notepad, adobe reader, command prompt, camera, powerpoint, excel, and word.\nI can "
                  "also search using google or wikipedia, play music that is in your desktop or play videos"
                  " on youtube.\nI am able to open online websites such as stackoverflow, facebook, and "
                  "gmail.\nI can create a note for you in notepad, send email, or send whatsapp message."
                  "\nI am also able to open specific folders of your choice, for example opening Documents "
                  "folder.\nI am not limited to these tasks only, I can do other things like telling jokes, "
                  "and so on. Anyway that's not what I am here for.")

        elif "fine" in query or "good" in query:
            speak("It's good to know that you are fine")

        # Google search
        elif 'search google for' in query:
            query = query.replace('jennifer', "")
            query = query.replace('search Google for', "")
            speak(f"Okay sir, searching google for {query}, please wait while I get the information")
            web = f"https://www.google.com/search?q={query}"
            webbrowser.open(web)
            speak("Done sir, tHere is what I found on google for your search Sir")

            # closing the assistant

        # Youtube search
        elif 'search youtube for' in query:
            speak(f"Searching YouTube for {query}, please wait while I get the information")
            query = query.replace('john', "")
            query = query.replace('search youtube for', "")
            web = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(web)
            speak("Done sir, Here is what I found on youtube for your search Sir.")

        # opening any website
        elif 'open website' in query:
            speak("Which site do you want me to open sir?")
            query = take_command().lower()
            query = query.replace(" ", "")
            web1 = f"https://www.{query}.com"
            webbrowser.open(web1)
            speak("Website launched!")

        # taking screenshot

        elif 'screenshot' in query:
            screenshot()

        elif 'whatsapp' in query:
            whatsapp()

        # shut down the system
        elif "shut down the system" in query:
            speak('Shutting down the system sir. Goodbye.')
            os.system("shutdown /s /t 5")

        # restart the system
        elif "restart the system" in query:
            speak('Restarting the system sir.')
            os.system("shutdown /r /t 5")

        # sleep the system
        elif "sleep the system" in query:
            speak('suspending the system sir.')
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

        # Gratitude
        elif 'thank you' in query or 'thanks' in query or 'you are awesome' in query:
            stmsgs = ['You are welcome Sir.', "It's my pleasure sir.", "I'm happy to do it sir.",
                      "No problem sir."]
            speak(random.choice(stmsgs))

        # tell a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # System Space used
        elif 'space used' in query:
            vm = psutil.virtual_memory()
            lists = []
            for it in vm:
                lists.append(it)

            used = lists[3]
            used_1 = str(round(used / (1024 * 1024 * 1024), 3))
            speak(f"The total space used for the system is {used_1} Gigabytes sir.")

        # System Space available
        elif 'space available' in query:
            vm_1 = psutil.virtual_memory()
            vm_lists = []
            for it in vm_1:
                vm_lists.append(it)

            available = vm_lists[1]
            available_1 = str(round(available / (1024 * 1024 * 1024), 3))
            speak(f"The total space available for the system is {available_1} Gigabytes sir.")

        # close apps
        elif 'close application' in query:
            close_apps()

        # opens notepad
        if 'open system notepad' in query:
            query = 'open system notepad'
            open_apps(query)

        # opens pycharm
        if 'open pycharm' in query:
            query = 'open pycharm'
            open_apps(query)

        # open word app
        elif 'open word' in query:
            query = 'open word'
            open_apps(query)

        # open powerpoint app
        elif 'open powerpoint' in query:
            query = 'open powerpoint'
            open_apps(query)

        # open excel app
        elif 'open excel' in query:
            query = 'open excel'
            open_apps(query)

        # opens adobe reader
        elif 'open pdf reader' in query:
            query = 'open pdf reader'
            open_apps(query)

        # opens command prompt
        elif 'open command' in query or 'open command prompt' in query:
            query = 'open command'
            open_apps(query)

        # opens teams
        elif 'open outlook' in query:
            query = 'open outlook'
            open_apps(query)

        # opens teams
        elif 'open teams' in query:
            query = 'open teams'
            open_apps(query)

        # opens microsoft edge
        elif 'open edge' in query:
            query = 'open edge'
            open_apps(query)

        # opens Qt Designer edge
        elif 'open designer' in query:
            query = 'open designer'
            open_apps(query)

        # opens notepad plus
        elif 'open notepad plus' in query:
            query = 'open notepad plus'
            open_apps(query)

        # restart a video/music
        elif 'restart' in query:
            keyboard.press('0')

        # next a video/music
        elif 'next' in query or 'skip' in query:
            keyboard.press('1')

        # back a video/music
        elif 'back' in query:
            keyboard.press('j')

        # mute a video/music
        elif 'mute' in query:
            keyboard.press('m')

        # full screen a video/music
        elif 'full screen' in query:
            keyboard.press('f')

        # film mode a video/music
        elif 'film mode' in query:
            keyboard.press('t')

        # restart a video/music
        elif 'pause' in query or 'stop' in query:
            keyboard.press('k')

        # switching windows
        elif 'switch window' in query:
            speak("Switching windows.")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("Windows switched sir")

        # closing current tab of the browser
        if 'close this tab' in query:
            keyboard.press('ctrl + w')

        # opening new tab of the browser
        elif 'open new tab' in query:
            keyboard.press('ctrl + t')

        # opening new window of the browser
        elif 'open new window' in query:
            keyboard.press('ctrl + n')

        # youtube video download
        elif 'download video' in query:
            # Defining CreateWidgets() function
            # to create necessary tkinter widgets
            def Widgets():
                link_label = Label(root, text="YouTube link :", bg="#E8D579", width=20)
                link_label.grid(row=1, column=0, pady=5, padx=5)

                linkText = Entry(root, width=50, textvariable=video_Link)
                linkText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

                destination_label = Label(root, text="Destination :", bg="#E8D579", width=20)
                destination_label.grid(row=2, column=0, pady=5, padx=5)

                destinationText = Entry(root, width=40, textvariable=download_Path)
                destinationText.grid(row=2, column=1, pady=5, padx=5)

                browse_B = Button(root, text="Browse", command=Browse, width=10, bg="#05E8E0")
                browse_B.grid(row=2, column=2, pady=1, padx=1)

                Download_B = Button(root, text="Download", command=Download, width=20, bg="#05E8E0")
                Download_B.grid(row=3, column=1, pady=3, padx=3)

            # Defining Browse() to select a
            # destination folder to save the video
            def Browse():
                download_Directory = filedialog.askdirectory(initialdir=pathlib.Path.cwd())
                # Displaying the directory in the directory
                # textbox
                download_Path.set(download_Directory)

            # Defining Download() to download the video
            def Download():
                # getting user-input Youtube Link
                Youtube_link = video_Link.get()
                # select the optimal location for
                # saving file's
                download_Folder = download_Path.get()
                # Creating object of YouTube()
                getVideo = YouTube(Youtube_link)
                # Getting all the available streams of the
                # youtube video and selecting the first
                # from the
                videoStream = getVideo.streams.first()
                # Downloading the video to destination
                # directory
                videoStream.download(download_Folder)
                # Displaying the message
                messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n"
                                    + download_Folder)

            # Creating object of tk class
            root = Tk()
            root.geometry("700x300")
            root.resizable()
            root.title("YouTube Video Downloader")
            root.config(background="#000000")
            # Creating the tkinter Variables
            video_Link = StringVar()
            download_Path = StringVar()
            # Calling the Widgets() function
            Widgets()
            root.mainloop()

            speak("Video downloaded")

        # checking downloading speed

        elif 'downloading speed' in query:
            query = 'downloading'
            speed_test(query)

        # checking uploading speed
        elif 'uploading speed' in query:
            query = 'uploading'
            speed_test(query)

        # checking internet speed
        elif 'internet speed' in query:
            query = 'internet speed'
            speed_test(query)

        elif 'goodbye' in query or 'go to sleep' in query or 'you can sleep' in \
                query or 'bye' in query:
            close_sys()

        elif 'send email' in query:
            try:
                speak("Who should I send it to?")
                to_addr = input("Message: ")
                speak("What should I say?")
                email_body = take_command()
                send_email(to_addr, email_body)
                speak("The email is sent successfully")
            except Exception as e:
                print(F"Exception: {str(e)}")
                speak("Unable to send email at the moment sir.")

        elif 'remember this' in query or 'remember that' in query:
            remind_me()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You said I should remember: " + remember.read())

        elif 'battery' in query:
            battery = psutil.sensors_battery().percent
            speak(f"the current battery life is {battery}%")

        elif 'chrome' in query:
            chrome_auto(query)

        speak("Please tell me how can I help you?")
