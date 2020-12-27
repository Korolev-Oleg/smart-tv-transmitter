import sys

from PyQt5 import Qt
from src.interface import uxMain


def main():
    app = Qt.QApplication(sys.argv)
    window = uxMain.Window()
    window.show()
    sys.exit(
        app.exec_()
    )


if __name__ == '__main__':
    main()
