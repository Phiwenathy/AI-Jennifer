import datetime
import os
import webbrowser
import psutil
from jenniferui import UiJenniferWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import main


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        main.task_execution()


startFunctions = MainThread()


class GuiStart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = UiJenniferWindow()
        self.gui.setupUi(self)

        self.gui.stop_button.clicked.connect(self.close)
        self.gui.start_button.clicked.connect(self.startTask)
        self.gui.cmd_button.clicked.connect(self.cmd_app)
        self.gui.telegram_button.clicked.connect(self.telegram_app)
        self.gui.teams_button.clicked.connect(self.teams_app)
        self.gui.notepadplus_button.clicked.connect(self.notepadplus_app)
        self.gui.youtube_button.clicked.connect(self.youtube_app)
        self.gui.word_button.clicked.connect(self.word_app)
        self.gui.excel_button.clicked.connect(self.excel_app)
        self.gui.powerpoint_button.clicked.connect(self.powerpoint_app)
        self.gui.snip_tool_button.clicked.connect(self.edge_app)
        self.gui.pycharm_button.clicked.connect(self.pycharm_app)

        self.startTime()
        self.startSpeed()

    def cmd_app(self):
        main.speak("Opening command prompt plus.")
        os.system("Start cmd")
        main.speak("Command prompt plus plus opened Sir.")

    def notepadplus_app(self):
        t_path = "C:/Program Files (x86)/Notepad++/notepad++.exe"
        main.speak("Opening notepad plus plus.")
        os.startfile(t_path)
        main.speak("Notepad plus plus opened Sir.")

    def telegram_app(self):
        path = "C:/Users/zasodozay/AppData/Roaming/Telegram Desktop/Telegram.exe"
        main.speak("Opening telegram.")
        os.startfile(path)
        main.speak("Telegram opened Sir.")

    def word_app(self):
        main.speak('opening microsoft word.')
        os.system('start WINWORD.EXE')
        main.speak('microsoft word has been opened sir.')

    def excel_app(self):
        main.speak('opening microsoft excel.')
        os.system('start excel.exe')
        main.speak('microsoft excel has been opened sir.')

    def teams_app(self):
        t_path = "C:/Users/zasodozay/AppData/Local/Microsoft/Teams/current/Teams.exe"
        main.speak("Opening microsoft teams.")
        os.startfile(t_path)
        main.speak("Microsoft teams opened Sir.")

    def edge_app(self):
        t_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        main.speak("Opening Microsoft Edge.")
        os.startfile(t_path)
        main.speak("Microsoft Edge opened Sir.")

    def pycharm_app(self):
        t_path = "C:/Program Files/JetBrains/PyCharm 2020.2.3/bin/pycharm64.exe"
        main.speak("Opening Pycharm.")
        os.startfile(t_path)
        main.speak("Pycharm opened Sir.")

    def powerpoint_app(self):
        main.speak('Opening microsoft powerpoint.')
        os.system('start POWERPNT.EXE')
        main.speak('microsoft powerpoint has been opened sir.')

    def youtube_app(self):
        main.speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com/")
        main.speak("YouTube opened Sir.")

    def startTask(self):
        startFunctions.start()

    def startTime(self):
        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

    def showTimeLive(self):
        t_time = datetime.datetime.now().strftime('%I:%M:%S %p')
        d_date = datetime.datetime.today().strftime('%d %B %Y')
        day = datetime.datetime.today().strftime('%A')
        date = f"{day}, {d_date}"
        self.gui.time_value.setText(t_time)
        self.gui.date_value.setText(date)

    def showSpace(self):
        disk = psutil.disk_usage('/').percent
        ram = psutil.virtual_memory().percent
        swap = psutil.swap_memory().percent
        battery_percent = psutil.sensors_battery().percent
        vm = psutil.virtual_memory()
        lists = []
        for it in vm:
            lists.append(it)
        used = lists[3]
        used_1 = str(round(used / (1024 * 1024 * 1024), 3))
        available = vm[1]
        available_1 = str(round(available / (1024 * 1024 * 1024), 3))

        self.gui.free_space_value.setText(f"Free Space: {available_1} GB")
        self.gui.space_used_value.setText(f"Used Space: {used_1} GB")
        self.gui.cpu_value.setText(f"Disk Used: {disk}%")
        self.gui.ram_value.setText(f"RAM Used: {ram}%")
        self.gui.swap_value.setText(f"SWAP Used: {swap}%")
        self.gui.battery_value.setText(f"Battery Life: {battery_percent}%")

    def startSpeed(self):
        times = QTimer(self)
        times.timeout.connect(self.showSpace)
        times.start(1200)


GuiApp = QApplication(sys.argv)
jen_gui = GuiStart()
jen_gui.show()
exit(GuiApp.exec_())
