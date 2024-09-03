# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lvdApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resource_c

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(764, 563)
        MainWindow.setStyleSheet(u"background-color: rgb(51, 51, 51);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_Widget = QWidget(self.centralwidget)
        self.icon_Widget.setObjectName(u"icon_Widget")
        self.icon_Widget.setMinimumSize(QSize(57, 0))
        self.icon_Widget.setMaximumSize(QSize(57, 16777215))
        self.icon_Widget.setStyleSheet(u"QWidget {\n"
"	background-color: #000000;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: #E6E6E6;\n"
"	height: 40px\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_Widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_widget_switch_Button = QPushButton(self.icon_Widget)
        self.icon_widget_switch_Button.setObjectName(u"icon_widget_switch_Button")
        font = QFont()
        font.setFamilies([u"Syne"])
        self.icon_widget_switch_Button.setFont(font)
        self.icon_widget_switch_Button.setStyleSheet(u"QPushButton {\n"
"	height: 20px\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ICON/MENU CLOSE 2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_widget_switch_Button.setIcon(icon)
        self.icon_widget_switch_Button.setIconSize(QSize(20, 20))
        self.icon_widget_switch_Button.setCheckable(True)
        self.icon_widget_switch_Button.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.icon_widget_switch_Button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_5 = QSpacerItem(20, 141, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.home_Button = QPushButton(self.icon_Widget)
        self.home_Button.setObjectName(u"home_Button")
        self.home_Button.setFont(font)
        self.home_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_Button.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/ICON/HOME (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/ICON/HOME.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.home_Button.setIcon(icon1)
        self.home_Button.setIconSize(QSize(30, 20))
        self.home_Button.setCheckable(True)
        self.home_Button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.home_Button)

        self.my_file_Button = QPushButton(self.icon_Widget)
        self.my_file_Button.setObjectName(u"my_file_Button")
        self.my_file_Button.setFont(font)
        self.my_file_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/ICON/FILE.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/ICON/FILE 2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.my_file_Button.setIcon(icon2)
        self.my_file_Button.setIconSize(QSize(20, 20))
        self.my_file_Button.setCheckable(True)
        self.my_file_Button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.my_file_Button)

        self.tolls_Button = QPushButton(self.icon_Widget)
        self.tolls_Button.setObjectName(u"tolls_Button")
        self.tolls_Button.setFont(font)
        self.tolls_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/ICON/TOOLS 2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/ICON/TOOLS.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.tolls_Button.setIcon(icon3)
        self.tolls_Button.setIconSize(QSize(20, 20))
        self.tolls_Button.setCheckable(True)
        self.tolls_Button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.tolls_Button)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 218, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.icon_Widget, 0, 0, 1, 1)

        self.icon_Widget_With_Name = QWidget(self.centralwidget)
        self.icon_Widget_With_Name.setObjectName(u"icon_Widget_With_Name")
        self.icon_Widget_With_Name.setMinimumSize(QSize(142, 0))
        self.icon_Widget_With_Name.setMaximumSize(QSize(142, 16777215))
        self.icon_Widget_With_Name.setStyleSheet(u"QWidget {\n"
"	background-color: #000000;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 40px;\n"
"	padding-left: 20px;\n"
"	color: #E6E6E6;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 0px none;\n"
"	border-left: 2px solid #00FFA6;\n"
"	background-color: #292929;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.icon_Widget_With_Name)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_widget_with_name_switch_Button = QPushButton(self.icon_Widget_With_Name)
        self.icon_widget_with_name_switch_Button.setObjectName(u"icon_widget_with_name_switch_Button")
        self.icon_widget_with_name_switch_Button.setFont(font)
        self.icon_widget_with_name_switch_Button.setStyleSheet(u"QPushButton {\n"
"	height: 20px;\n"
"	padding-left: 0;\n"
"	color: none;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 0px none;\n"
"	background-color: none;\n"
"}")
        self.icon_widget_with_name_switch_Button.setIcon(icon)
        self.icon_widget_with_name_switch_Button.setIconSize(QSize(20, 20))
        self.icon_widget_with_name_switch_Button.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.icon_widget_with_name_switch_Button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.profile_images = QPushButton(self.icon_Widget_With_Name)
        self.profile_images.setObjectName(u"profile_images")
        self.profile_images.setStyleSheet(u"QPushButton {\n"
"	height: 80px;\n"
"	padding-left: 0;\n"
"	color: none;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 0px none;\n"
"	background-color: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/ICON/dp_image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profile_images.setIcon(icon4)
        self.profile_images.setIconSize(QSize(70, 70))

        self.horizontalLayout_5.addWidget(self.profile_images)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.app_name = QLabel(self.icon_Widget_With_Name)
        self.app_name.setObjectName(u"app_name")
        font1 = QFont()
        font1.setFamilies([u"Syne Medium"])
        font1.setPointSize(15)
        font1.setKerning(True)
        self.app_name.setFont(font1)
        self.app_name.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.app_name.setStyleSheet(u"QLabel {\n"
"	color: #E6E6E6;\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.app_name.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.app_name)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 40, -1, -1)
        self.home_Button_2 = QPushButton(self.icon_Widget_With_Name)
        self.home_Button_2.setObjectName(u"home_Button_2")
        self.home_Button_2.setFont(font)
        self.home_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_Button_2.setStyleSheet(u"QPushButton:checked {\n"
"font-weight: bold;\n"
"}")
        self.home_Button_2.setIcon(icon1)
        self.home_Button_2.setIconSize(QSize(30, 20))
        self.home_Button_2.setCheckable(True)
        self.home_Button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_Button_2)

        self.my_file_Button_2 = QPushButton(self.icon_Widget_With_Name)
        self.my_file_Button_2.setObjectName(u"my_file_Button_2")
        self.my_file_Button_2.setFont(font)
        self.my_file_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.my_file_Button_2.setStyleSheet(u"QPushButton:checked {\n"
"font-weight: bold;\n"
"}")
        self.my_file_Button_2.setIcon(icon2)
        self.my_file_Button_2.setIconSize(QSize(20, 20))
        self.my_file_Button_2.setCheckable(True)
        self.my_file_Button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.my_file_Button_2)

        self.tools_Button_2 = QPushButton(self.icon_Widget_With_Name)
        self.tools_Button_2.setObjectName(u"tools_Button_2")
        self.tools_Button_2.setFont(font)
        self.tools_Button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tools_Button_2.setStyleSheet(u"QPushButton:checked {\n"
"font-weight: bold;\n"
"}")
        self.tools_Button_2.setIcon(icon3)
        self.tools_Button_2.setIconSize(QSize(18, 20))
        self.tools_Button_2.setCheckable(True)
        self.tools_Button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.tools_Button_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 192, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.icon_Widget_With_Name, 0, 1, 1, 1)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"QWidget {\n"
"background-color: #202020;\n"
"}\n"
"\n"
"QLabel {\n"
"qproperty-alignment: 'AlignLeft';\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"font-weight: bold;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.main_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.top_menu_widget = QWidget(self.main_widget)
        self.top_menu_widget.setObjectName(u"top_menu_widget")
        self.top_menu_widget.setStyleSheet(u"QWidget {\n"
"	background-color: #000000;\n"
"}\n"
"\n"
"QPushButton {\n"
"height: 30px;\n"
"width: 25;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.top_menu_widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(468, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_Button = QPushButton(self.top_menu_widget)
        self.user_Button.setObjectName(u"user_Button")
        icon5 = QIcon()
        icon5.addFile(u":/ICON/USER.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_Button.setIcon(icon5)
        self.user_Button.setIconSize(QSize(15, 15))

        self.horizontalLayout.addWidget(self.user_Button)

        self.minimize_Button = QPushButton(self.top_menu_widget)
        self.minimize_Button.setObjectName(u"minimize_Button")
        self.minimize_Button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #292929;\n"
"height: 50px\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/ICON/RESTORE.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_Button.setIcon(icon6)
        self.minimize_Button.setIconSize(QSize(8, 10))
        self.minimize_Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.minimize_Button)

        self.max_Button = QPushButton(self.top_menu_widget)
        self.max_Button.setObjectName(u"max_Button")
        self.max_Button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: #292929;\n"
"height: 50px\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/ICON/MAX.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.max_Button.setIcon(icon7)
        self.max_Button.setIconSize(QSize(10, 10))
        self.max_Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.max_Button)

        self.close_Button = QPushButton(self.top_menu_widget)
        self.close_Button.setObjectName(u"close_Button")
        self.close_Button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: red;\n"
"height: 50px\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/ICON/CLOSE.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_Button.setIcon(icon8)
        self.close_Button.setIconSize(QSize(10, 10))
        self.close_Button.setCheckable(True)

        self.horizontalLayout.addWidget(self.close_Button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.top_menu_widget)

        self.mainPage_stackedWidget = QStackedWidget(self.main_widget)
        self.mainPage_stackedWidget.setObjectName(u"mainPage_stackedWidget")
        self.mainPage_stackedWidget.setStyleSheet(u"QLabel {\n"
"color: #E6E6E6;\n"
"}")
        self.mainPage_stackedWidget.setFrameShape(QFrame.NoFrame)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QWidget {\n"
"background-color: #202020;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: #E6E6E6\n"
"\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.home_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.homepage_header_widget = QWidget(self.home_page)
        self.homepage_header_widget.setObjectName(u"homepage_header_widget")
        self.homepage_header_widget.setStyleSheet(u"QPushButton{\n"
"color: #707070;\n"
"border: none;\n"
"width: 80px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color: #E6E6E6;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #828282;\n"
"border-Bottom: 1px solid #4A4A4A;\n"
"padding-bottom: 5px\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.homepage_header_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 40, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(134, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.youtube_download_page_button = QPushButton(self.homepage_header_widget)
        self.youtube_download_page_button.setObjectName(u"youtube_download_page_button")
        font2 = QFont()
        font2.setFamilies([u"Syne"])
        font2.setPointSize(10)
        self.youtube_download_page_button.setFont(font2)
        self.youtube_download_page_button.setCheckable(True)
        self.youtube_download_page_button.setAutoExclusive(True)

        self.horizontalLayout_8.addWidget(self.youtube_download_page_button)

        self.facebook_download_page_button = QPushButton(self.homepage_header_widget)
        self.facebook_download_page_button.setObjectName(u"facebook_download_page_button")
        self.facebook_download_page_button.setFont(font2)
        self.facebook_download_page_button.setCheckable(True)
        self.facebook_download_page_button.setAutoExclusive(True)

        self.horizontalLayout_8.addWidget(self.facebook_download_page_button)

        self.instagram_download_page_button = QPushButton(self.homepage_header_widget)
        self.instagram_download_page_button.setObjectName(u"instagram_download_page_button")
        self.instagram_download_page_button.setFont(font2)
        self.instagram_download_page_button.setCheckable(True)
        self.instagram_download_page_button.setAutoExclusive(True)

        self.horizontalLayout_8.addWidget(self.instagram_download_page_button)

        self.tk = QPushButton(self.homepage_header_widget)
        self.tk.setObjectName(u"tk")
        self.tk.setFont(font2)
        self.tk.setCheckable(True)
        self.tk.setAutoExclusive(True)

        self.horizontalLayout_8.addWidget(self.tk)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(133, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_13.addWidget(self.homepage_header_widget)

        self.downloadPage_stackedWidget = QStackedWidget(self.home_page)
        self.downloadPage_stackedWidget.setObjectName(u"downloadPage_stackedWidget")
        self.youtube_download_page = QWidget()
        self.youtube_download_page.setObjectName(u"youtube_download_page")
        self.verticalLayout_8 = QVBoxLayout(self.youtube_download_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_67 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_67)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.youtubeTitle_LAbel = QLabel(self.youtube_download_page)
        self.youtubeTitle_LAbel.setObjectName(u"youtubeTitle_LAbel")
        font3 = QFont()
        font3.setFamilies([u"Syne SemiBold"])
        font3.setPointSize(20)
        self.youtubeTitle_LAbel.setFont(font3)
        self.youtubeTitle_LAbel.setStyleSheet(u"QLabel {\n"
"color: #00FFA6;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_30.addWidget(self.youtubeTitle_LAbel)

        self.youtubeStatus_Label = QLabel(self.youtube_download_page)
        self.youtubeStatus_Label.setObjectName(u"youtubeStatus_Label")
        self.youtubeStatus_Label.setMaximumSize(QSize(306, 16))
        font4 = QFont()
        font4.setFamilies([u"Syne"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.youtubeStatus_Label.setFont(font4)
        self.youtubeStatus_Label.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_30.addWidget(self.youtubeStatus_Label)


        self.horizontalLayout_86.addLayout(self.verticalLayout_30)

        self.horizontalSpacer_68 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_68)


        self.verticalLayout_8.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(-1, 40, -1, -1)
        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_60)

        self.searchbar_Widget = QWidget(self.youtube_download_page)
        self.searchbar_Widget.setObjectName(u"searchbar_Widget")
        self.searchbar_Widget.setMinimumSize(QSize(450, 46))
        self.searchbar_Widget.setMaximumSize(QSize(450, 46))
        self.searchbar_Widget.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_77 = QHBoxLayout(self.searchbar_Widget)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.youtubeURL_Lineedit = QLineEdit(self.searchbar_Widget)
        self.youtubeURL_Lineedit.setObjectName(u"youtubeURL_Lineedit")
        self.youtubeURL_Lineedit.setMinimumSize(QSize(300, 20))
        self.youtubeURL_Lineedit.setStyleSheet(u"color: #E6E6E6;")

        self.horizontalLayout_78.addWidget(self.youtubeURL_Lineedit)

        self.youtubeFetchVideo_Button = QPushButton(self.searchbar_Widget)
        self.youtubeFetchVideo_Button.setObjectName(u"youtubeFetchVideo_Button")
        self.youtubeFetchVideo_Button.setMinimumSize(QSize(90, 30))
        self.youtubeFetchVideo_Button.setMaximumSize(QSize(90, 30))
        font5 = QFont()
        font5.setFamilies([u"Syne SemiBold"])
        font5.setPointSize(10)
        self.youtubeFetchVideo_Button.setFont(font5)
        self.youtubeFetchVideo_Button.setStyleSheet(u"QPushButton {\n"
"color: #00FFA6;\n"
"border-radius: 13px;\n"
"background-color: qlineargradient(spread:pad, x1:0.495955, y1:0.421, x2:1, y2:1, stop:0 rgba(0, 0, 0, 236), stop:1 rgba(39, 107, 48, 255));\n"
"}")
        self.youtubeFetchVideo_Button.setCheckable(True)

        self.horizontalLayout_78.addWidget(self.youtubeFetchVideo_Button)


        self.horizontalLayout_77.addLayout(self.horizontalLayout_78)


        self.horizontalLayout_76.addWidget(self.searchbar_Widget)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_61)


        self.verticalLayout_8.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_78 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_78)

        self.youtubeThumbnail_Widget = QWidget(self.youtube_download_page)
        self.youtubeThumbnail_Widget.setObjectName(u"youtubeThumbnail_Widget")
        self.youtubeThumbnail_Widget.setMinimumSize(QSize(0, 0))
        self.youtubeThumbnail_Widget.setMaximumSize(QSize(1000, 1000))
        self.horizontalLayout_11 = QHBoxLayout(self.youtubeThumbnail_Widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.youtubeThumbnail_ImageCard_Widget = QWidget(self.youtubeThumbnail_Widget)
        self.youtubeThumbnail_ImageCard_Widget.setObjectName(u"youtubeThumbnail_ImageCard_Widget")
        self.youtubeThumbnail_ImageCard_Widget.setMinimumSize(QSize(228, 128))
        self.youtubeThumbnail_ImageCard_Widget.setMaximumSize(QSize(228, 128))
        self.youtubeThumbnail_ImageCard_Widget.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.552773, y1:0.449409, x2:1, y2:1, stop:0 rgba(26, 26, 26, 255), stop:1 rgba(53, 93, 58, 255));\n"
"border-radius: 10px;\n"
"}")
        self.youtubeThumbnail_Image_Label = QLabel(self.youtubeThumbnail_ImageCard_Widget)
        self.youtubeThumbnail_Image_Label.setObjectName(u"youtubeThumbnail_Image_Label")
        self.youtubeThumbnail_Image_Label.setGeometry(QRect(0, 0, 228, 128))
        self.youtubeThumbnail_Image_Label.setMinimumSize(QSize(228, 128))
        self.youtubeThumbnail_Image_Label.setMaximumSize(QSize(228, 128))
        self.youtubeThumbnail_Image_Label.setStyleSheet(u"Qlabel {\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.youtubeThumbnail_Image_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_11.addWidget(self.youtubeThumbnail_ImageCard_Widget)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.youtube_VideoName_Label = QLabel(self.youtubeThumbnail_Widget)
        self.youtube_VideoName_Label.setObjectName(u"youtube_VideoName_Label")
        self.youtube_VideoName_Label.setMinimumSize(QSize(270, 40))
        self.youtube_VideoName_Label.setMaximumSize(QSize(270, 40))
        self.youtube_VideoName_Label.setFont(font5)
        self.youtube_VideoName_Label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.youtube_VideoName_Label)

        self.youtube_duration_Label = QLabel(self.youtubeThumbnail_Widget)
        self.youtube_duration_Label.setObjectName(u"youtube_duration_Label")
        self.youtube_duration_Label.setMinimumSize(QSize(270, 16))
        self.youtube_duration_Label.setMaximumSize(QSize(270, 16))
        font6 = QFont()
        font6.setFamilies([u"Syne Medium"])
        font6.setPointSize(10)
        self.youtube_duration_Label.setFont(font6)
        self.youtube_duration_Label.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: \"AlignLeft\";\n"
"}")
        self.youtube_duration_Label.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.youtube_duration_Label)

        self.download_comboBox_widget_7 = QWidget(self.youtubeThumbnail_Widget)
        self.download_comboBox_widget_7.setObjectName(u"download_comboBox_widget_7")
        self.download_comboBox_widget_7.setMinimumSize(QSize(290, 46))
        self.download_comboBox_widget_7.setMaximumSize(QSize(290, 46))
        self.download_comboBox_widget_7.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.download_comboBox_widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.youtubeDownload_Button = QPushButton(self.download_comboBox_widget_7)
        self.youtubeDownload_Button.setObjectName(u"youtubeDownload_Button")
        self.youtubeDownload_Button.setMinimumSize(QSize(90, 30))
        self.youtubeDownload_Button.setMaximumSize(QSize(90, 30))
        self.youtubeDownload_Button.setFont(font5)
        self.youtubeDownload_Button.setStyleSheet(u"QPushButton {\n"
"color: #000000;\n"
"border-radius: 13px;\n"
"background-color: #00FFA6;\n"
"}")
        self.youtubeDownload_Button.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.youtubeDownload_Button)

        self.youtubeFormatSelection_ComboBox = QComboBox(self.download_comboBox_widget_7)
        self.youtubeFormatSelection_ComboBox.setObjectName(u"youtubeFormatSelection_ComboBox")
        self.youtubeFormatSelection_ComboBox.setMinimumSize(QSize(180, 30))
        self.youtubeFormatSelection_ComboBox.setMaximumSize(QSize(180, 30))
        self.youtubeFormatSelection_ComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #292929; /* ComboBox background */\n"
