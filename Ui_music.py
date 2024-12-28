# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\lolJames\OneDrive\桌面\Machine Learning\Homework\GestureMusicPlayer\music.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GestureMusicPlayer(object):
    def setupUi(self, GestureMusicPlayer):
        GestureMusicPlayer.setObjectName("GestureMusicPlayer")
        GestureMusicPlayer.resize(1008, 935)
        GestureMusicPlayer.setMinimumSize(QtCore.QSize(950, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/CD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GestureMusicPlayer.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(GestureMusicPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.gesture_frame = QtWidgets.QFrame(self.frame)
        self.gesture_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gesture_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gesture_frame.setObjectName("gesture_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gesture_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.camera_label = QtWidgets.QLabel(self.gesture_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_label.sizePolicy().hasHeightForWidth())
        self.camera_label.setSizePolicy(sizePolicy)
        self.camera_label.setMinimumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        self.camera_label.setFont(font)
        self.camera_label.setAutoFillBackground(False)
        self.camera_label.setStyleSheet("QLabel {\n"
"    background-color: #4f4f4f;  /* 背景顏色為黑色 */\n"
"    color: white;  /* 文字顏色為白色 */\n"
"    border-radius: 12px;  /* 添加圓角效果，10px 可根據需要調整 */\n"
"    text-align: center;  /* 確保文字居中 */\n"
"    qproperty-alignment: \'AlignCenter\';  /* 確保 QLabel 內容完全置中 */\n"
"    padding: 10px\n"
"}")
        self.camera_label.setTextFormat(QtCore.Qt.AutoText)
        self.camera_label.setObjectName("camera_label")
        self.verticalLayout_6.addWidget(self.camera_label)
        self.gesture_instruction_label = QtWidgets.QLabel(self.gesture_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gesture_instruction_label.sizePolicy().hasHeightForWidth())
        self.gesture_instruction_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.gesture_instruction_label.setFont(font)
        self.gesture_instruction_label.setStyleSheet("line-height: 1.0;\n"
"border: 2px solid black;      \n"
" border-radius: 10px;         ")
        self.gesture_instruction_label.setLineWidth(-1)
        self.gesture_instruction_label.setTextFormat(QtCore.Qt.RichText)
        self.gesture_instruction_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gesture_instruction_label.setWordWrap(False)
        self.gesture_instruction_label.setObjectName("gesture_instruction_label")
        self.verticalLayout_6.addWidget(self.gesture_instruction_label)
        self.info_textbox = QtWidgets.QTextEdit(self.gesture_frame)
        self.info_textbox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_textbox.sizePolicy().hasHeightForWidth())
        self.info_textbox.setSizePolicy(sizePolicy)
        self.info_textbox.setMinimumSize(QtCore.QSize(0, 50))
        self.info_textbox.setBaseSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.info_textbox.setFont(font)
        self.info_textbox.setStyleSheet("QTextEdit {\n"
"    background-color: #f0f0f0;\n"
"    color: #000000;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"}")
        self.info_textbox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.info_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.info_textbox.setReadOnly(True)
        self.info_textbox.setObjectName("info_textbox")
        self.verticalLayout_6.addWidget(self.info_textbox)
        self.current_song_label = QtWidgets.QLabel(self.gesture_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.current_song_label.setFont(font)
        self.current_song_label.setStyleSheet("    QLabel {\n"
"        background-color: grey;       /* 灰色背景 */\n"
"        color: yellow;                /* 黄色文字 */\n"
"        font-size: 16px;              /* 可选：设置字体大小 */\n"
"        border: 2px solid black;      /* 边框样式 */\n"
"        border-radius: 10px;          /* 圆角半径 */\n"
"        padding: 5px;                 /* 可选：增加文字的内边距 */\n"
"    }")
        self.current_song_label.setObjectName("current_song_label")
        self.verticalLayout_6.addWidget(self.current_song_label)
        self.horizontalLayout_15.addWidget(self.gesture_frame)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setStyleSheet("QListView {\n"
"    outline: none;\n"
"    border: none;\n"
"    background-color: #4f4f4f; /* 整體背景淺灰色 */\n"
"    border-radius: 12px; /* 外框圓角 */\n"
"}\n"
"\n"
"#listWidget::item {\n"
"    background-color: #4f4f4f; /* 項目背景色 */\n"
"    color: #ffffff; /* 文字顏色 */\n"
"    border: none;\n"
"    padding: 8px;\n"
"    margin: 4px; /* 增加間距以突顯圓角效果 */\n"
"    border-radius: 12px; /* 每個項目圓角 */\n"
"}\n"
"\n"
"#listWidget::item:hover {\n"
"    background-color: #6c6c6c; /* 懸停時的較亮背景色 */\n"
"    border-radius: 12px; /* 保持圓角 */\n"
"}\n"
"\n"
"#listWidget::item:selected {\n"
"    background-color: #009688; /* 選中背景色 */\n"
"    color: #ffffff; /* 選中後文字顏色 */\n"
"    border: none;\n"
"    border-radius: 12px; /* 選中效果圓角 */\n"
"}\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_15.addWidget(self.listWidget)
        self.verticalLayout_3.addWidget(self.frame)
        self.volume_music_ctrl_frame = QtWidgets.QFrame(self.centralwidget)
        self.volume_music_ctrl_frame.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.volume_music_ctrl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.volume_music_ctrl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.volume_music_ctrl_frame.setObjectName("volume_music_ctrl_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.volume_music_ctrl_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.volume_frame = QtWidgets.QFrame(self.volume_music_ctrl_frame)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.volume_frame.setFont(font)
        self.volume_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.volume_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.volume_frame.setObjectName("volume_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.volume_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.volume_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.volumeSlider = QtWidgets.QSlider(self.volume_frame)
        self.volumeSlider.setMinimumSize(QtCore.QSize(250, 0))
        self.volumeSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.volumeSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volumeSlider.setStyleSheet("QSlider {\n"
"    border-radius: 10px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #fff; /* 白色 */\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #f00;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -6px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(\n"
"        spread: pad, \n"
"        x1: 0, y1: 0.5, x2: 1, y2: 0.5, \n"
"        stop: 0 #0000ff,   /* 深藍 */\n"
"        stop: 1 #87cefa    /* 淺藍 */\n"
"    );\n"
"}\n"
"")
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setSingleStep(1)
        self.volumeSlider.setProperty("value", 50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setInvertedAppearance(False)
        self.volumeSlider.setInvertedControls(False)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_4.addWidget(self.volumeSlider)
        self.volume_label = QtWidgets.QLabel(self.volume_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.volume_label.setFont(font)
        self.volume_label.setObjectName("volume_label")
        self.horizontalLayout_4.addWidget(self.volume_label)
        self.verticalLayout.addWidget(self.volume_frame, 0, QtCore.Qt.AlignLeft)
        self.music_ctrl_frame = QtWidgets.QFrame(self.volume_music_ctrl_frame)
        self.music_ctrl_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.music_ctrl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_ctrl_frame.setObjectName("music_ctrl_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.music_ctrl_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ctrl_btn_frame = QtWidgets.QFrame(self.music_ctrl_frame)
        self.ctrl_btn_frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.ctrl_btn_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ctrl_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ctrl_btn_frame.setObjectName("ctrl_btn_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ctrl_btn_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inner_ctrl_btn_frame = QtWidgets.QFrame(self.ctrl_btn_frame)
        self.inner_ctrl_btn_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inner_ctrl_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inner_ctrl_btn_frame.setObjectName("inner_ctrl_btn_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.inner_ctrl_btn_frame)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playpushButton = QtWidgets.QPushButton(self.inner_ctrl_btn_frame)
        self.playpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playpushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/images/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playpushButton.setIcon(icon1)
        self.playpushButton.setIconSize(QtCore.QSize(24, 24))
        self.playpushButton.setFlat(True)
        self.playpushButton.setObjectName("playpushButton")
        self.horizontalLayout_2.addWidget(self.playpushButton)
        self.pausepushButton = QtWidgets.QPushButton(self.inner_ctrl_btn_frame)
        self.pausepushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pausepushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/images/Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pausepushButton.setIcon(icon2)
        self.pausepushButton.setIconSize(QtCore.QSize(24, 24))
        self.pausepushButton.setFlat(True)
        self.pausepushButton.setObjectName("pausepushButton")
        self.horizontalLayout_2.addWidget(self.pausepushButton)
        self.stoppushButton = QtWidgets.QPushButton(self.inner_ctrl_btn_frame)
        self.stoppushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stoppushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/images/Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stoppushButton.setIcon(icon3)
        self.stoppushButton.setIconSize(QtCore.QSize(24, 24))
        self.stoppushButton.setFlat(True)
        self.stoppushButton.setObjectName("stoppushButton")
        self.horizontalLayout_2.addWidget(self.stoppushButton)
        self.previouspushButton = QtWidgets.QPushButton(self.inner_ctrl_btn_frame)
        self.previouspushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previouspushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/images/Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previouspushButton.setIcon(icon4)
        self.previouspushButton.setIconSize(QtCore.QSize(24, 24))
        self.previouspushButton.setFlat(True)
        self.previouspushButton.setObjectName("previouspushButton")
        self.horizontalLayout_2.addWidget(self.previouspushButton)
        self.nextpushButton = QtWidgets.QPushButton(self.inner_ctrl_btn_frame)
        self.nextpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextpushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/images/Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextpushButton.setIcon(icon5)
        self.nextpushButton.setIconSize(QtCore.QSize(24, 24))
        self.nextpushButton.setFlat(True)
        self.nextpushButton.setObjectName("nextpushButton")
        self.horizontalLayout_2.addWidget(self.nextpushButton)
        self.verticalLayout_2.addWidget(self.inner_ctrl_btn_frame)
        self.horizontalLayout.addWidget(self.ctrl_btn_frame)
        self.music_progress_frame = QtWidgets.QFrame(self.music_ctrl_frame)
        self.music_progress_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.music_progress_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_progress_frame.setObjectName("music_progress_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.music_progress_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_time_label = QtWidgets.QLabel(self.music_progress_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.start_time_label.setFont(font)
        self.start_time_label.setObjectName("start_time_label")
        self.horizontalLayout_3.addWidget(self.start_time_label)
        self.musicSlider = QtWidgets.QSlider(self.music_progress_frame)
        self.musicSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.musicSlider.setStyleSheet("QSlider {\n"
"    border-radius: 10px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #fff; /* 白色 */\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #f00;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -6px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(\n"
"        spread: pad, \n"
"        x1: 0, y1: 0.5, x2: 1, y2: 0.5, \n"
"        stop: 0 #0000ff,   /* 深藍 */\n"
"        stop: 1 #87cefa    /* 淺藍 */\n"
"    );\n"
"}\n"
"")
        self.musicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicSlider.setObjectName("musicSlider")
        self.horizontalLayout_3.addWidget(self.musicSlider)
        self.end_time_label = QtWidgets.QLabel(self.music_progress_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.end_time_label.setFont(font)
        self.end_time_label.setObjectName("end_time_label")
        self.horizontalLayout_3.addWidget(self.end_time_label)
        self.horizontalLayout.addWidget(self.music_progress_frame)
        self.verticalLayout.addWidget(self.music_ctrl_frame)
        self.verticalLayout_3.addWidget(self.volume_music_ctrl_frame)
        GestureMusicPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GestureMusicPlayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menubar.setStyleSheet("QMenuBar {\n"
"    background-color: #f0f0f0;  /* 設置背景顏色為淺灰色 */\n"
"    color: #000000;  /* 設置文字顏色為黑色 */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;  /* 項目背景透明 */\n"
"    color: #000000;  /* 項目文字顏色 */\n"
"    padding: 8px;  /* 設置項目內邊距 */\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #c8c8c8;  /* 選中項目的背景顏色 */\n"
"    color: #000000;  /* 選中項目的文字顏色 */\n"
"}\n"
"")
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menuMenu.setFont(font)
        self.menuMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuMenu.setObjectName("menuMenu")
        GestureMusicPlayer.setMenuBar(self.menubar)
        self.actionAdd_Songs = QtWidgets.QAction(GestureMusicPlayer)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/images/Create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Songs.setIcon(icon6)
        self.actionAdd_Songs.setObjectName("actionAdd_Songs")
        self.actionRemove_Selected = QtWidgets.QAction(GestureMusicPlayer)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/images/Remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_Selected.setIcon(icon7)
        self.actionRemove_Selected.setObjectName("actionRemove_Selected")
        self.actionRemove_All = QtWidgets.QAction(GestureMusicPlayer)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/images/Delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_All.setIcon(icon8)
        self.actionRemove_All.setObjectName("actionRemove_All")
        self.menuMenu.addAction(self.actionAdd_Songs)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionRemove_Selected)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionRemove_All)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(GestureMusicPlayer)
        QtCore.QMetaObject.connectSlotsByName(GestureMusicPlayer)

    def retranslateUi(self, GestureMusicPlayer):
        _translate = QtCore.QCoreApplication.translate
        GestureMusicPlayer.setWindowTitle(_translate("GestureMusicPlayer", "Gesture Music Player"))
        self.camera_label.setText(_translate("GestureMusicPlayer", "Lens screen not found..."))
        self.gesture_instruction_label.setText(_translate("GestureMusicPlayer", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:400;\">~~~Gesture Instructions~~~</span></p><p><span style=\" font-size:12pt; font-weight:400;\">ok: Start Music<br/>0: Pause/Unpause Music<br/>Pinky: Stop Music<br/>1~9: ⏩ n × 10s<br/>lotus+0~9: ⏪ n × 10s<br/>Thumb Up/Down: Volume Up/Down<br/>Thumb Left/Rignt: Previous/Next Song<br/>Rock!: 100% Volume<br/>▼ Latest Gesture Recognition Results </span></p></body></html>"))
        self.info_textbox.setHtml(_translate("GestureMusicPlayer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><br /></p></body></html>"))
        self.current_song_label.setText(_translate("GestureMusicPlayer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Playing Nothing</span></p></body></html>"))
        self.label.setText(_translate("GestureMusicPlayer", "Volume:"))
        self.volume_label.setText(_translate("GestureMusicPlayer", "50"))
        self.playpushButton.setToolTip(_translate("GestureMusicPlayer", "Play"))
        self.pausepushButton.setToolTip(_translate("GestureMusicPlayer", "Pause/Unpause"))
        self.stoppushButton.setToolTip(_translate("GestureMusicPlayer", "Stop"))
        self.previouspushButton.setToolTip(_translate("GestureMusicPlayer", "Previous"))
        self.nextpushButton.setToolTip(_translate("GestureMusicPlayer", "Next"))
        self.start_time_label.setText(_translate("GestureMusicPlayer", "00:00:00"))
        self.end_time_label.setText(_translate("GestureMusicPlayer", "00:00:00"))
        self.menuMenu.setTitle(_translate("GestureMusicPlayer", "Menu"))
        self.actionAdd_Songs.setText(_translate("GestureMusicPlayer", "Add Songs"))
        self.actionAdd_Songs.setToolTip(_translate("GestureMusicPlayer", "Add songs to music player"))
        self.actionAdd_Songs.setShortcut(_translate("GestureMusicPlayer", "Alt+A"))
        self.actionRemove_Selected.setText(_translate("GestureMusicPlayer", "Remove Selected"))
        self.actionRemove_Selected.setToolTip(_translate("GestureMusicPlayer", "Remove Selected Song"))
        self.actionRemove_Selected.setShortcut(_translate("GestureMusicPlayer", "Del"))
        self.actionRemove_All.setText(_translate("GestureMusicPlayer", "Remove All"))
        self.actionRemove_All.setToolTip(_translate("GestureMusicPlayer", "Remove All Songs"))
        self.actionRemove_All.setShortcut(_translate("GestureMusicPlayer", "Alt+Del"))
import music_res_rc
