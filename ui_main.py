# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(404, 559)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 450, 75, 71))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 450, 75, 71))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(160, 450, 75, 71))
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(10, 80, 18, 160))
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(100, 410, 78, 20))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(230, 410, 78, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 50, 49, 16))
        self.Cover = QFrame(self.centralwidget)
        self.Cover.setObjectName(u"Cover")
        self.Cover.setGeometry(QRect(60, 20, 311, 301))
        self.Cover.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cover.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 330, 181, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 350, 171, 16))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(80, 370, 301, 23))
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Play/Stop", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Track", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Author", None))
    # retranslateUi