"    color: white; /* Text color */\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #292929; /* Drop-down background */\n"
"    border: none;\n"
"	border-radius: 5px;\n"
"    color: white; /* Text color */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 20px; /* Drop-down width */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/ICON/drop_down_icon.png); /* Arrow image */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin-right: 0px; /* Margin for alignment */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #292929; /* Drop-down list background */\n"
"    color: #E6E6E6; /* Text color */\n"
"    padding: 0; /* No extra padding */\n"
"	selection-background-color: #3D3D3D; /* Background color of selected item */\n"
"	selection-color: white; /* Text color of selected item */\n"
"	padding:"
                        " 5px;\n"
"	border-radius: 5px; /* Rounded corners for the dropdown list */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #292929; /* Background color of individual items */\n"
"    color: #E6E6E6; /* Text color of items */\n"
"    padding: 5px; /* Padding within items */\n"
" 	min-height: 30px; /* Minimum height of items */\n"
"    min-width: 100px; /* Minimum width of items */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #00FFA6; /* Background color for selected items */\n"
"    color: #202020; /* Text color for selected items */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none; /* No border around the scrollbar */\n"
"    background: #292929; /* Scrollbar background color */\n"
"    width: 10px; /* Scrollbar width */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: white; /* Handle color */\n"
"    min-height: 20px; /* Minimum height of the handle */\n"
"    border-radius: 5px; /* Rounded corners for the handle *"
                        "/\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none; /* Remove the border around the add-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the add-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none; /* Remove the border around the sub-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the sub-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* Remove arrow backgrounds */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* Remove page background */\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.youtubeFormatSelection_ComboBox)


        self.verticalLayout_7.addWidget(self.download_comboBox_widget_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_7)


        self.horizontalLayout_12.addWidget(self.youtubeThumbnail_Widget)

        self.horizontalSpacer_63 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_63)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_64)

        self.youtube_ProgressBar = QProgressBar(self.youtube_download_page)
        self.youtube_ProgressBar.setObjectName(u"youtube_ProgressBar")
        self.youtube_ProgressBar.setMinimumSize(QSize(450, 10))
        self.youtube_ProgressBar.setMaximumSize(QSize(450, 10))
        font7 = QFont()
        font7.setFamilies([u"Syne Medium"])
        font7.setPointSize(12)
        self.youtube_ProgressBar.setFont(font7)
        self.youtube_ProgressBar.setStyleSheet(u"QProgressBar {\n"
"color: white;\n"
"background-color: #292929;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"color: white;\n"
"background-color: #00FFA6;;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"")
        self.youtube_ProgressBar.setValue(0)
        self.youtube_ProgressBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.youtube_ProgressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_83.addWidget(self.youtube_ProgressBar)

        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_65)


        self.verticalLayout_8.addLayout(self.horizontalLayout_83)

        self.verticalSpacer_14 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_14)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.fileLocation_Label_6 = QLabel(self.youtube_download_page)
        self.fileLocation_Label_6.setObjectName(u"fileLocation_Label_6")
        self.fileLocation_Label_6.setMinimumSize(QSize(71, 16))
        self.fileLocation_Label_6.setMaximumSize(QSize(71, 16))
        self.fileLocation_Label_6.setFont(font6)
        self.fileLocation_Label_6.setStyleSheet(u"color: #707070;")
        self.fileLocation_Label_6.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.fileLocation_Label_6)

        self.folder_browser_widget_7 = QWidget(self.youtube_download_page)
        self.folder_browser_widget_7.setObjectName(u"folder_browser_widget_7")
        self.folder_browser_widget_7.setMinimumSize(QSize(321, 40))
        self.folder_browser_widget_7.setMaximumSize(QSize(321, 40))
        self.folder_browser_widget_7.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_85 = QHBoxLayout(self.folder_browser_widget_7)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.youtubeLocationURL_Label = QLabel(self.folder_browser_widget_7)
        self.youtubeLocationURL_Label.setObjectName(u"youtubeLocationURL_Label")
        self.youtubeLocationURL_Label.setMinimumSize(QSize(290, 20))
        self.youtubeLocationURL_Label.setMaximumSize(QSize(290, 20))
        font8 = QFont()
        font8.setPointSize(10)
        self.youtubeLocationURL_Label.setFont(font8)
        self.youtubeLocationURL_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_85.addWidget(self.youtubeLocationURL_Label)


        self.horizontalLayout_2.addWidget(self.folder_browser_widget_7)

        self.youtubeBrowseFileLocation_Button = QPushButton(self.youtube_download_page)
        self.youtubeBrowseFileLocation_Button.setObjectName(u"youtubeBrowseFileLocation_Button")
        self.youtubeBrowseFileLocation_Button.setFont(font)
        self.youtubeBrowseFileLocation_Button.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/ICON/Icon_-7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.youtubeBrowseFileLocation_Button.setIcon(icon9)
        self.youtubeBrowseFileLocation_Button.setIconSize(QSize(20, 20))
        self.youtubeBrowseFileLocation_Button.setCheckable(True)
        self.youtubeBrowseFileLocation_Button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.youtubeBrowseFileLocation_Button)

        self.horizontalSpacer_66 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_66)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.downloadPage_stackedWidget.addWidget(self.youtube_download_page)
        self.facebook_download_page = QWidget()
        self.facebook_download_page.setObjectName(u"facebook_download_page")
        self.verticalLayout_10 = QVBoxLayout(self.facebook_download_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 7)
        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_76 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_76)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.facebookTitle_Label = QLabel(self.facebook_download_page)
        self.facebookTitle_Label.setObjectName(u"facebookTitle_Label")
        self.facebookTitle_Label.setFont(font3)
        self.facebookTitle_Label.setStyleSheet(u"QLabel {\n"
"color: #00FFA6;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_33.addWidget(self.facebookTitle_Label)

        self.facebookStatus_Label = QLabel(self.facebook_download_page)
        self.facebookStatus_Label.setObjectName(u"facebookStatus_Label")
        self.facebookStatus_Label.setFont(font4)
        self.facebookStatus_Label.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_33.addWidget(self.facebookStatus_Label)


        self.horizontalLayout_97.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_77 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_77)


        self.verticalLayout_10.addLayout(self.horizontalLayout_97)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(20)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(-1, 40, -1, -1)
        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_69)

        self.facebookSearchbar_Widget = QWidget(self.facebook_download_page)
        self.facebookSearchbar_Widget.setObjectName(u"facebookSearchbar_Widget")
        self.facebookSearchbar_Widget.setMinimumSize(QSize(450, 46))
        self.facebookSearchbar_Widget.setMaximumSize(QSize(450, 46))
        self.facebookSearchbar_Widget.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_88 = QHBoxLayout(self.facebookSearchbar_Widget)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.url_lineedit_7 = QLineEdit(self.facebookSearchbar_Widget)
        self.url_lineedit_7.setObjectName(u"url_lineedit_7")
        self.url_lineedit_7.setMinimumSize(QSize(300, 20))
        self.url_lineedit_7.setStyleSheet(u"color: #E6E6E6;")

        self.horizontalLayout_89.addWidget(self.url_lineedit_7)

        self.facebookFetchVideo_Button = QPushButton(self.facebookSearchbar_Widget)
        self.facebookFetchVideo_Button.setObjectName(u"facebookFetchVideo_Button")
        self.facebookFetchVideo_Button.setMinimumSize(QSize(90, 30))
        self.facebookFetchVideo_Button.setMaximumSize(QSize(90, 30))
        self.facebookFetchVideo_Button.setFont(font5)
        self.facebookFetchVideo_Button.setStyleSheet(u"QPushButton {\n"
"color: #00FFA6;\n"
"border-radius: 13px;\n"
"background-color: qlineargradient(spread:pad, x1:0.495955, y1:0.421, x2:1, y2:1, stop:0 rgba(0, 0, 0, 236), stop:1 rgba(39, 107, 48, 255));\n"
"}")
        self.facebookFetchVideo_Button.setCheckable(True)

        self.horizontalLayout_89.addWidget(self.facebookFetchVideo_Button)


        self.horizontalLayout_88.addLayout(self.horizontalLayout_89)


        self.horizontalLayout_87.addWidget(self.facebookSearchbar_Widget)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_70)


        self.verticalLayout_31.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_71)

        self.facebookThumbnail_Widget = QWidget(self.facebook_download_page)
        self.facebookThumbnail_Widget.setObjectName(u"facebookThumbnail_Widget")
        self.facebookThumbnail_Widget.setMinimumSize(QSize(449, 0))
        self.facebookThumbnail_Widget.setMaximumSize(QSize(449, 146))
        self.horizontalLayout_91 = QHBoxLayout(self.facebookThumbnail_Widget)
        self.horizontalLayout_91.setSpacing(10)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.facebookThumbnail_ImageCard_Widget = QWidget(self.facebookThumbnail_Widget)
        self.facebookThumbnail_ImageCard_Widget.setObjectName(u"facebookThumbnail_ImageCard_Widget")
        self.facebookThumbnail_ImageCard_Widget.setMinimumSize(QSize(192, 132))
        self.facebookThumbnail_ImageCard_Widget.setMaximumSize(QSize(192, 132))
        self.facebookThumbnail_ImageCard_Widget.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.552773, y1:0.449409, x2:1, y2:1, stop:0 rgba(26, 26, 26, 255), stop:1 rgba(53, 93, 58, 255));\n"
