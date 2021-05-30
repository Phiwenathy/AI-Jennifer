from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QMovie, QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class UiJenniferWindow(object):
    def setupUi(self, jennifer_window):
        jennifer_window.setObjectName("Sam_Window")
        jennifer_window.setGeometry(98, 50, 1810, 1020)
        jennifer_window.setWindowTitle('John Virtual Artificial Intelligence')
        jennifer_window.setWindowIcon(QIcon('../photos/jennifer ui/Icon.png'))
        self.centralwidget = QtWidgets.QWidget(jennifer_window)
        self.centralwidget.setObjectName("centralwidget")

        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setColor(QColor("#ffffff"))
        shadow_effect.setOffset(1, 1)

        # background label
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1810, 1020))
        self.background_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/background-image.jpg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")

        # loading label
        self.loading_label = QtWidgets.QLabel(self.centralwidget)
        self.loading_label.setGeometry(QtCore.QRect(0, 175, 310, 100))
        self.loading_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/load.gif"))
        self.loading_label.setScaledContents(True)
        self.loading_label.setObjectName("loading_label")
        self.loading_movie = QMovie('../photos/jennifer ui/load.gif')
        self.loading_label.setMovie(self.loading_movie)

        # date info
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(10, 70, 300, 100))
        self.date_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/element.jpg"))
        self.date_label.setScaledContents(True)
        self.date_label.setObjectName("date_label")

        self.date_value = QtWidgets.QLabel(self.centralwidget)
        self.date_value.setGeometry(QtCore.QRect(10, 75, 290, 90))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.date_value.setFont(font)
        self.date_value.setStyleSheet("color: #00BFFF;background-color:transparent;")
        self.date_value.setAlignment(QtCore.Qt.AlignCenter)
        self.date_value.setWordWrap(True)
        self.date_value.setGraphicsEffect(shadow_effect)
        self.date_value.setObjectName("date_value")

        # time info
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(10, 280, 300, 100))
        self.time_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/element.jpg"))
        self.time_label.setScaledContents(True)
        self.time_label.setObjectName("time_label")

        self.time_value = QtWidgets.QLabel(self.centralwidget)
        self.time_value.setGeometry(QtCore.QRect(20, 285, 290, 90))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.time_value.setFont(font)
        self.time_value.setStyleSheet("color: #00BFFF;background-color:transparent;")
        self.time_value.setObjectName("time_value")
        self.time_value.setAlignment(QtCore.Qt.AlignCenter)
        self.time_value.setWordWrap(True)
        self.time_value.setGraphicsEffect(shadow_effect)

        # temperature info
        self.temperature_label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_label.setGeometry(QtCore.QRect(10, 390, 300, 100))
        self.temperature_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/element.jpg"))
        self.temperature_label.setScaledContents(True)
        self.temperature_label.setObjectName("temperature_label")

        self.temperature_value = QtWidgets.QLabel(self.centralwidget)
        self.temperature_value.setGeometry(QtCore.QRect(30, 395, 290, 90))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.temperature_value.setFont(font)
        self.temperature_value.setStyleSheet("color: #00BFFF;background-color:transparent;")
        self.temperature_value.setObjectName("temperature_value")
        self.temperature_value.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_value.setWordWrap(True)
        self.temperature_value.setGraphicsEffect(shadow_effect)

        # voice label
        self.voice_label = QtWidgets.QLabel(self.centralwidget)
        self.voice_label.setGeometry(QtCore.QRect(10, 520, 300, 200))
        self.voice_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/voice.gif"))
        self.voice_label.setScaledContents(True)
        self.voice_label.setObjectName("voice_label")
        self.voice_movie = QMovie('../photos/jennifer ui/voice.gif')
        self.voice_label.setMovie(self.voice_movie)

        # apps info
        self.teams_button = QtWidgets.QPushButton(self.centralwidget)
        self.teams_button.setGeometry(QtCore.QRect(340, 90, 105, 105))
        self.teams_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/teams.png);\nborder:none;"
            "\nbackground-repeat: no-repeat;")
        self.teams_button.setText("")
        self.teams_button.setObjectName("teams_button")

        self.cmd_button = QtWidgets.QPushButton(self.centralwidget)
        self.cmd_button.setGeometry(QtCore.QRect(340, 210, 105, 105))
        self.cmd_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/cmd.png);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.cmd_button.setText("")
        self.cmd_button.setObjectName("cmd_button")

        self.word_button = QtWidgets.QPushButton(self.centralwidget)
        self.word_button.setGeometry(QtCore.QRect(340, 330, 105, 105))
        self.word_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/word.png);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.word_button.setText("")
        self.word_button.setObjectName("word_button")

        self.powerpoint_button = QtWidgets.QPushButton(self.centralwidget)
        self.powerpoint_button.setGeometry(QtCore.QRect(340, 450, 105, 105))
        self.powerpoint_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/powerpoint.png);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.powerpoint_button.setText("")
        self.powerpoint_button.setObjectName("powerpoint_button")

        self.notepadplus_button = QtWidgets.QPushButton(self.centralwidget)
        self.notepadplus_button.setGeometry(QtCore.QRect(340, 570, 105, 105))
        self.notepadplus_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/notepad_plus.png);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.notepadplus_button.setText("")
        self.notepadplus_button.setObjectName("notepadplus_button")

        self.snip_tool_button = QtWidgets.QPushButton(self.centralwidget)
        self.snip_tool_button.setGeometry(QtCore.QRect(290, 690, 105, 105))
        self.snip_tool_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/edge.jpg);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.snip_tool_button.setText("")
        self.snip_tool_button.setObjectName("snip_tool_button")

        self.excel_button = QtWidgets.QPushButton(self.centralwidget)
        self.excel_button.setGeometry(QtCore.QRect(500, 90, 105, 105))
        self.excel_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/excel.png);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.excel_button.setText("")
        self.excel_button.setObjectName("excel_button")

        self.youtube_button = QtWidgets.QPushButton(self.centralwidget)
        self.youtube_button.setGeometry(QtCore.QRect(500, 210, 105, 105))
        self.youtube_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/youtube.png);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.youtube_button.setText("")
        self.youtube_button.setObjectName("youtube_button")

        self.telegram_button = QtWidgets.QPushButton(self.centralwidget)
        self.telegram_button.setGeometry(QtCore.QRect(500, 330, 105, 105))
        self.telegram_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/telegram.png);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.telegram_button.setText("")
        self.telegram_button.setObjectName("telegram_button")
        jennifer_window.setCentralWidget(self.centralwidget)

        self.pycharm_button = QtWidgets.QPushButton(self.centralwidget)
        self.pycharm_button.setGeometry(QtCore.QRect(500, 450, 105, 105))
        self.pycharm_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/pycharm.jpg);\nbackground-size: cover;"
            "\nbackground-repeat: no-repeat;\nborder: none;")
        self.pycharm_button.setText("")
        self.pycharm_button.setObjectName("pycharm_button")

        # Lara2 rotating
        self.lara2_label = QtWidgets.QLabel(self.centralwidget)
        self.lara2_label.setGeometry(QtCore.QRect(630, 170, 250, 400))
        self.lara2_label.setText("")
        self.lara2_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/lara2.gif"))
        self.lara2_label.setScaledContents(True)
        self.lara2_label.setObjectName("lara2_label")
        self.lara2_movie = QMovie('../photos/jennifer ui/lara2.gif')
        self.lara2_label.setMovie(self.lara2_movie)

        # jennifer label
        self.jennifer_label = QtWidgets.QLabel(self.centralwidget)
        self.jennifer_label.setGeometry(QtCore.QRect(890, 170, 250, 400))
        self.jennifer_label.setText("")
        self.jennifer_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/anime.gif"))
        self.jennifer_label.setScaledContents(True)
        self.jennifer_label.setObjectName("jennifer_label")
        self.jennifer_movie = QMovie('../photos/jennifer ui/anime.gif')
        self.jennifer_label.setMovie(self.jennifer_movie)

        self.jennifer_value = QtWidgets.QLabel(self.centralwidget)
        self.jennifer_value.setGeometry(QtCore.QRect(830, 440, 250, 100))
        self.jennifer_value.setText("Jennifer \nAI Assistant")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(95)
        self.jennifer_value.setFont(font)
        self.jennifer_value.setStyleSheet("color: blue; background-color:transparent;")
        self.jennifer_value.setObjectName("jennifer_value")
        self.jennifer_value.setAlignment(QtCore.Qt.AlignCenter)
        self.jennifer_value.setWordWrap(True)
        self.jennifer_value.setGraphicsEffect(shadow_effect)

        # Lara3 rotating
        self.lara3_label = QtWidgets.QLabel(self.centralwidget)
        self.lara3_label.setGeometry(QtCore.QRect(1150, 170, 250, 400))
        self.lara3_label.setText("")
        self.lara3_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/lara3.gif"))
        self.lara3_label.setScaledContents(True)
        self.lara3_label.setObjectName("lara3_label")
        self.lara3_movie = QMovie('../photos/jennifer ui/lara3.gif')
        self.lara3_label.setMovie(self.lara3_movie)

        # lara rotating
        self.ironman_label = QtWidgets.QLabel(self.centralwidget)
        self.ironman_label.setGeometry(QtCore.QRect(1550, 370, 250, 400))
        self.ironman_label.setText("")
        self.ironman_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/lara4.gif"))
        self.ironman_label.setScaledContents(True)
        self.ironman_label.setObjectName("ironman_label")
        self.ironman_movie = QMovie('../photos/jennifer ui/lara4.gif')
        self.ironman_label.setMovie(self.ironman_movie)

        # Battery Info
        self.battery_label = QtWidgets.QLabel(self.centralwidget)
        self.battery_label.setGeometry(QtCore.QRect(600, 70, 300, 100))
        self.battery_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/element2.png"))
        self.battery_label.setScaledContents(True)
        self.battery_label.setObjectName("battery_label")

        self.battery_value = QtWidgets.QLabel(self.centralwidget)
        self.battery_value.setGeometry(QtCore.QRect(650, 100, 201, 31))
        self.battery_value.setStyleSheet("color: #00BFFF;background-color:transparent;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.battery_value.setFont(font)
        self.battery_value.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_value.setWordWrap(True)
        self.battery_value.setObjectName("battery_value")

        # swap percentage
        self.swap_label = QtWidgets.QLabel(self.centralwidget)
        self.swap_label.setGeometry(QtCore.QRect(850, 70, 300, 100))
        self.swap_label.setText("")
        self.swap_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/element2.png"))
        self.swap_label.setScaledContents(True)
        self.swap_label.setObjectName("swap_label")

        self.swap_value = QtWidgets.QLabel(self.centralwidget)
        self.swap_value.setGeometry(QtCore.QRect(900, 100, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.swap_value.setFont(font)
        self.swap_value.setText("")
        self.swap_value.setAlignment(QtCore.Qt.AlignCenter)
        self.swap_value.setWordWrap(True)
        self.swap_value.setObjectName("swap_value")
        font.setPointSize(8)
        self.swap_value.setStyleSheet("color: #00BFFF;background-color:transparent;")

        # Ram percentage info
        self.ram_label = QtWidgets.QLabel(self.centralwidget)
        self.ram_label.setGeometry(QtCore.QRect(1100, 70, 300, 100))
        self.ram_label.setText("")
        self.ram_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/element2.png"))
        self.ram_label.setScaledContents(True)
        self.ram_label.setObjectName("ram_label")

        self.ram_value = QtWidgets.QLabel(self.centralwidget)
        self.ram_value.setGeometry(QtCore.QRect(1150, 100, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ram_value.setFont(font)
        self.ram_value.setText("")
        self.ram_value.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_value.setWordWrap(True)
        self.ram_value.setObjectName("ram_value")
        font.setPointSize(8)
        self.ram_value.setStyleSheet("color: #00BFFF;background-color:transparent;")

        # CPU percentage info
        self.cpu_label = QtWidgets.QLabel(self.centralwidget)
        self.cpu_label.setGeometry(QtCore.QRect(1350, 70, 300, 100))
        self.cpu_label.setText("")
        self.cpu_label.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/element2.png"))
        self.cpu_label.setScaledContents(True)
        self.cpu_label.setObjectName("cpu_label")

        self.cpu_value = QtWidgets.QLabel(self.centralwidget)
        self.cpu_value.setGeometry(QtCore.QRect(1400, 100, 201, 31))
        self.cpu_value.setStyleSheet("color: #00BFFF;background-color:transparent;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.cpu_value.setFont(font)
        self.cpu_value.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_value.setWordWrap(True)
        self.cpu_value.setObjectName("cpu_value")

        # start button
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(685, 910, 100, 100))
        self.start_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/startbutton.png);\nborder:none;"
            "\nbackground-repeat: no-repeat;")
        self.start_button.setText("")
        self.start_button.setObjectName("start_button")

        # pause button
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(850, 910, 100, 100))
        self.pause_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/pausebutton.png);\nborder:none;"
            "\nbackground-repeat: no-repeat;")
        self.pause_button.setText("")
        self.pause_button.setObjectName("pause_button")

        # stop button
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(1030, 915, 100, 100))
        self.stop_button.setStyleSheet(
            "background-image: url(../photos/jennifer ui/stopbutton.png);\nborder:none;"
            "\nbackground-repeat: no-repeat;")
        self.stop_button.setText("")
        self.stop_button.setObjectName("stop_button")

        # download speed info
        self.download_label = QtWidgets.QLabel(self.centralwidget)
        self.download_label.setGeometry(QtCore.QRect(490, 670, 70, 70))
        self.download_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/download.png"))
        self.download_label.setScaledContents(True)
        self.download_label.setObjectName("download_label")

        self.download_value = QtWidgets.QLabel(self.centralwidget)
        self.download_value.setGeometry(QtCore.QRect(535, 680, 120, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(8)
        font.setWeight(25)
        self.download_value.setFont(font)
        self.download_value.setStyleSheet("color: rgb(85, 255, 255);")
        self.download_value.setAlignment(QtCore.Qt.AlignCenter)
        self.download_value.setWordWrap(True)
        self.download_value.setObjectName("download_value")

        # upload speed info
        self.upload_label = QtWidgets.QLabel(self.centralwidget)
        self.upload_label.setGeometry(QtCore.QRect(1150, 670, 70, 70))
        self.upload_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/upload.png"))
        self.upload_label.setScaledContents(True)
        self.upload_label.setObjectName("upload_label")

        self.upload_value = QtWidgets.QLabel(self.centralwidget)
        self.upload_value.setGeometry(QtCore.QRect(1195, 680, 120, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(8)
        font.setWeight(25)
        self.upload_value.setFont(font)
        self.upload_value.setText("6 mbps")
        self.upload_value.setStyleSheet("color: rgb(85, 255, 255);")
        self.upload_value.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_value.setWordWrap(True)
        self.upload_value.setObjectName("upload_value")

        # ram info
        self.ram_space_label = QtWidgets.QLabel(self.centralwidget)
        self.ram_space_label.setGeometry(QtCore.QRect(880, 710, 70, 70))
        self.ram_space_label.setText("")
        self.ram_space_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/ram.png"))
        self.ram_space_label.setScaledContents(True)
        self.ram_space_label.setObjectName("ram_space_label")

        self.space_used_value = QtWidgets.QLabel(self.centralwidget)
        self.space_used_value.setGeometry(QtCore.QRect(770, 710, 120, 50))
        self.space_used_value.setObjectName("space_used_value")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.space_used_value.setFont(font)
        self.space_used_value.setStyleSheet("color: #00BFFF;background-color:transparent;")
        self.space_used_value.setAlignment(QtCore.Qt.AlignCenter)
        self.space_used_value.setWordWrap(True)

        self.free_space_value = QtWidgets.QLabel(self.centralwidget)
        self.free_space_value.setGeometry(QtCore.QRect(940, 710, 120, 50))
        self.free_space_value.setObjectName("free_space_value")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.free_space_value.setFont(font)
        self.free_space_value.setStyleSheet("color: #00BFFF;background-color:transparent;")
        self.free_space_value.setAlignment(QtCore.Qt.AlignCenter)
        self.free_space_value.setWordWrap(True)

        # User info
        self.usercard_label = QtWidgets.QLabel(self.centralwidget)
        self.usercard_label.setGeometry(QtCore.QRect(1625, 70, 180, 300))
        self.usercard_label.setText("")
        self.usercard_label.setPixmap(QtGui.QPixmap("../photos/jennifer ui/card.jpg"))
        self.usercard_label.setScaledContents(True)
        self.usercard_label.setObjectName("usercard_label")

        self.user_value = QtWidgets.QLabel(self.centralwidget)
        self.user_value.setGeometry(QtCore.QRect(1665, 140, 100, 100))
        self.user_value.setText("")
        self.user_value.setPixmap(QtGui.QPixmap(
            "../photos/jennifer ui/my-profile.jpg"))
        self.user_value.setScaledContents(True)
        self.user_value.setObjectName("user_value")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1660, 245, 100, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(8)
        font.setWeight(25)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1660, 260, 110, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(8)
        font.setWeight(25)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.loading_movie.start()
        self.voice_movie.start()
        self.ironman_movie.start()
        self.jennifer_movie.start()
        self.lara2_movie.start()
        self.lara3_movie.start()

        self.retranslateUi(jennifer_window)
        QtCore.QMetaObject.connectSlotsByName(jennifer_window)

    def retranslateUi(self, jennifer_window):
        _translate = QtCore.QCoreApplication.translate
        jennifer_window.setWindowTitle(_translate("Sam_Window", "MainWindow"))
        self.download_value.setText(_translate("Sam_Window", "5 mbps"))
        self.upload_value.setText(_translate("Sam_Window", "6 mbps"))
        self.label.setText(_translate("Sam_Window", "Yanga Sodoza"))
        self.label_2.setText(_translate("Sam_Window", "Solutions Administrator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sam_Window = QtWidgets.QMainWindow()
    ui = UiJenniferWindow()
    ui.setupUi(Sam_Window)
    Sam_Window.show()
    sys.exit(app.exec_())
