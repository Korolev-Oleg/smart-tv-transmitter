from PyQt5 import Qt
from .ui.uiMain import Ui_MainWindow

from .setup import setupIcon


class Window(Qt.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__setupIcons__()

    def __setupIcons__(self):
        setupIcon('play-btn.png', self.runButton)
        setupIcon('question.png', self.actionHowTo)