"border-radius: 10px;\n"
"}")
        self.facebookThumbnail_Image_Label = QLabel(self.facebookThumbnail_ImageCard_Widget)
        self.facebookThumbnail_Image_Label.setObjectName(u"facebookThumbnail_Image_Label")
        self.facebookThumbnail_Image_Label.setGeometry(QRect(0, 0, 190, 130))
        self.facebookThumbnail_Image_Label.setMinimumSize(QSize(190, 130))
        self.facebookThumbnail_Image_Label.setMaximumSize(QSize(190, 131))
        self.facebookThumbnail_Image_Label.setStyleSheet(u"Qlabel {\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.facebookThumbnail_Image_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_91.addWidget(self.facebookThumbnail_ImageCard_Widget)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 10, -1, 10)
        self.facebookVideoName_Label = QLabel(self.facebookThumbnail_Widget)
        self.facebookVideoName_Label.setObjectName(u"facebookVideoName_Label")
        self.facebookVideoName_Label.setMinimumSize(QSize(220, 40))
        self.facebookVideoName_Label.setMaximumSize(QSize(220, 40))
        self.facebookVideoName_Label.setFont(font5)
        self.facebookVideoName_Label.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.facebookVideoName_Label)

        self.facebookDuration_Label = QLabel(self.facebookThumbnail_Widget)
        self.facebookDuration_Label.setObjectName(u"facebookDuration_Label")
        self.facebookDuration_Label.setFont(font6)
        self.facebookDuration_Label.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: \"AlignLeft\";\n"
