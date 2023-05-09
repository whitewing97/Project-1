from PyQt5.QtWidgets import *
from view import *
from view import Ui_Remote

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_Remote):
    MIN_VOLUME = 0
    MAX_VOLUME = 3
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, *args, **kwargs) -> None:
        """
        Function connects the buttons to their respective function.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.power_button.clicked.connect(lambda: self.power())
        self.Mute_button.clicked.connect(lambda: self.mute())
        self.Volume_up_button.clicked.connect(lambda: self.volume_up())
        self.Volume_down_button.clicked.connect(lambda: self.volume_down())
        self.Channel_up_button.clicked.connect(lambda: self.channel_up())
        self.Channel_down_button.clicked.connect(lambda: self.channel_down())
        self.__status = False
        self.__muted = False
        self.__volume = Controller.MIN_VOLUME
        self.__channel = Controller.MIN_CHANNEL
        
    def channel_check(self) -> None:
        """
        Function determines what channel user is on.
        """
        if self.__status == True:
            if self.__channel == 0:
                self.Channel_0.setHidden(False)
                self.Channel_1.setHidden(True)
                self.Channel_2.setHidden(True)
                self.Channel_3.setHidden(True)
            elif self.__channel == 1:
                self.Channel_0.setHidden(True)
                self.Channel_1.setHidden(False)
                self.Channel_2.setHidden(True)
                self.Channel_3.setHidden(True)
            elif self.__channel == 2:
                self.Channel_0.setHidden(True)
                self.Channel_1.setHidden(True)
                self.Channel_2.setHidden(False)
                self.Channel_3.setHidden(True)
            else:
                self.Channel_0.setHidden(True)
                self.Channel_1.setHidden(True)
                self.Channel_2.setHidden(True)
                self.Channel_3.setHidden(False)

    def power(self) -> None:
        """
        Function determines whether or not hte power is on or off.
        :return:
        """
        self.__status = not self.__status
        if self.__status == False:
            self.power_off_image.setHidden(False)            
        else:
            self.power_off_image.setHidden(True)


    def channel_up(self) -> None:
        """
        Function controls the channel up button and cycles through the channels.
        """
        if self.__status:
            if self.__channel < Controller.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Controller.MIN_CHANNEL
        Controller.channel_check(self)
        

    def channel_down(self):
        """
        Function controls the channel down button and cycles through the channels.
        """
        if self.__status:
            if self.__channel > Controller.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Controller.MAX_CHANNEL
        Controller.channel_check(self)

    def volume_up(self) -> None:
        """
        Function controls the volume up button and moves the volume status bar.
        """
        if self.__status:
            if self.__volume < Controller.MAX_VOLUME:
                self.__volume += 1
                self.volume_status.setValue(self.__volume)
                if self.__muted:
                    self.__muted = False

    def volume_down(self) -> None:
        """
        Function controls the volume down button and moves the volume status bar.
        """
        if self.__status:
            if self.__volume > Controller.MIN_VOLUME:
                self.__volume -= 1
                self.volume_status.setValue(self.__volume)
                if self.__muted:
                    self.__muted = False


    def mute(self) -> None:
        """
        Function determines mute status and disables interactivity with volume buttons.
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.Volume_up_button.setEnabled(False)
                self.Volume_down_button.setEnabled(False)
                self.volume_status.setEnabled(False)
                self.volume_status.setValue(0)
            else:
                self.Volume_up_button.setEnabled(True)
                self.Volume_down_button.setEnabled(True)
                self.volume_status.setEnabled(True)
                self.volume_status.setValue(self.__volume)