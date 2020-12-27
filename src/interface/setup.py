import sys, os
from pathlib import Path

from PyQt5 import Qt


def resourcePath(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    source = Path(r'./src/interface/resources/images')
    path = source / relative_path
    return path.as_posix()


def setupIcon(iconName, item, window=False):
    path = resourcePath(iconName)
    iconName = Qt.QIcon()
    iconName.addPixmap(Qt.QPixmap(path), Qt.QIcon.Normal,
                       Qt.QIcon.Off)
    if window:
        item.setWindowIcon(iconName)
    else:
        item.setIcon(iconName)