"}")
        self.facebookDuration_Label.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.facebookDuration_Label)

        self.download_comboBox_widget_8 = QWidget(self.facebookThumbnail_Widget)
        self.download_comboBox_widget_8.setObjectName(u"download_comboBox_widget_8")
        self.download_comboBox_widget_8.setMinimumSize(QSize(231, 46))
        self.download_comboBox_widget_8.setMaximumSize(QSize(231, 46))
        self.download_comboBox_widget_8.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_92 = QHBoxLayout(self.download_comboBox_widget_8)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.facebookDownload_Button = QPushButton(self.download_comboBox_widget_8)
        self.facebookDownload_Button.setObjectName(u"facebookDownload_Button")
        self.facebookDownload_Button.setMinimumSize(QSize(90, 30))
        self.facebookDownload_Button.setMaximumSize(QSize(90, 30))
        self.facebookDownload_Button.setFont(font5)
        self.facebookDownload_Button.setStyleSheet(u"QPushButton {\n"
"color: #000000;\n"
"border-radius: 13px;\n"
"background-color: #00FFA6;\n"
"}")
        self.facebookDownload_Button.setCheckable(True)

        self.horizontalLayout_93.addWidget(self.facebookDownload_Button)

        self.facebookFormatSelection_comboBox = QComboBox(self.download_comboBox_widget_8)
        self.facebookFormatSelection_comboBox.setObjectName(u"facebookFormatSelection_comboBox")
        self.facebookFormatSelection_comboBox.setMinimumSize(QSize(120, 30))
        self.facebookFormatSelection_comboBox.setMaximumSize(QSize(120, 30))
        self.facebookFormatSelection_comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #292929; /* ComboBox background */\n"
"    color: white; /* Text color */\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #292929; /* Drop-down background */\n"
"    border: none;\n"
"	border-radius: 5px;\n"
"    color: white; /* Text color */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 20px; /* Drop-down width */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/ICON/drop_down_icon.png); /* Arrow image */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin-right: 0px; /* Margin for alignment */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #292929; /* Drop-down list background */\n"
"    color: #E6E6E6; /* Text color */\n"
"    padding: 0; /* No extra padding */\n"
"	selection-background-color: #3D3D3D; /* Background color of selected item */\n"
"	selection-color: white; /* Text color of selected item */\n"
"	padding:"
                        " 5px;\n"
"	border-radius: 5px; /* Rounded corners for the dropdown list */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #292929; /* Background color of individual items */\n"
"    color: #E6E6E6; /* Text color of items */\n"
"    padding: 10px; /* Padding within items */\n"
" 	min-height: 30px; /* Minimum height of items */\n"
"    min-width: 100px; /* Minimum width of items */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: lightgreen; /* Background color for selected items */\n"
"    color: darkblue; /* Text color for selected items */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none; /* No border around the scrollbar */\n"
"    background: #292929; /* Scrollbar background color */\n"
"    width: 10px; /* Scrollbar width */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: white; /* Handle color */\n"
"    min-height: 20px; /* Minimum height of the handle */\n"
"    "
                        "border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none; /* Remove the border around the add-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the add-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none; /* Remove the border around the sub-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the sub-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* Remove arrow backgrounds */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* Remove page background */\n"
