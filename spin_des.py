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
from PySide2.QtGui import QTransform, QPixmap, QMovie, QFont
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
        font = QFont()
        font.setPointSize(26)
        # self.gridLayoutWidget = QWidget(self.centralwidget)
        # self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        # self.gridLayoutWidget.setGeometry(QRect(0, 0, 860, 900))
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        # self.gridLayout.setGeometry(QRect(200,200,0,0))
        self.main_widget = QWidget(MainWindow)

        self.main_grid = QGridLayout(self.main_widget)
        self.main_grid.setObjectName('main_grid')
        self.main_grid.setContentsMargins(0,0,0,0)

        self.gif = QMovie(self.main_widget)
        self.gif.setFileName('./resource/spinning-arrows.gif')
        self.label = QLabel(self.main_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 430, 450))
        self.label.setMovie(self.gif)
        self.gif.setSpeed(95)
        self.change_button = QPushButton(self.main_widget)
        self.change_button.setObjectName(u"change_button")
        self.change_button.setStyleSheet('''QPushButton{ color: rgb(255, 255, 255);background-color: rgb(0, 113, 193);border-radius: 15px;border-width: 2px;border-color: rgb(0,0,0);border-style: solid}\n
                                            QPushButton:pressed{background-color: rgb(0, 90, 150);border-style: inset};''')
        self.change_button.setText('START!')
        self.change_button.setFont(font)
        self.timer_label = QLabel(self.main_widget)
        self.timer_label.setObjectName(u"label")
        
        self.timer_label.setFont(font)

        self.timer = QTimer(self.main_widget)
        self.timer.timeout.connect(self.tt)

        self.label_queen = QLabel(self.main_widget)
        
        
        pic=QPixmap("./resource/queen.jpg")
        self.pic_logo = pic.scaledToHeight(450)
        self.label_queen.setPixmap(self.pic_logo)
        self.label_queen.setVisible(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.label.setSizePolicy(sizePolicy)

        self.label_hbd = QLabel(self.main_widget)
        self.label_hbd.setText('Happy Birthday !!')
        self.label_hbd.setFont(font)
        self.label_hbd.setVisible(False)

        self.re_button = QPushButton(self.main_widget)
        self.re_button.setObjectName(u"re_button")
        self.re_button.setStyleSheet('''QPushButton{ color: rgb(255, 255, 255);background-color: rgb(0, 113, 193);border-radius: 15px;border-width: 2px;border-color: rgb(0,0,0);border-style: solid}\n
                                            QPushButton:pressed{background-color: rgb(0, 90, 150);border-style: inset};''')
        self.re_button.setText('再..再一次')
        self.re_button.setVisible(False)
        self.re_button.setFont(font)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 21, 21)

        self.gridLayout.addWidget(self.label, 10,10,1,1)
        self.gridLayout.addWidget(self.change_button, 20,8,1,5)
        self.gridLayout.addWidget(self.timer_label, 1, 10, 8, 8)
        self.gridLayout.addWidget(self.label_queen, 1, 10, 10, 1)
        self.gridLayout.addWidget(self.label_hbd, 12, 9, 5, 5)
        self.gridLayout.addWidget(self.re_button,20, 15, 1, 5)
        

        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.change_button.clicked.connect(self.time_count)
        self.re_button.clicked.connect(self.re)
        self.sec = 5

    def re(self):
        self.sec = 5
        self.label_queen.setVisible(False)
        self.label.setVisible(False)
        self.timer_label.setText('')
        # self.timer.stop()
        self.label_hbd.setVisible(False)
        self.change_button.setVisible(True)
        self.re_button.setVisible(False)

    def time_count(self):
        self.change_button.setVisible(False)
        self.label.setVisible(True)
        self.timer.start(1000)
        self.gif.start()
        self.timer_label.setText(f'00:00:{self.sec:02d}')
    
    def tt(self):
        self.sec -= 1
        if self.sec == 0:
            self.label_queen.setVisible(True)
            
            self.label.setVisible(False)
            self.gif.stop()
            # self.timer_label.setVisible(False)
            self.timer.stop()
            self.label_hbd.setVisible(True)
            self.re_button.setVisible(True)
        self.timer_label.setText(f'00:00:{self.sec:02d}')
        

        

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
        # self.label.setText("3")
    # retranslateUi

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())