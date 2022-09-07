# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VAPT.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from distutils import errors
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets

from time import sleep
import NDMS
import os
#Only for development
from pprint import pprint

from subprocess import Popen, PIPE


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 931)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/nmap_94081.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Parent_frame = QtWidgets.QFrame(self.frame)
        self.Parent_frame.setGeometry(QtCore.QRect(0, 0, 1211, 871))
        self.Parent_frame.setStyleSheet("")
        self.Parent_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Parent_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Parent_frame.setObjectName("Parent_frame")
        self.Menubar_frame = QtWidgets.QFrame(self.Parent_frame)
        self.Menubar_frame.setGeometry(QtCore.QRect(0, 0, 1211, 71))
        self.Menubar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menubar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menubar_frame.setObjectName("Menubar_frame")
        self.startstop_widget = QtWidgets.QWidget(self.Menubar_frame)
        self.startstop_widget.setGeometry(QtCore.QRect(-1, 0, 291, 71))
        self.startstop_widget.setObjectName("startstop_widget")
        self.startscanButton = QtWidgets.QPushButton(self.startstop_widget,clicked=lambda: self.startScan())
        self.startscanButton.setGeometry(QtCore.QRect(30, 10, 71, 51))
        self.startscanButton.setStyleSheet("background-color : rgb(78, 154, 6)")
        self.startscanButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Start_37108.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startscanButton.setIcon(icon1)
        self.startscanButton.setIconSize(QtCore.QSize(40, 40))
        self.startscanButton.setObjectName("startscanButton")
        self.stopscanButton = QtWidgets.QPushButton(self.startstop_widget)
        self.stopscanButton.setGeometry(QtCore.QRect(170, 10, 71, 51))
        self.stopscanButton.setStyleSheet("background-color : rgb(204, 0, 0)")
        self.stopscanButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/cancel_stop_exit_1583.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopscanButton.setIcon(icon2)
        self.stopscanButton.setIconSize(QtCore.QSize(40, 40))
        self.stopscanButton.setObjectName("stopscanButton")
        self.menubar_line = QtWidgets.QFrame(self.Menubar_frame)
        self.menubar_line.setGeometry(QtCore.QRect(280, 0, 20, 71))
        self.menubar_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.menubar_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menubar_line.setObjectName("menubar_line")
        self.line = QtWidgets.QFrame(self.Menubar_frame)
        self.line.setGeometry(QtCore.QRect(810, 0, 16, 71))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.openScanFile_Button = QtWidgets.QPushButton(self.Menubar_frame)
        self.openScanFile_Button.setGeometry(QtCore.QRect(350, 10, 81, 51))
        self.openScanFile_Button.setStyleSheet("background-color : rgb(85, 87, 83)")
        self.openScanFile_Button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/open-file_40455.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openScanFile_Button.setIcon(icon3)
        self.openScanFile_Button.setIconSize(QtCore.QSize(50, 50))
        self.openScanFile_Button.setObjectName("openScanFile_Button")
        self.exitAppButton = QtWidgets.QPushButton(self.Menubar_frame,clicked=lambda: self.exitApp())
        self.exitAppButton.setGeometry(QtCore.QRect(690, 10, 71, 51))
        self.exitAppButton.setStyleSheet("background-color : rgb(204, 0, 0)")
        self.exitAppButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/button_exit_15724.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitAppButton.setIcon(icon4)
        self.exitAppButton.setIconSize(QtCore.QSize(50, 50))
        self.exitAppButton.setObjectName("exitAppButton")
        self.osint_Button = QtWidgets.QPushButton(self.Menubar_frame)
        self.osint_Button.setGeometry(QtCore.QRect(500, 10, 89, 51))
        self.osint_Button.setText("")
        self.osint_Button.setIcon(icon)
        self.osint_Button.setIconSize(QtCore.QSize(50, 50))
        self.osint_Button.setObjectName("osint_Button")
        self.scanOutput_Tab = QtWidgets.QTabWidget(self.Parent_frame)
        self.scanOutput_Tab.setGeometry(QtCore.QRect(10, 160, 1181, 691))
        self.scanOutput_Tab.setStyleSheet("")
        self.scanOutput_Tab.setObjectName("scanOutput_Tab")
        self.scanoption_tab = QtWidgets.QWidget()
        self.scanoption_tab.setObjectName("scanoption_tab")
        self.optionwidget_1 = QtWidgets.QWidget(self.scanoption_tab)
        self.optionwidget_1.setGeometry(QtCore.QRect(10, 10, 631, 631))
        self.optionwidget_1.setStyleSheet("background-color : rgb(186, 189, 182)")
        self.optionwidget_1.setObjectName("optionwidget_1")
        self.port_widget = QtWidgets.QWidget(self.optionwidget_1)
        self.port_widget.setGeometry(QtCore.QRect(20, 30, 581, 51))
        self.port_widget.setStyleSheet("background-color :rgb(52, 101, 164)")
        self.port_widget.setObjectName("port_widget")
        self.firstport_splitter = QtWidgets.QSplitter(self.port_widget)
        self.firstport_splitter.setGeometry(QtCore.QRect(10, 10, 241, 25))
        self.firstport_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.firstport_splitter.setObjectName("firstport_splitter")
        self.firstport_label = QtWidgets.QLabel(self.firstport_splitter)
        self.firstport_label.setStyleSheet("background-color : rgb(243, 243, 243)")
        self.firstport_label.setObjectName("firstport_label")
        self.firstPort = QtWidgets.QSpinBox(self.firstport_splitter)
        self.firstPort.setStyleSheet("background-color : rgb(243, 243, 243)")
        self.firstPort.setMinimum(0)
        self.firstPort.setMaximum(65536)
        self.firstPort.setObjectName("firstPort")
        self.lastport_splitter = QtWidgets.QSplitter(self.port_widget)
        self.lastport_splitter.setGeometry(QtCore.QRect(310, 10, 261, 25))
        self.lastport_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.lastport_splitter.setObjectName("lastport_splitter")
        self.lastport_label = QtWidgets.QLabel(self.lastport_splitter)
        self.lastport_label.setStyleSheet("background-color : rgb(243, 243, 243)")
        self.lastport_label.setObjectName("lastport_label")
        self.lastPort = QtWidgets.QSpinBox(self.lastport_splitter)
        self.lastPort.setAccessibleDescription("")
        self.lastPort.setStyleSheet("background-color : rgb(243, 243, 243)")
        self.lastPort.setMaximum(65536)
        self.lastPort.setDisplayIntegerBase(10)
        self.lastPort.setObjectName("lastPort")
        self.groupBox = QtWidgets.QGroupBox(self.optionwidget_1)
        self.groupBox.setGeometry(QtCore.QRect(330, 130, 281, 461))
        self.groupBox.setStyleSheet("background-color : rgb(238, 238, 236)")
        self.groupBox.setObjectName("groupBox")
        self.Versionscan_button = QtWidgets.QRadioButton(self.groupBox)
        self.Versionscan_button.setGeometry(QtCore.QRect(40, 30, 161, 71))
        self.Versionscan_button.setObjectName("Versionscan_button")
        self.UDPscan_button = QtWidgets.QRadioButton(self.groupBox)
        self.UDPscan_button.setGeometry(QtCore.QRect(40, 290, 161, 71))
        self.UDPscan_button.setObjectName("UDPscan_button")
        self.Xmasscan_button = QtWidgets.QRadioButton(self.groupBox)
        self.Xmasscan_button.setGeometry(QtCore.QRect(40, 380, 161, 71))
        self.Xmasscan_button.setObjectName("Xmasscan_button")
        self.ACKscan_button = QtWidgets.QRadioButton(self.groupBox)
        self.ACKscan_button.setGeometry(QtCore.QRect(40, 190, 141, 71))
        self.ACKscan_button.setObjectName("ACKscan_button")
        self.Connectscan_button = QtWidgets.QRadioButton(self.groupBox)
        self.Connectscan_button.setGeometry(QtCore.QRect(40, 110, 141, 61))
        self.Connectscan_button.setObjectName("Connectscan_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.optionwidget_1)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 130, 291, 461))
        self.groupBox_2.setStyleSheet("background-color : rgb(238, 238, 236)")
        self.groupBox_2.setObjectName("groupBox_2")
        self.frag_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.frag_checkBox.setGeometry(QtCore.QRect(20, 50, 161, 81))
        self.frag_checkBox.setObjectName("frag_checkBox")
        self.savescan_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.savescan_checkBox.setGeometry(QtCore.QRect(20, 350, 161, 81))
        self.savescan_checkBox.setObjectName("savescan_checkBox")
        self.portchanger_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.portchanger_checkBox.setGeometry(QtCore.QRect(20, 150, 181, 91))
        self.portchanger_checkBox.setObjectName("portchanger_checkBox")
        self.evadedetection_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.evadedetection_checkBox.setGeometry(QtCore.QRect(20, 260, 161, 71))
        self.evadedetection_checkBox.setObjectName("evadedetection_checkBox")
        self.scripOptionsGroup = QtWidgets.QWidget(self.scanoption_tab)
        self.scripOptionsGroup.setEnabled(True)
        self.scripOptionsGroup.setGeometry(QtCore.QRect(670, 10, 491, 631))
        self.scripOptionsGroup.setAutoFillBackground(False)
        self.scripOptionsGroup.setStyleSheet("background-color : rgb(186, 189, 182)")
        self.scripOptionsGroup.setObjectName("scripOptionsGroup")
        self.scriptCateg = QtWidgets.QWidget(self.scripOptionsGroup)
        self.scriptCateg.setGeometry(QtCore.QRect(20, 120, 451, 491))
        self.scriptCateg.setStyleSheet("background-color : rgb(238, 238, 236)")
        self.scriptCateg.setObjectName("scriptCateg")
        self.defaultScript = QtWidgets.QCheckBox(self.scriptCateg)
        self.defaultScript.setGeometry(QtCore.QRect(40, 70, 91, 23))
        self.defaultScript.setChecked(False)
        self.defaultScript.setObjectName("defaultScript")
        self.vulnScript = QtWidgets.QCheckBox(self.scriptCateg)
        self.vulnScript.setGeometry(QtCore.QRect(40, 200, 101, 23))
        self.vulnScript.setObjectName("vulnScript")
        self.exploitScript = QtWidgets.QCheckBox(self.scriptCateg)
        self.exploitScript.setGeometry(QtCore.QRect(260, 340, 141, 23))
        self.exploitScript.setObjectName("exploitScript")
        self.authScript = QtWidgets.QCheckBox(self.scriptCateg)
        self.authScript.setGeometry(QtCore.QRect(40, 340, 121, 23))
        self.authScript.setObjectName("authScript")
        self.bruteScript = QtWidgets.QCheckBox(self.scriptCateg)
        self.bruteScript.setGeometry(QtCore.QRect(250, 70, 141, 23))
        self.bruteScript.setObjectName("bruteScript")
        self.menubar_line_2 = QtWidgets.QFrame(self.scriptCateg)
        self.menubar_line_2.setGeometry(QtCore.QRect(190, 60, 20, 351))
        self.menubar_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.menubar_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menubar_line_2.setObjectName("menubar_line_2")
        self.fuzzScript = QtWidgets.QCheckBox(self.scriptCateg)
        self.fuzzScript.setGeometry(QtCore.QRect(250, 200, 141, 23))
        self.fuzzScript.setObjectName("fuzzScript")
        self.script_implementation_label = QtWidgets.QLabel(self.scripOptionsGroup)
        self.script_implementation_label.setGeometry(QtCore.QRect(90, 30, 291, 41))
        self.script_implementation_label.setStyleSheet("background-color : rgb(52, 101, 164)")
        self.script_implementation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.script_implementation_label.setObjectName("script_implementation_label")
        self.scanOutput_Tab.addTab(self.scanoption_tab, "")
        self.scanoutput_tab = QtWidgets.QWidget()
        self.scanoutput_tab.setObjectName("scanoutput_tab")
        self.displayresults = QtWidgets.QScrollArea(self.scanoutput_tab)
        self.displayresults.setGeometry(QtCore.QRect(10, 10, 1161, 641))
        self.displayresults.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.displayresults.setWidgetResizable(True)
        self.displayresults.setObjectName("displayresults")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1159, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scanResult_TextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.scanResult_TextEdit.setGeometry(QtCore.QRect(10, 10, 1141, 621))
        self.scanResult_TextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scanResult_TextEdit.setUndoRedoEnabled(False)
        self.scanResult_TextEdit.setReadOnly(True)
        self.scanResult_TextEdit.setObjectName("scanResult_TextEdit")
        self.displayresults.setWidget(self.scrollAreaWidgetContents)
        self.scanOutput_Tab.addTab(self.scanoutput_tab, "")
        self.osintOutput_tab = QtWidgets.QWidget()
        self.osintOutput_tab.setObjectName("osintOutput_tab")
        self.scrollArea = QtWidgets.QScrollArea(self.osintOutput_tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 1151, 641))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1149, 639))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.osintResult_TextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.osintResult_TextEdit.setGeometry(QtCore.QRect(10, 10, 1131, 621))
        self.osintResult_TextEdit.setReadOnly(True)
        self.osintResult_TextEdit.setObjectName("osintResult_TextEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.scanOutput_Tab.addTab(self.osintOutput_tab, "")
        self.webOutput_tab = QtWidgets.QWidget()
        self.webOutput_tab.setObjectName("webOutput_tab")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.webOutput_tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 1151, 631))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1149, 629))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.webResult_TextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_4)
        self.webResult_TextEdit.setGeometry(QtCore.QRect(10, 10, 1131, 611))
        self.webResult_TextEdit.setTabChangesFocus(False)
        self.webResult_TextEdit.setDocumentTitle("")
        self.webResult_TextEdit.setReadOnly(True)
        self.webResult_TextEdit.setObjectName("webResult_TextEdit")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.scanOutput_Tab.addTab(self.webOutput_tab, "")
        self.scaninput_widget = QtWidgets.QWidget(self.Parent_frame)
        self.scaninput_widget.setGeometry(QtCore.QRect(10, 80, 1201, 61))
        self.scaninput_widget.setObjectName("scaninput_widget")
        self.splitter = QtWidgets.QSplitter(self.scaninput_widget)
        self.splitter.setGeometry(QtCore.QRect(40, 20, 611, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.target_label = QtWidgets.QLabel(self.splitter)
        self.target_label.setWordWrap(False)
        self.target_label.setObjectName("target_label")
        self.target_input = QtWidgets.QLineEdit(self.splitter)
        self.target_input.setObjectName("target_input")
        self.splitter_2 = QtWidgets.QSplitter(self.scaninput_widget)
        self.splitter_2.setGeometry(QtCore.QRect(730, 20, 421, 25))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.scanspeed_label = QtWidgets.QLabel(self.splitter_2)
        self.scanspeed_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.scanspeed_label.setTextFormat(QtCore.Qt.AutoText)
        self.scanspeed_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scanspeed_label.setWordWrap(True)
        self.scanspeed_label.setObjectName("scanspeed_label")
        self.scanspeed = QtWidgets.QComboBox(self.splitter_2)
        self.scanspeed.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.scanspeed.setTabletTracking(False)
        self.scanspeed.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scanspeed.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.scanspeed.setAcceptDrops(True)
        self.scanspeed.setEditable(False)
        self.scanspeed.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.scanspeed.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.scanspeed.setModelColumn(0)
        self.scanspeed.setObjectName("scanspeed")
        self.scanspeed.addItem("")
        self.scanspeed.addItem("")
        self.scanspeed.addItem("")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_target_file = QtWidgets.QAction(MainWindow)
        self.actionopen_target_file.setObjectName("actionopen_target_file")
        self.actionsave_scan = QtWidgets.QAction(MainWindow)
        self.actionsave_scan.setObjectName("actionsave_scan")
        self.actionopen_scan_file = QtWidgets.QAction(MainWindow)
        self.actionopen_scan_file.setObjectName("actionopen_scan_file")
        self.actionfind_out_more = QtWidgets.QAction(MainWindow)
        self.actionfind_out_more.setObjectName("actionfind_out_more")
        self.actionlog = QtWidgets.QAction(MainWindow)
        self.actionlog.setObjectName("actionlog")
        self.menuView.addAction(self.actionlog)
        self.menuHelp.addAction(self.actionfind_out_more)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.scanOutput_Tab.setCurrentIndex(3)
        self.scanspeed.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CYNIX NETWORK AND VULNERABILITY SCANNER"))
        self.osint_Button.setWhatsThis(_translate("MainWindow", "Discover more information about target(OSINT)"))
        self.firstport_label.setText(_translate("MainWindow", "First Port"))
        self.lastport_label.setText(_translate("MainWindow", "Last Port"))
        self.groupBox.setTitle(_translate("MainWindow", "Scan Type"))
        self.Versionscan_button.setText(_translate("MainWindow", "Protocol scan"))
        self.UDPscan_button.setText(_translate("MainWindow", "UDP scan"))
        self.Xmasscan_button.setText(_translate("MainWindow", "Xmas scan"))
        self.ACKscan_button.setText(_translate("MainWindow", "ACK scan"))
        self.Connectscan_button.setText(_translate("MainWindow", "Connect scan"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Scan Flag"))
        self.frag_checkBox.setText(_translate("MainWindow", "Fragment Scan"))
        self.savescan_checkBox.setText(_translate("MainWindow", "Enable IPv6"))
        self.portchanger_checkBox.setText(_translate("MainWindow", "Random source port"))
        self.evadedetection_checkBox.setText(_translate("MainWindow", "Evade detections"))
        self.defaultScript.setText(_translate("MainWindow", "Default "))
        self.vulnScript.setText(_translate("MainWindow", "Vulnerable "))
        self.exploitScript.setText(_translate("MainWindow", "Exploit "))
        self.authScript.setText(_translate("MainWindow", "Authentication"))
        self.bruteScript.setText(_translate("MainWindow", "Bruteforce"))
        self.fuzzScript.setText(_translate("MainWindow", "Fuzzer"))
        self.script_implementation_label.setText(_translate("MainWindow", "SCRIPT iMPLETMENTATIONS"))
        self.scanOutput_Tab.setTabText(self.scanOutput_Tab.indexOf(self.scanoption_tab), _translate("MainWindow", "Scan Options"))
        self.scanResult_TextEdit.setPlaceholderText(_translate("MainWindow", "RESULTS FROM SCANS WILL APPEAR HERE."))
        self.scanOutput_Tab.setTabText(self.scanOutput_Tab.indexOf(self.scanoutput_tab), _translate("MainWindow", "Scan Output"))
        self.osintResult_TextEdit.setPlaceholderText(_translate("MainWindow", "ANY  SERVICES ON THE INTERNET THAT MAY FURTHER EXPOSE THEIR SYSTEMS WILL BE DISPLAYED HERE IF AVAILABLE"))
        self.scanOutput_Tab.setTabText(self.scanOutput_Tab.indexOf(self.osintOutput_tab), _translate("MainWindow", "OSINT OUTPUT"))
        self.webResult_TextEdit.setPlaceholderText(_translate("MainWindow", "ANY SUB DOMAIN AND WEB DIRECTORIES DISCOVERED OF A POSSIBLE WEB SERVER TARGET WILL BE DISPLAYED HERE"))
        self.scanOutput_Tab.setTabText(self.scanOutput_Tab.indexOf(self.webOutput_tab), _translate("MainWindow", "WEB ENUMERATIONS"))
        self.target_label.setText(_translate("MainWindow", "Target IP or Url: "))
        self.scanspeed_label.setText(_translate("MainWindow", "Scan speed : "))
        self.scanspeed.setCurrentText(_translate("MainWindow", "high"))
        self.scanspeed.setItemText(0, _translate("MainWindow", "high"))
        self.scanspeed.setItemText(1, _translate("MainWindow", "moderate"))
        self.scanspeed.setItemText(2, _translate("MainWindow", "low"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionopen_target_file.setText(_translate("MainWindow", " open target file"))
        self.actionsave_scan.setText(_translate("MainWindow", "save scan"))
        self.actionopen_scan_file.setText(_translate("MainWindow", "open scan file"))
        self.actionfind_out_more.setText(_translate("MainWindow", "find out more"))
        self.actionlog.setText(_translate("MainWindow", "scan logs"))

    def scriptEngine(self):
        scriptList = {}
        if self.defaultScript.isChecked() == True:
            scriptList['default'] = 'default'

        if self.vulnScript.isChecked() == True:
            scriptList['vuln'] = 'vuln'

        if self.authScript.isChecked() == True:
            scriptList['auth']  = 'auth'

        if self.exploitScript.isChecked() == True:
            scriptList['exploit'] = 'exploit'

        if self.fuzzScript.isChecked() == True:
            scriptList['fuzz']  =  'fuzz'

        if self.bruteScript.isChecked() == True:
           scriptList.append('intrusive')

        return scriptList


    # Function to return scan type
    def ScanType(self):
        if self.Versionscan_button.isChecked():
            scan_type   =   '-sV'
        elif self.ACKscan_button.isChecked():
            scan_type   =   '-sA'
        elif self.UDPscan_button.isChecked():
            scan_type   =   '-sU'
        elif self.Xmasscan_button.isChecked():
            scan_type   =   '-sX'
        elif self.Connectscan_button.isChecked():
            scan_type   =   '-sS'    
        else:
            scan_type   =   '-sT'
        return scan_type

    #Function to retrieve Scan Flags
    def scanFlags(self):
        scanFlagsets = {}
        if self.savescan_checkBox.isChecked():
            scanFlagsets['savescan'] = '-6'
        else:
            scanFlagsets = scanFlagsets
        if self.frag_checkBox.isChecked():
            scanFlagsets['frag']= '-f'
        else:
            scanFlagsets = scanFlagsets
        if self.evadedetection_checkBox.isChecked():
            scanFlagsets['evader'] = '--badsum'
        else:
            scanFlagsets = scanFlagsets
        if self.portchanger_checkBox.isChecked():
            scanFlagsets['randomize'] = '-g'
        else:
            scanFlagsets = scanFlagsets

        return scanFlagsets


    # Function to set scan speed
    def scanSpeed(self):
        # selectedSpeed   = self.scanspeed_comboBox.currentText()
        speed = ''
        if self.scanspeed.currentText() == 'low':
            speed = '-T1'
        elif self.scanspeed.currentText() == 'moderate':
            speed = '-T3'
        elif self.scanspeed.currentText() == 'high':
            speed = '-T5'

        return speed


    def get_target(self):
        target_unstripped = self.target_input.text()
        target  = target_unstripped.strip()


        return target


    # Function to get port range
    def portRange(self):
        startPort   = self.firstPort.value()
        endPort     = self.lastPort.value()

        if not  startPort:
            pass
        elif not endPort:
            pass
        else:
            port = 1000

        return port


    # Function to identify root priveleges
    def is_root():
        if os.geteuid() == 0:
            return True
        else:
            return False


    def exitApp(self):
        QtWidgets.QApplication.instance().quit()
    
    
    def startScan(self):
        target    = self.get_target()
        # root      = self.is_root()
        scanSpeed = self.scanSpeed()
        scanFlag  = self.scanFlags()
        scanType  = self.ScanType()
        scriptType = self.scriptEngine()

        self.scanObject = Scans(target,scanSpeed,scanFlag,scanType,scriptType)
        self.scanThread1 = QtCore.QThread()
        self.scanObject.moveToThread(self.scanThread1)
        self.scanObject.sendScanResult.connect(self.setTextEdit, type=QtCore.Qt.QueuedConnection)
        app.processEvents()
        self.scanObject.finished.connect(self.scanThread1.quit)
        self.scanThread1.started.connect(self.scanObject.run)
        self.scanResult_TextEdit.clear()
        self.scanResult_TextEdit.insertPlainText('Scanning in Progress.......')
        self.scanThread1.start()
        
        
    def setTextEdit(self,val):
        self.scanResult_TextEdit.clear()
        self.scanResult_TextEdit.setText(val)
    

        
"""
A Class t to create a thread that performs scans and inject into 

the scanoutput_TextEdit UI
"""
class Scans(QtCore.QObject):
        finished        = QtCore.pyqtSignal() # Determine if scan is finished
        sendScanResult  = QtCore.pyqtSignal(str) #Emit scan results
        errors          = QtCore.pyqtSignal(str)
        inProgress      = False
        

        def __init__(self,target,scanSpeed,scanFlag,scanType,scriptType):
            super().__init__()
            self.target     = target 
            self.scanSpeed  = scanSpeed
            self.scanFlag   = scanFlag
            self.scanType   = scanType
            self.scriptType = scriptType

        # Perform an Osint scan using zoomeye
        def osintScan(self):
            osintTarget     = self.target
            api = str("D6106079-BBA2-06A96-93b5-BCe0cb1fa8f")

            initailize      = Popen(['zoomeye' , 'init', '-apikey',api],stdout=PIPE,stderr=PIPE)
            ini_stdout,ini_stderr   = initailize.communicate()
            if ini_stdout:
                pass
            else:
                self.errors.emit(ini_stderr.decode())

            osintScanner    = Popen(['zoomeye' , 'search','kstu.edu.gh'],stdout=PIPE,stderr=PIPE)
            osint_stdout,osint_stderr = osintScanner.communicate()

            if osint_stdout:
                self.sendScanResult(osint_stdout.decode())
            else:
                self.errors.emit(osint_stderr.decode())


        def run(self):
        
            print('target is ', self.target)
            print('scanSpeed is ',self.scanSpeed)
            print('scanFlag is ', self.scanFlag)
            print('scanType is ', self.scanType)
            print('script Engine used is ' , self.scriptType)

            try: 
               #if user is root or admininistrator
                if True:
                    # If no Flags and Scripts were selected
                    if  not self.scanFlag and  not self.scriptType: 
                        command = '/usr/bin/nmap'                       
                        process = Popen([command,self.target,self.scanType], stdout=PIPE,stderr=PIPE)
                        stdout,stderr   = process.communicate()      
                        # print result : if no error result is displayed or error message
                        if process.wait() == 0:
                            self.sendScanResult.emit(stdout.decode())
                        else:
                            self.sendScanResult.emit(stderr.decode())
                        
                        app.processEvents()
                        self.finished.emit()
                        print('Host scanning process completed..........')
                        QtWidgets.QApplication.sendPostedEvents()
                        QtWidgets.QApplication.processEvents()  
                        self.finished.emit()

                    elif self.scanFlag or self.scriptType:
                        # set nmap argument variables if exist in dictionary
                        if 'frag' in self.scanFlag:
                            frag        = self.scanFlag['frag']
                        if 'savescan' in self.scanFlag:
                            save        = self.scanFlag['savescan']
                        if 'evader' in self.scanFlag:
                            evader      = self.scanFlag['evader']
                        if 'version' in self.scanFlag:
                            randomer    = self.scanFlag['randomize']

                        if frag:
                            command = '/usr/bin/nmap'
                            print(self.scriptType)
                            process = Popen([command,self.target,frag,], stdout=PIPE,stderr=PIPE)
                            stdout, stderr = process.communicate()
                            # print result : if no error result is displayed or error message
                            if process.wait() == 0:
                                self.sendScanResult.emit(stdout.decode())
                            else:
                                self.sendScanResult.emit(stderr.decode())

                            print(process.poll()) # identify is the process is still running
                           
                            app.processEvents()
                            self.finished.emit()
                        
                        elif not frag and save:
                            # scanResult = scanner.scan(target, scanSpeed, scanType,save)
                            pass
                        elif (not frag and not save) and randomer:
                            # scanResult = scanner.scan(target, scanSpeed, scanType, evad)
                            command = '/usr/bin/nmap'
                            print(self.scriptType)
                            process = Popen([command,self.target,'{a} {b}'.format(a=randomer,b = 53),], stdout=PIPE,stderr=PIPE)
                            stdout, stderr = process.communicate()
                            # print result : if no error result is displayed or error message
                            if process.wait() == 0:
                                self.sendScanResult.emit(stdout.decode())
                            else:
                                self.sendScanResult.emit(stderr.decode())

                            print(process.poll()) # identify is the process is still running
                           
                            app.processEvents()
                            self.finished.emit()
                            pass
                        elif (not frag and not save and not randomer):
                            # scanResult = scanner.scan(target, scanSpeed, scanType,delay)tableView
                            pass
                else:
                    print('sorry you need root priveleges')
            except Exception as e:
                print(e)   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