"}\n"
"")

        self.horizontalLayout_93.addWidget(self.facebookFormatSelection_comboBox)


        self.horizontalLayout_92.addLayout(self.horizontalLayout_93)


        self.verticalLayout_32.addWidget(self.download_comboBox_widget_8)


        self.horizontalLayout_91.addLayout(self.verticalLayout_32)


        self.horizontalLayout_90.addWidget(self.facebookThumbnail_Widget)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_72)


        self.verticalLayout_31.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_73)

        self.facebookProgressBar = QProgressBar(self.facebook_download_page)
        self.facebookProgressBar.setObjectName(u"facebookProgressBar")
        self.facebookProgressBar.setMinimumSize(QSize(450, 10))
        self.facebookProgressBar.setMaximumSize(QSize(450, 10))
        self.facebookProgressBar.setFont(font7)
        self.facebookProgressBar.setStyleSheet(u"QProgressBar {\n"
"color: white;\n"
"background-color: #292929;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"color: white;\n"
"background-color: #00FFA6;;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"")
        self.facebookProgressBar.setValue(0)
        self.facebookProgressBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.facebookProgressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_94.addWidget(self.facebookProgressBar)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_74)


        self.verticalLayout_31.addLayout(self.horizontalLayout_94)


        self.verticalLayout_10.addLayout(self.verticalLayout_31)

        self.verticalSpacer_15 = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_15)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(40, -1, -1, -1)
        self.fileLocation_Label_7 = QLabel(self.facebook_download_page)
        self.fileLocation_Label_7.setObjectName(u"fileLocation_Label_7")
        self.fileLocation_Label_7.setMinimumSize(QSize(71, 16))
        self.fileLocation_Label_7.setMaximumSize(QSize(71, 16))
        self.fileLocation_Label_7.setFont(font6)
        self.fileLocation_Label_7.setStyleSheet(u"color: #707070;")
        self.fileLocation_Label_7.setWordWrap(True)

        self.horizontalLayout_95.addWidget(self.fileLocation_Label_7)

        self.folder_browser_widget_8 = QWidget(self.facebook_download_page)
        self.folder_browser_widget_8.setObjectName(u"folder_browser_widget_8")
        self.folder_browser_widget_8.setMinimumSize(QSize(321, 40))
        self.folder_browser_widget_8.setMaximumSize(QSize(321, 40))
        self.folder_browser_widget_8.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_96 = QHBoxLayout(self.folder_browser_widget_8)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.facebookLocationURL_Label = QLabel(self.folder_browser_widget_8)
        self.facebookLocationURL_Label.setObjectName(u"facebookLocationURL_Label")
        self.facebookLocationURL_Label.setMinimumSize(QSize(290, 20))
        self.facebookLocationURL_Label.setMaximumSize(QSize(290, 20))
        self.facebookLocationURL_Label.setFont(font8)
        self.facebookLocationURL_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_96.addWidget(self.facebookLocationURL_Label)


        self.horizontalLayout_95.addWidget(self.folder_browser_widget_8)

        self.facebookBowseFileLocation_Button = QPushButton(self.facebook_download_page)
        self.facebookBowseFileLocation_Button.setObjectName(u"facebookBowseFileLocation_Button")
        self.facebookBowseFileLocation_Button.setFont(font)
        self.facebookBowseFileLocation_Button.setStyleSheet(u"")
        self.facebookBowseFileLocation_Button.setIcon(icon9)
        self.facebookBowseFileLocation_Button.setIconSize(QSize(20, 20))
        self.facebookBowseFileLocation_Button.setCheckable(True)
        self.facebookBowseFileLocation_Button.setAutoExclusive(True)

        self.horizontalLayout_95.addWidget(self.facebookBowseFileLocation_Button)

        self.horizontalSpacer_75 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_75)


        self.verticalLayout_10.addLayout(self.horizontalLayout_95)

        self.downloadPage_stackedWidget.addWidget(self.facebook_download_page)
        self.instagram_download_page = QWidget()
        self.instagram_download_page.setObjectName(u"instagram_download_page")
        self.verticalLayout_6 = QVBoxLayout(self.instagram_download_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 7)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_24 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_24)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.instagramTitle_Label = QLabel(self.instagram_download_page)
        self.instagramTitle_Label.setObjectName(u"instagramTitle_Label")
        self.instagramTitle_Label.setFont(font3)
        self.instagramTitle_Label.setStyleSheet(u"QLabel {\n"
"color: #00FFA6;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_15.addWidget(self.instagramTitle_Label)

        self.instagramStatus_Label = QLabel(self.instagram_download_page)
        self.instagramStatus_Label.setObjectName(u"instagramStatus_Label")
        self.instagramStatus_Label.setFont(font4)
        self.instagramStatus_Label.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_15.addWidget(self.instagramStatus_Label)


        self.horizontalLayout_32.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_25 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_25)


        self.verticalLayout_6.addLayout(self.horizontalLayout_32)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 40, -1, -1)
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_26)

        self.instagramSearchbar_Widget = QWidget(self.instagram_download_page)
        self.instagramSearchbar_Widget.setObjectName(u"instagramSearchbar_Widget")
        self.instagramSearchbar_Widget.setMinimumSize(QSize(450, 46))
        self.instagramSearchbar_Widget.setMaximumSize(QSize(450, 46))
        self.instagramSearchbar_Widget.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_34 = QHBoxLayout(self.instagramSearchbar_Widget)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.instagramUrl_LineEdit = QLineEdit(self.instagramSearchbar_Widget)
        self.instagramUrl_LineEdit.setObjectName(u"instagramUrl_LineEdit")
        self.instagramUrl_LineEdit.setMinimumSize(QSize(300, 20))
        self.instagramUrl_LineEdit.setStyleSheet(u"color: #E6E6E6;")

        self.horizontalLayout_35.addWidget(self.instagramUrl_LineEdit)

        self.instagramFetchVideo_Button = QPushButton(self.instagramSearchbar_Widget)
        self.instagramFetchVideo_Button.setObjectName(u"instagramFetchVideo_Button")
        self.instagramFetchVideo_Button.setMinimumSize(QSize(90, 30))
        self.instagramFetchVideo_Button.setMaximumSize(QSize(90, 30))
        self.instagramFetchVideo_Button.setFont(font5)
        self.instagramFetchVideo_Button.setStyleSheet(u"QPushButton {\n"
"color: #00FFA6;\n"
"border-radius: 13px;\n"
"background-color: qlineargradient(spread:pad, x1:0.495955, y1:0.421, x2:1, y2:1, stop:0 rgba(0, 0, 0, 236), stop:1 rgba(39, 107, 48, 255));\n"
"}")
        self.instagramFetchVideo_Button.setCheckable(True)

        self.horizontalLayout_35.addWidget(self.instagramFetchVideo_Button)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_33.addWidget(self.instagramSearchbar_Widget)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_27)


        self.verticalLayout_16.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_28)

        self.instagramThumbnail_Widget = QWidget(self.instagram_download_page)
        self.instagramThumbnail_Widget.setObjectName(u"instagramThumbnail_Widget")
        self.instagramThumbnail_Widget.setMinimumSize(QSize(449, 0))
        self.instagramThumbnail_Widget.setMaximumSize(QSize(449, 146))
        self.horizontalLayout_37 = QHBoxLayout(self.instagramThumbnail_Widget)
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.instagramThumbnail_imageCard_Widget = QWidget(self.instagramThumbnail_Widget)
        self.instagramThumbnail_imageCard_Widget.setObjectName(u"instagramThumbnail_imageCard_Widget")
        self.instagramThumbnail_imageCard_Widget.setMinimumSize(QSize(192, 132))
        self.instagramThumbnail_imageCard_Widget.setMaximumSize(QSize(192, 132))
        self.instagramThumbnail_imageCard_Widget.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.552773, y1:0.449409, x2:1, y2:1, stop:0 rgba(26, 26, 26, 255), stop:1 rgba(53, 93, 58, 255));\n"
"border-radius: 10px;\n"
"}")
        self.instagramThumbnail_Image_Label = QLabel(self.instagramThumbnail_imageCard_Widget)
        self.instagramThumbnail_Image_Label.setObjectName(u"instagramThumbnail_Image_Label")
        self.instagramThumbnail_Image_Label.setGeometry(QRect(0, 0, 190, 130))
        self.instagramThumbnail_Image_Label.setMinimumSize(QSize(190, 130))
        self.instagramThumbnail_Image_Label.setMaximumSize(QSize(190, 131))
        self.instagramThumbnail_Image_Label.setStyleSheet(u"Qlabel {\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.instagramThumbnail_Image_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_37.addWidget(self.instagramThumbnail_imageCard_Widget)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 10, -1, 10)
        self.instagramVideoName_Label = QLabel(self.instagramThumbnail_Widget)
        self.instagramVideoName_Label.setObjectName(u"instagramVideoName_Label")
        self.instagramVideoName_Label.setMinimumSize(QSize(220, 40))
        self.instagramVideoName_Label.setMaximumSize(QSize(220, 40))
        self.instagramVideoName_Label.setFont(font5)
        self.instagramVideoName_Label.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.instagramVideoName_Label)

        self.instagramDuration_Label = QLabel(self.instagramThumbnail_Widget)
        self.instagramDuration_Label.setObjectName(u"instagramDuration_Label")
        self.instagramDuration_Label.setFont(font6)
        self.instagramDuration_Label.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: \"AlignLeft\";\n"
"}")
        self.instagramDuration_Label.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.instagramDuration_Label)

        self.download_comboBox_widget_3 = QWidget(self.instagramThumbnail_Widget)
        self.download_comboBox_widget_3.setObjectName(u"download_comboBox_widget_3")
        self.download_comboBox_widget_3.setMinimumSize(QSize(231, 46))
        self.download_comboBox_widget_3.setMaximumSize(QSize(231, 46))
        self.download_comboBox_widget_3.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_38 = QHBoxLayout(self.download_comboBox_widget_3)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.instagramDownload_Button = QPushButton(self.download_comboBox_widget_3)
        self.instagramDownload_Button.setObjectName(u"instagramDownload_Button")
        self.instagramDownload_Button.setMinimumSize(QSize(90, 30))
        self.instagramDownload_Button.setMaximumSize(QSize(90, 30))
        self.instagramDownload_Button.setFont(font5)
        self.instagramDownload_Button.setStyleSheet(u"QPushButton {\n"
"color: #000000;\n"
"border-radius: 13px;\n"
"background-color: #00FFA6;\n"
"}")
        self.instagramDownload_Button.setCheckable(True)

        self.horizontalLayout_39.addWidget(self.instagramDownload_Button)

        self.instagramFormatSelection_ComboBox = QComboBox(self.download_comboBox_widget_3)
        self.instagramFormatSelection_ComboBox.setObjectName(u"instagramFormatSelection_ComboBox")
        self.instagramFormatSelection_ComboBox.setMinimumSize(QSize(120, 30))
        self.instagramFormatSelection_ComboBox.setMaximumSize(QSize(120, 30))
        self.instagramFormatSelection_ComboBox.setFont(font2)
        self.instagramFormatSelection_ComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #292929; /* ComboBox background */\n"
