# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from threading import Timer
from PySide2.QtCore import QTimer, QMetaObject, QCoreApplication, QRect
from PySide2.QtGui import QTransform, QPixmap, QMovie
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QSizePolicy, QMainWindow, QPushButton
import sys
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setStyleSheet("background-color:rgb(255,255,255)")
        # MainWindow.setFixedSize(530, 550)
        # self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName(u"centralwidget")
        
        # self.gridLayoutWidget = QWidget(self.centralwidget)
        # self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        # self.gridLayoutWidget.setGeometry(QRect(0, 0, 860, 900))
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        # self.gridLayout.setGeometry(QRect(200,200,0,0))
        self.main_widget = QWidget(MainWindow)
        self.gif = QMovie("spinning-arrows.gif")
        self.label = QLabel(self.main_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 430, 450))
        self.label.setMovie(self.gif)
        self.gif.setSpeed(95)
        self.gif.start()
        self.change_button = QPushButton(self.main_widget)
        self.change_button.setObjectName(u"change_button")
        self.change_button.setStyleSheet("background-color:rgb(225,250,20)")
        self.change_button.setText('START!')
        # pic=QPixmap("arrow.png")
        # self.pic_logo = pic.scaledToHeight(450)
        # # pic_logo = self.pic

        # self.label.setPixmap(self.pic_logo)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.label.setSizePolicy(sizePolicy)

        

        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 457, 22))
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName(u"statusbar")

        self.gridLayout.addWidget(self.main_widget, 0, 0, 21, 21)
        self.gridLayout.addWidget(self.label, 10,10,1,1)
        self.gridLayout.addWidget(self.change_button, 20,10,1,1)
        

        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.change_button.clicked.connect(self.random_pos)

    def random_pos(self):
        same_pos = True
        while same_pos:
            self.gridLayout.removeWidget(self.label)
            self.gridLayout.removeWidget(self.change_button)
            r1 = np.random.randint(1,21)
            c1 = np.random.randint(1,21)
            self.gridLayout.addWidget(self.label, r1,c1,1,1)
            r2 = np.random.randint(1,21)
            c2 = np.random.randint(1,21)
            self.gridLayout.addWidget(self.change_button, r2,c2,1,1)
            if r1!=r2 or c1!=c2:
                same_pos = False


    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"哈哈哈", None))
        self.label.setText("")
    # retranslateUi

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())