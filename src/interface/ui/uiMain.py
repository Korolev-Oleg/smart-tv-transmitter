# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 322)
        MainWindow.setMinimumSize(QtCore.QSize(529, 322))
        MainWindow.setMaximumSize(QtCore.QSize(529, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setMouseTracking(False)
        self.label.setScaledContents(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setToolTip("Вставьте скопированный html код видео")
        self.plainTextEdit.setToolTipDuration(-1)
        self.plainTextEdit.setStyleSheet("border: solid 1px;\n"
"color: #535a60;")
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 3, 0, 1, 7)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setMinimumSize(QtCore.QSize(212, 0))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setStyleSheet("font: Arial;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"color: #5d5d5d;\n"
"border: none;\n"
"background: none;\n"
"background-color: none;")
        self.label_2.setText("")
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setMinimumSize(QtCore.QSize(39, 33))
        self.runButton.setMaximumSize(QtCore.QSize(27, 42))
        self.runButton.setBaseSize(QtCore.QSize(0, 0))
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runButton.setStyleSheet("border-radius: 100px;")
        self.runButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/images/paly-btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon)
        self.runButton.setIconSize(QtCore.QSize(47, 54))
        self.runButton.setCheckable(False)
        self.runButton.setAutoRepeat(False)
        self.runButton.setAutoExclusive(False)
        self.runButton.setAutoDefault(False)
        self.runButton.setDefault(False)
        self.runButton.setFlat(False)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 29))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHowTo = QtWidgets.QAction(MainWindow)
        self.actionHowTo.setObjectName("actionHowTo")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionHowTo)
        self.menu.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart-TV Transmitter"))
        self.label.setText(_translate("MainWindow", "Код видео"))
        self.menu.setTitle(_translate("MainWindow", "Помощь"))
        self.actionHowTo.setText(_translate("MainWindow", "Как пользоваться"))
        self.actionAbout.setText(_translate("MainWindow", "О программе"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