"    color: white; /* Text color */\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #292929; /* Drop-down background */\n"
"    border: none;\n"
"	border-radius: 5px;\n"
"    color: white; /* Text color */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 20px; /* Drop-down width */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/ICON/drop_down_icon.png); /* Arrow image */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin-right: 0px; /* Margin for alignment */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #292929; /* Drop-down list background */\n"
"    color: #E6E6E6; /* Text color */\n"
"    padding: 0; /* No extra padding */\n"
"	selection-background-color: #3D3D3D; /* Background color of selected item */\n"
"	selection-color: white; /* Text color of selected item */\n"
"	padding:"
                        " 5px;\n"
"	border-radius: 5px; /* Rounded corners for the dropdown list */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #292929; /* Background color of individual items */\n"
"    color: #E6E6E6; /* Text color of items */\n"
"    padding: 10px; /* Padding within items */\n"
" 	min-height: 30px; /* Minimum height of items */\n"
"    min-width: 100px; /* Minimum width of items */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: lightgreen; /* Background color for selected items */\n"
"    color: darkblue; /* Text color for selected items */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none; /* No border around the scrollbar */\n"
"    background: #292929; /* Scrollbar background color */\n"
"    width: 10px; /* Scrollbar width */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: white; /* Handle color */\n"
"    min-height: 20px; /* Minimum height of the handle */\n"
"    "
                        "border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none; /* Remove the border around the add-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the add-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none; /* Remove the border around the sub-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the sub-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* Remove arrow backgrounds */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* Remove page background */\n"
"}\n"
"")

        self.horizontalLayout_39.addWidget(self.instagramFormatSelection_ComboBox)


        self.horizontalLayout_38.addLayout(self.horizontalLayout_39)


        self.verticalLayout_17.addWidget(self.download_comboBox_widget_3)


        self.horizontalLayout_37.addLayout(self.verticalLayout_17)


        self.horizontalLayout_36.addWidget(self.instagramThumbnail_Widget)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_29)


        self.verticalLayout_16.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_30)

        self.instagramProgressBar = QProgressBar(self.instagram_download_page)
        self.instagramProgressBar.setObjectName(u"instagramProgressBar")
        self.instagramProgressBar.setMinimumSize(QSize(450, 10))
        self.instagramProgressBar.setMaximumSize(QSize(450, 10))
        self.instagramProgressBar.setFont(font7)
        self.instagramProgressBar.setStyleSheet(u"QProgressBar {\n"
"color: white;\n"
"background-color: #292929;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"color: white;\n"
"background-color: #00FFA6;;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"")
        self.instagramProgressBar.setValue(0)
        self.instagramProgressBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.instagramProgressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_40.addWidget(self.instagramProgressBar)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_31)


        self.verticalLayout_16.addLayout(self.horizontalLayout_40)


        self.verticalLayout_6.addLayout(self.verticalLayout_16)

        self.verticalSpacer_11 = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_11)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(40, -1, -1, -1)
        self.fileLocation_Label_2 = QLabel(self.instagram_download_page)
        self.fileLocation_Label_2.setObjectName(u"fileLocation_Label_2")
        self.fileLocation_Label_2.setMinimumSize(QSize(71, 16))
        self.fileLocation_Label_2.setMaximumSize(QSize(71, 16))
        self.fileLocation_Label_2.setFont(font6)
        self.fileLocation_Label_2.setStyleSheet(u"color: #707070;")
        self.fileLocation_Label_2.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.fileLocation_Label_2)

        self.folder_browser_widget_3 = QWidget(self.instagram_download_page)
        self.folder_browser_widget_3.setObjectName(u"folder_browser_widget_3")
        self.folder_browser_widget_3.setMinimumSize(QSize(321, 40))
        self.folder_browser_widget_3.setMaximumSize(QSize(321, 40))
        self.folder_browser_widget_3.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_41 = QHBoxLayout(self.folder_browser_widget_3)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.instagramLocationURL_Label = QLabel(self.folder_browser_widget_3)
        self.instagramLocationURL_Label.setObjectName(u"instagramLocationURL_Label")
        self.instagramLocationURL_Label.setMinimumSize(QSize(290, 20))
        self.instagramLocationURL_Label.setMaximumSize(QSize(290, 20))
        self.instagramLocationURL_Label.setFont(font8)
        self.instagramLocationURL_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_41.addWidget(self.instagramLocationURL_Label)


        self.horizontalLayout_42.addWidget(self.folder_browser_widget_3)

        self.instagramBrowseFileLocation_Button = QPushButton(self.instagram_download_page)
        self.instagramBrowseFileLocation_Button.setObjectName(u"instagramBrowseFileLocation_Button")
        self.instagramBrowseFileLocation_Button.setFont(font)
        self.instagramBrowseFileLocation_Button.setStyleSheet(u"")
        self.instagramBrowseFileLocation_Button.setIcon(icon9)
        self.instagramBrowseFileLocation_Button.setIconSize(QSize(20, 20))
        self.instagramBrowseFileLocation_Button.setCheckable(True)
        self.instagramBrowseFileLocation_Button.setAutoExclusive(True)

        self.horizontalLayout_42.addWidget(self.instagramBrowseFileLocation_Button)

        self.horizontalSpacer_32 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_32)


        self.verticalLayout_6.addLayout(self.horizontalLayout_42)

        self.downloadPage_stackedWidget.addWidget(self.instagram_download_page)
        self.tiktok_download_page = QWidget()
        self.tiktok_download_page.setObjectName(u"tiktok_download_page")
        self.verticalLayout_9 = QVBoxLayout(self.tiktok_download_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_58 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_58)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.tiktokTitle_Label = QLabel(self.tiktok_download_page)
        self.tiktokTitle_Label.setObjectName(u"tiktokTitle_Label")
        self.tiktokTitle_Label.setFont(font3)
        self.tiktokTitle_Label.setStyleSheet(u"QLabel {\n"
"color: #00FFA6;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_27.addWidget(self.tiktokTitle_Label)

        self.status_Label_4 = QLabel(self.tiktok_download_page)
        self.status_Label_4.setObjectName(u"status_Label_4")
        self.status_Label_4.setFont(font4)
        self.status_Label_4.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: 'AlignCenter';\n"
"background-color: none;\n"
"}")

        self.verticalLayout_27.addWidget(self.status_Label_4)


        self.horizontalLayout_75.addLayout(self.verticalLayout_27)

        self.horizontalSpacer_59 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_59)


        self.verticalLayout_9.addLayout(self.horizontalLayout_75)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(-1, 40, -1, -1)
        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_51)

        self.tiktokSearchbar_Widget = QWidget(self.tiktok_download_page)
        self.tiktokSearchbar_Widget.setObjectName(u"tiktokSearchbar_Widget")
        self.tiktokSearchbar_Widget.setMinimumSize(QSize(450, 46))
        self.tiktokSearchbar_Widget.setMaximumSize(QSize(450, 46))
        self.tiktokSearchbar_Widget.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_66 = QHBoxLayout(self.tiktokSearchbar_Widget)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.ticktokURL_LineEdit = QLineEdit(self.tiktokSearchbar_Widget)
        self.ticktokURL_LineEdit.setObjectName(u"ticktokURL_LineEdit")
        self.ticktokURL_LineEdit.setMinimumSize(QSize(300, 20))
        self.ticktokURL_LineEdit.setStyleSheet(u"color: #E6E6E6;")

        self.horizontalLayout_67.addWidget(self.ticktokURL_LineEdit)

        self.tiktokFetchVideo_Button_6 = QPushButton(self.tiktokSearchbar_Widget)
        self.tiktokFetchVideo_Button_6.setObjectName(u"tiktokFetchVideo_Button_6")
        self.tiktokFetchVideo_Button_6.setMinimumSize(QSize(90, 30))
        self.tiktokFetchVideo_Button_6.setMaximumSize(QSize(90, 30))
        self.tiktokFetchVideo_Button_6.setFont(font5)
        self.tiktokFetchVideo_Button_6.setStyleSheet(u"QPushButton {\n"
"color: #00FFA6;\n"
"border-radius: 13px;\n"
"background-color: qlineargradient(spread:pad, x1:0.495955, y1:0.421, x2:1, y2:1, stop:0 rgba(0, 0, 0, 236), stop:1 rgba(39, 107, 48, 255));\n"
"}")
        self.tiktokFetchVideo_Button_6.setCheckable(True)

        self.horizontalLayout_67.addWidget(self.tiktokFetchVideo_Button_6)


        self.horizontalLayout_66.addLayout(self.horizontalLayout_67)


        self.horizontalLayout_65.addWidget(self.tiktokSearchbar_Widget)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_52)


        self.verticalLayout_25.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_53)

        self.tiktokThumbnail_Widget = QWidget(self.tiktok_download_page)
        self.tiktokThumbnail_Widget.setObjectName(u"tiktokThumbnail_Widget")
        self.tiktokThumbnail_Widget.setMinimumSize(QSize(449, 0))
        self.tiktokThumbnail_Widget.setMaximumSize(QSize(449, 146))
        self.horizontalLayout_69 = QHBoxLayout(self.tiktokThumbnail_Widget)
        self.horizontalLayout_69.setSpacing(10)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.tiktokThumbnail_ImageCard_Widget = QWidget(self.tiktokThumbnail_Widget)
        self.tiktokThumbnail_ImageCard_Widget.setObjectName(u"tiktokThumbnail_ImageCard_Widget")
        self.tiktokThumbnail_ImageCard_Widget.setMinimumSize(QSize(192, 132))
        self.tiktokThumbnail_ImageCard_Widget.setMaximumSize(QSize(192, 132))
        self.tiktokThumbnail_ImageCard_Widget.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.552773, y1:0.449409, x2:1, y2:1, stop:0 rgba(26, 26, 26, 255), stop:1 rgba(53, 93, 58, 255));\n"
