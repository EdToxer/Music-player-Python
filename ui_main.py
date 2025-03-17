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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QTabWidget, QWidget)
import resr_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 600))
        MainWindow.setMaximumSize(QSize(400, 600))
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0\n"
"rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155,\n"
"79, 165, 255));\n"
"")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.push_Next = QPushButton(self.centralwidget)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.push_Next)
        self.push_Next.setObjectName(u"push_Next")
        self.push_Next.setGeometry(QRect(261, 451, 82, 78))
        self.push_Next.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        icon = QIcon()
        icon.addFile(u":/icons/pctr/image_2025-03-06_22-14-54.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_Next.setIcon(icon)
        self.push_Next.setIconSize(QSize(70, 70))
        self.push_Next.setCheckable(True)
        self.push_Back = QPushButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.push_Back)
        self.push_Back.setObjectName(u"push_Back")
        self.push_Back.setGeometry(QRect(31, 451, 82, 78))
        self.push_Back.setAutoFillBackground(False)
        self.push_Back.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        self.push_Back.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/pctr/image_2025-03-06_22-14-15.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_Back.setIcon(icon1)
        self.push_Back.setIconSize(QSize(70, 70))
        self.push_Back.setCheckable(True)
        self.push_Play_Stop = QPushButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.push_Play_Stop)
        self.push_Play_Stop.setObjectName(u"push_Play_Stop")
        self.push_Play_Stop.setGeometry(QRect(146, 451, 82, 78))
        self.push_Play_Stop.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        icon2 = QIcon()
        icon2.addFile(u":/icons/pctr/image_2025-03-06_22-14-25.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_Play_Stop.setIcon(icon2)
        self.push_Play_Stop.setIconSize(QSize(70, 70))
        self.push_Play_Stop.setCheckable(True)
        self.slider_Volume = QSlider(self.centralwidget)
        self.slider_Volume.setObjectName(u"slider_Volume")
        self.slider_Volume.setGeometry(QRect(10, 100, 31, 160))
        self.slider_Volume.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        self.slider_Volume.setOrientation(Qt.Orientation.Vertical)
        self.push_Shuffle = QPushButton(self.centralwidget)
        self.push_Shuffle.setObjectName(u"push_Shuffle")
        self.push_Shuffle.setGeometry(QRect(110, 400, 46, 41))
        self.push_Shuffle.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        icon3 = QIcon()
        icon3.addFile(u":/icons/pctr/image_2025-03-06_22-14-03.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/pctr/image_2025-03-06_22-20-15.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon3.addFile(u":/icons/pctr/image_2025-03-06_22-20-15.png", QSize(), QIcon.Active, QIcon.On)
        icon3.addFile(u":/icons/pctr/image_2025-03-06_22-20-15.png", QSize(), QIcon.Selected, QIcon.On)
        self.push_Shuffle.setIcon(icon3)
        self.push_Shuffle.setIconSize(QSize(40, 40))
        self.push_Shuffle.setCheckable(True)
        self.push_Repeat = QPushButton(self.centralwidget)
        self.push_Repeat.setObjectName(u"push_Repeat")
        self.push_Repeat.setGeometry(QRect(230, 400, 46, 41))
        self.push_Repeat.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        self.push_Repeat.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/pctr/image_2025-03-06_22-15-05.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/pctr/image_2025-03-06_22-17-44.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon4.addFile(u":/icons/pctr/image_2025-03-06_22-17-44.png", QSize(), QIcon.Active, QIcon.On)
        self.push_Repeat.setIcon(icon4)
        self.push_Repeat.setIconSize(QSize(40, 40))
        self.push_Repeat.setCheckable(True)
        self.Cover = QFrame(self.centralwidget)
        self.Cover.setObjectName(u"Cover")
        self.Cover.setGeometry(QRect(60, 30, 311, 301))
        self.Cover.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cover.setFrameShadow(QFrame.Shadow.Raised)
        self.label_TrackName = QLabel(self.centralwidget)
        self.label_TrackName.setObjectName(u"label_TrackName")
        self.label_TrackName.setGeometry(QRect(81, 331, 259, 16))
        self.label_TrackName.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        self.label_Author = QLabel(self.centralwidget)
        self.label_Author.setObjectName(u"label_Author")
        self.label_Author.setGeometry(QRect(81, 353, 259, 16))
        self.label_Author.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border-radius: 1px;\n"
"border-color: rgb(255, 255, 0);")
        self.bar_Music = QProgressBar(self.centralwidget)
        self.bar_Music.setObjectName(u"bar_Music")
        self.bar_Music.setEnabled(True)
        self.bar_Music.setGeometry(QRect(70, 362, 261, 31))
        self.bar_Music.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgba(0, 0, 0, 0)")
        self.bar_Music.setValue(24)
        self.bar_Music.setTextVisible(False)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 60, 31, 31))
        self.pushButton.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        icon5 = QIcon()
        icon5.addFile(u":/icons/pctr/image_2025-03-06_22-13-46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(-1, 10, 41, 40))
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0)")
        icon6 = QIcon()
        icon6.addFile(u":/icons/pctr/image_2025-03-06_22-15-19.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(38, 40))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Player", None))
        self.push_Next.setText("")
#if QT_CONFIG(tooltip)
        self.push_Back.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.push_Play_Stop.setText("")
        self.push_Shuffle.setText("")
        self.label_TrackName.setText("")
        self.label_Author.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