"border-radius: 10px;\n"
"}")
        self.tiktokThumbnail_Image_Label = QLabel(self.tiktokThumbnail_ImageCard_Widget)
        self.tiktokThumbnail_Image_Label.setObjectName(u"tiktokThumbnail_Image_Label")
        self.tiktokThumbnail_Image_Label.setGeometry(QRect(0, 0, 190, 130))
        self.tiktokThumbnail_Image_Label.setMinimumSize(QSize(190, 130))
        self.tiktokThumbnail_Image_Label.setMaximumSize(QSize(190, 131))
        self.tiktokThumbnail_Image_Label.setStyleSheet(u"Qlabel {\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.tiktokThumbnail_Image_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_69.addWidget(self.tiktokThumbnail_ImageCard_Widget)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 10, -1, 10)
        self.tiktokVideoName_Label = QLabel(self.tiktokThumbnail_Widget)
        self.tiktokVideoName_Label.setObjectName(u"tiktokVideoName_Label")
        self.tiktokVideoName_Label.setMinimumSize(QSize(220, 40))
        self.tiktokVideoName_Label.setMaximumSize(QSize(220, 40))
        self.tiktokVideoName_Label.setFont(font5)
        self.tiktokVideoName_Label.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.tiktokVideoName_Label)

        self.tiktokDuration_Label = QLabel(self.tiktokThumbnail_Widget)
        self.tiktokDuration_Label.setObjectName(u"tiktokDuration_Label")
        self.tiktokDuration_Label.setFont(font6)
        self.tiktokDuration_Label.setStyleSheet(u"QLabel {\n"
"color: #707070;\n"
"qproperty-alignment: \"AlignLeft\";\n"
"}")
        self.tiktokDuration_Label.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.tiktokDuration_Label)

        self.download_comboBox_widget_6 = QWidget(self.tiktokThumbnail_Widget)
        self.download_comboBox_widget_6.setObjectName(u"download_comboBox_widget_6")
        self.download_comboBox_widget_6.setMinimumSize(QSize(231, 46))
        self.download_comboBox_widget_6.setMaximumSize(QSize(231, 46))
        self.download_comboBox_widget_6.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_70 = QHBoxLayout(self.download_comboBox_widget_6)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.tiktokDownload_Button = QPushButton(self.download_comboBox_widget_6)
        self.tiktokDownload_Button.setObjectName(u"tiktokDownload_Button")
        self.tiktokDownload_Button.setMinimumSize(QSize(90, 30))
        self.tiktokDownload_Button.setMaximumSize(QSize(90, 30))
        self.tiktokDownload_Button.setFont(font5)
        self.tiktokDownload_Button.setStyleSheet(u"QPushButton {\n"
"color: #000000;\n"
"border-radius: 13px;\n"
"background-color: #00FFA6;\n"
"}")
        self.tiktokDownload_Button.setCheckable(True)

        self.horizontalLayout_71.addWidget(self.tiktokDownload_Button)

        self.tiktokFormatSelection_ComboBox = QComboBox(self.download_comboBox_widget_6)
        self.tiktokFormatSelection_ComboBox.setObjectName(u"tiktokFormatSelection_ComboBox")
        self.tiktokFormatSelection_ComboBox.setMinimumSize(QSize(120, 30))
        self.tiktokFormatSelection_ComboBox.setMaximumSize(QSize(120, 30))
        self.tiktokFormatSelection_ComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #292929; /* ComboBox background */\n"
"    color: white; /* Text color */\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #292929; /* Drop-down background */\n"
"    border: none;\n"
"	border-radius: 5px;\n"
"    color: white; /* Text color */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 20px; /* Drop-down width */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/ICON/drop_down_icon.png); /* Arrow image */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin-right: 0px; /* Margin for alignment */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #292929; /* Drop-down list background */\n"
"    color: #E6E6E6; /* Text color */\n"
"    padding: 0; /* No extra padding */\n"
"	selection-background-color: #3D3D3D; /* Background color of selected item */\n"
"	selection-color: white; /* Text color of selected item */\n"
"	padding:"
                        " 5px;\n"
"	border-radius: 5px; /* Rounded corners for the dropdown list */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #292929; /* Background color of individual items */\n"
"    color: #E6E6E6; /* Text color of items */\n"
"    padding: 10px; /* Padding within items */\n"
" 	min-height: 30px; /* Minimum height of items */\n"
"    min-width: 100px; /* Minimum width of items */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: lightgreen; /* Background color for selected items */\n"
"    color: darkblue; /* Text color for selected items */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none; /* No border around the scrollbar */\n"
"    background: #292929; /* Scrollbar background color */\n"
"    width: 10px; /* Scrollbar width */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: white; /* Handle color */\n"
"    min-height: 20px; /* Minimum height of the handle */\n"
"    "
                        "border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none; /* Remove the border around the add-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the add-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none; /* Remove the border around the sub-line */\n"
"    background: none; /* Remove background */\n"
"    height: 15px; /* Height of the sub-line area */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* Remove arrow backgrounds */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* Remove page background */\n"
"}\n"
"")

        self.horizontalLayout_71.addWidget(self.tiktokFormatSelection_ComboBox)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_71)


        self.verticalLayout_26.addWidget(self.download_comboBox_widget_6)


        self.horizontalLayout_69.addLayout(self.verticalLayout_26)


        self.horizontalLayout_68.addWidget(self.tiktokThumbnail_Widget)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_54)


        self.verticalLayout_25.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_55)

        self.tiktok_ProgressBar = QProgressBar(self.tiktok_download_page)
        self.tiktok_ProgressBar.setObjectName(u"tiktok_ProgressBar")
        self.tiktok_ProgressBar.setMinimumSize(QSize(450, 10))
        self.tiktok_ProgressBar.setMaximumSize(QSize(450, 10))
        self.tiktok_ProgressBar.setFont(font7)
        self.tiktok_ProgressBar.setStyleSheet(u"QProgressBar {\n"
"color: white;\n"
"background-color: #292929;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"color: white;\n"
"background-color: #00FFA6;;\n"
"border-radius: 5;\n"
"}\n"
"\n"
"")
        self.tiktok_ProgressBar.setValue(0)
        self.tiktok_ProgressBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tiktok_ProgressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_72.addWidget(self.tiktok_ProgressBar)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_56)


        self.verticalLayout_25.addLayout(self.horizontalLayout_72)


        self.verticalLayout_9.addLayout(self.verticalLayout_25)

        self.verticalSpacer_13 = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_13)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(40, -1, -1, -1)
        self.fileLocation_Label_5 = QLabel(self.tiktok_download_page)
        self.fileLocation_Label_5.setObjectName(u"fileLocation_Label_5")
        self.fileLocation_Label_5.setMinimumSize(QSize(71, 16))
        self.fileLocation_Label_5.setMaximumSize(QSize(71, 16))
        self.fileLocation_Label_5.setFont(font6)
        self.fileLocation_Label_5.setStyleSheet(u"color: #707070;")
        self.fileLocation_Label_5.setWordWrap(True)

        self.horizontalLayout_73.addWidget(self.fileLocation_Label_5)

        self.folder_browser_widget_6 = QWidget(self.tiktok_download_page)
        self.folder_browser_widget_6.setObjectName(u"folder_browser_widget_6")
        self.folder_browser_widget_6.setMinimumSize(QSize(321, 40))
        self.folder_browser_widget_6.setMaximumSize(QSize(321, 40))
        self.folder_browser_widget_6.setStyleSheet(u"QWidget {\n"
"background-color: #292929;\n"
"border-radius: 20px;\n"
"}")
        self.horizontalLayout_74 = QHBoxLayout(self.folder_browser_widget_6)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.tiktokLocationURL_Label = QLabel(self.folder_browser_widget_6)
        self.tiktokLocationURL_Label.setObjectName(u"tiktokLocationURL_Label")
        self.tiktokLocationURL_Label.setMinimumSize(QSize(290, 20))
        self.tiktokLocationURL_Label.setMaximumSize(QSize(290, 20))
        self.tiktokLocationURL_Label.setFont(font8)
        self.tiktokLocationURL_Label.setAlignment(Qt.AlignLeading)

        self.horizontalLayout_74.addWidget(self.tiktokLocationURL_Label)


        self.horizontalLayout_73.addWidget(self.folder_browser_widget_6)

        self.tiktokBrowseFileLocation_Button = QPushButton(self.tiktok_download_page)
        self.tiktokBrowseFileLocation_Button.setObjectName(u"tiktokBrowseFileLocation_Button")
        self.tiktokBrowseFileLocation_Button.setFont(font)
        self.tiktokBrowseFileLocation_Button.setStyleSheet(u"")
        self.tiktokBrowseFileLocation_Button.setIcon(icon9)
        self.tiktokBrowseFileLocation_Button.setIconSize(QSize(20, 20))
        self.tiktokBrowseFileLocation_Button.setCheckable(True)
        self.tiktokBrowseFileLocation_Button.setAutoExclusive(True)

        self.horizontalLayout_73.addWidget(self.tiktokBrowseFileLocation_Button)

        self.horizontalSpacer_57 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_57)


        self.verticalLayout_9.addLayout(self.horizontalLayout_73)

        self.downloadPage_stackedWidget.addWidget(self.tiktok_download_page)

        self.verticalLayout_13.addWidget(self.downloadPage_stackedWidget)

        self.mainPage_stackedWidget.addWidget(self.home_page)
        self.myfile_page = QWidget()
        self.myfile_page.setObjectName(u"myfile_page")
        self.verticalLayout_11 = QVBoxLayout(self.myfile_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.myfile_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"qproperty-alignment: 'AlignCenter';")

        self.verticalLayout_11.addWidget(self.label_2)

        self.label = QLabel(self.myfile_page)
        self.label.setObjectName(u"label")
        font9 = QFont()
        font9.setFamilies([u"Syne"])
        font9.setPointSize(12)
        self.label.setFont(font9)
        self.label.setStyleSheet(u"qproperty-alignment: 'AlignCenter';\n"
"")

        self.verticalLayout_11.addWidget(self.label)

        self.mainPage_stackedWidget.addWidget(self.myfile_page)
        self.tools_page = QWidget()
        self.tools_page.setObjectName(u"tools_page")
        self.verticalLayout_12 = QVBoxLayout(self.tools_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.tools_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"qproperty-alignment: 'AlignCenter';")

        self.verticalLayout_12.addWidget(self.label_3)

        self.label_4 = QLabel(self.tools_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font9)
        self.label_4.setStyleSheet(u"qproperty-alignment: 'AlignCenter';\n"
"")

        self.verticalLayout_12.addWidget(self.label_4)

        self.mainPage_stackedWidget.addWidget(self.tools_page)

        self.verticalLayout_14.addWidget(self.mainPage_stackedWidget)


        self.gridLayout.addWidget(self.main_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.home_Button_2.toggled.connect(self.home_Button.setChecked)
        self.home_Button.toggled.connect(self.home_Button_2.setChecked)
        self.my_file_Button.toggled.connect(self.my_file_Button_2.setChecked)
        self.my_file_Button_2.toggled.connect(self.my_file_Button.setChecked)
        self.tolls_Button.toggled.connect(self.tools_Button_2.setChecked)
        self.tools_Button_2.toggled.connect(self.tolls_Button.setChecked)
        self.icon_widget_with_name_switch_Button.toggled.connect(self.icon_Widget.setVisible)
        self.icon_widget_with_name_switch_Button.toggled.connect(self.icon_Widget_With_Name.setHidden)
        self.icon_widget_switch_Button.toggled.connect(self.icon_Widget_With_Name.setVisible)
        self.icon_widget_switch_Button.toggled.connect(self.icon_Widget.setHidden)
        self.close_Button.toggled.connect(MainWindow.close)
        self.max_Button.windowIconChanged.connect(MainWindow.showMaximized)
        self.minimize_Button.windowIconChanged.connect(MainWindow.hide)

        self.mainPage_stackedWidget.setCurrentIndex(0)
        self.downloadPage_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.icon_widget_switch_Button.setToolTip(QCoreApplication.translate("MainWindow", u"Double click to close manu", None))
#endif // QT_CONFIG(tooltip)
        self.icon_widget_switch_Button.setText("")
        self.home_Button.setText("")
        self.my_file_Button.setText("")
        self.tolls_Button.setText("")
#if QT_CONFIG(tooltip)
        self.icon_widget_with_name_switch_Button.setToolTip(QCoreApplication.translate("MainWindow", u"Double click to close manu", None))
#endif // QT_CONFIG(tooltip)
        self.icon_widget_with_name_switch_Button.setText("")
        self.profile_images.setText("")
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"Line Video Downloader", None))
        self.home_Button_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.my_file_Button_2.setText(QCoreApplication.translate("MainWindow", u"My file", None))
        self.tools_Button_2.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.user_Button.setText("")
        self.minimize_Button.setText("")
        self.max_Button.setText("")
        self.close_Button.setText("")
        self.youtube_download_page_button.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.facebook_download_page_button.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.instagram_download_page_button.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        self.tk.setText(QCoreApplication.translate("MainWindow", u"TikTok", None))
        self.youtubeTitle_LAbel.setText(QCoreApplication.translate("MainWindow", u"Youtube Downloader", None))
        self.youtubeStatus_Label.setText(QCoreApplication.translate("MainWindow", u"Grab videos effortlessly in top quality", None))
        self.youtubeURL_Lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Drop your YOUTUBE video URL here!", None))
        self.youtubeFetchVideo_Button.setText(QCoreApplication.translate("MainWindow", u"Fetch Video", None))
        self.youtubeThumbnail_Image_Label.setText("")
        self.youtube_VideoName_Label.setText("")
        self.youtube_duration_Label.setText("")
        self.youtubeDownload_Button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.youtubeFormatSelection_ComboBox.setCurrentText("")
        self.fileLocation_Label_6.setText(QCoreApplication.translate("MainWindow", u"File Location:", None))
        self.youtubeLocationURL_Label.setText(QCoreApplication.translate("MainWindow", u"c:/", None))
        self.youtubeBrowseFileLocation_Button.setText("")
        self.facebookTitle_Label.setText(QCoreApplication.translate("MainWindow", u"Facebook Downloader", None))
        self.facebookStatus_Label.setText(QCoreApplication.translate("MainWindow", u"Grab videos effortlessly in top quality, from FACEBOOK", None))
        self.url_lineedit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Drop your FACEBOOK video URL here!", None))
        self.facebookFetchVideo_Button.setText(QCoreApplication.translate("MainWindow", u"Fetch Video", None))
        self.facebookThumbnail_Image_Label.setText("")
        self.facebookVideoName_Label.setText("")
        self.facebookDuration_Label.setText("")
        self.facebookDownload_Button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.facebookFormatSelection_comboBox.setCurrentText("")
        self.fileLocation_Label_7.setText(QCoreApplication.translate("MainWindow", u"File Location:", None))
        self.facebookLocationURL_Label.setText(QCoreApplication.translate("MainWindow", u"c:/", None))
        self.facebookBowseFileLocation_Button.setText("")
        self.instagramTitle_Label.setText(QCoreApplication.translate("MainWindow", u"Instagram Downloader", None))
        self.instagramStatus_Label.setText(QCoreApplication.translate("MainWindow", u"Grab videos effortlessly in top quality, from INSTAGRAM.", None))
        self.instagramUrl_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Drop your INSTAGRAM video URL here!", None))
        self.instagramFetchVideo_Button.setText(QCoreApplication.translate("MainWindow", u"Fetch Video", None))
        self.instagramThumbnail_Image_Label.setText("")
        self.instagramVideoName_Label.setText("")
        self.instagramDuration_Label.setText("")
        self.instagramDownload_Button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.instagramFormatSelection_ComboBox.setCurrentText("")
        self.fileLocation_Label_2.setText(QCoreApplication.translate("MainWindow", u"File Location:", None))
        self.instagramLocationURL_Label.setText(QCoreApplication.translate("MainWindow", u"c:/", None))
        self.instagramBrowseFileLocation_Button.setText("")
        self.tiktokTitle_Label.setText(QCoreApplication.translate("MainWindow", u"TikTok Downloader", None))
        self.status_Label_4.setText(QCoreApplication.translate("MainWindow", u"Grab videos effortlessly in top quality, from TIKTOK.", None))
        self.ticktokURL_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Drop your TIKTOK video URL here!", None))
        self.tiktokFetchVideo_Button_6.setText(QCoreApplication.translate("MainWindow", u"Fetch Video", None))
        self.tiktokThumbnail_Image_Label.setText("")
        self.tiktokVideoName_Label.setText("")
        self.tiktokDuration_Label.setText("")
        self.tiktokDownload_Button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.tiktokFormatSelection_ComboBox.setCurrentText("")
        self.fileLocation_Label_5.setText(QCoreApplication.translate("MainWindow", u"File Location:", None))
        self.tiktokLocationURL_Label.setText(QCoreApplication.translate("MainWindow", u"c:/", None))
        self.tiktokBrowseFileLocation_Button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"We are currently working on My File page", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User of this app will be ble to access all there downloaded file here", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"We are currently working on Tools Page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User of this app will be ble to access all there downloaded file here", None))
    # retranslateUi

