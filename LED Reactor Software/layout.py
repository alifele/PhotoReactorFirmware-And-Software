# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 331, 221))
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 311, 181))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.LED = QtWidgets.QWidget()
        self.LED.setObjectName("LED")
        self.gridLayout = QtWidgets.QGridLayout(self.LED)
        self.gridLayout.setObjectName("gridLayout")
        self.RedLED = QtWidgets.QRadioButton(self.LED)
        self.RedLED.setObjectName("RedLED")
        self.gridLayout.addWidget(self.RedLED, 0, 0, 1, 1)
        self.IntensityLineEdit = QtWidgets.QLineEdit(self.LED)
        self.IntensityLineEdit.setObjectName("IntensityLineEdit")
        self.gridLayout.addWidget(self.IntensityLineEdit, 6, 1, 1, 1)
        self.OrangeLED = QtWidgets.QRadioButton(self.LED)
        self.OrangeLED.setObjectName("OrangeLED")
        self.gridLayout.addWidget(self.OrangeLED, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.LED)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.GreenLED = QtWidgets.QRadioButton(self.LED)
        self.GreenLED.setObjectName("GreenLED")
        self.gridLayout.addWidget(self.GreenLED, 4, 0, 1, 1)
        self.IntensityBar = QtWidgets.QSlider(self.LED)
        self.IntensityBar.setOrientation(QtCore.Qt.Horizontal)
        self.IntensityBar.setObjectName("IntensityBar")
        self.gridLayout.addWidget(self.IntensityBar, 5, 1, 1, 1)
        self.BlueLED = QtWidgets.QRadioButton(self.LED)
        self.BlueLED.setObjectName("BlueLED")
        self.gridLayout.addWidget(self.BlueLED, 1, 0, 1, 1)
        self.WhiteLED = QtWidgets.QRadioButton(self.LED)
        self.WhiteLED.setObjectName("WhiteLED")
        self.gridLayout.addWidget(self.WhiteLED, 1, 1, 1, 1)
        self.tabWidget.addTab(self.LED, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.FanOn = QtWidgets.QRadioButton(self.tab_2)
        self.FanOn.setGeometry(QtCore.QRect(20, 20, 112, 23))
        self.FanOn.setObjectName("FanOn")
        self.FanOff = QtWidgets.QRadioButton(self.tab_2)
        self.FanOff.setGeometry(QtCore.QRect(20, 50, 112, 23))
        self.FanOff.setObjectName("FanOff")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.GasInOn = QtWidgets.QRadioButton(self.tab)
        self.GasInOn.setGeometry(QtCore.QRect(20, 20, 112, 23))
        self.GasInOn.setObjectName("GasInOn")
        self.GasInOff = QtWidgets.QRadioButton(self.tab)
        self.GasInOff.setGeometry(QtCore.QRect(20, 50, 112, 23))
        self.GasInOff.setObjectName("GasInOff")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(120, 20, 81, 21))
        self.label.setObjectName("label")
        self.GasFlowRateLineEdit = QtWidgets.QLineEdit(self.tab)
        self.GasFlowRateLineEdit.setGeometry(QtCore.QRect(120, 40, 113, 25))
        self.GasFlowRateLineEdit.setObjectName("GasFlowRateLineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.WaterInOn = QtWidgets.QRadioButton(self.tab_3)
        self.WaterInOn.setGeometry(QtCore.QRect(20, 20, 112, 23))
        self.WaterInOn.setObjectName("WaterInOn")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 81, 21))
        self.label_2.setObjectName("label_2")
        self.WaterFlowRateLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.WaterFlowRateLineEdit.setGeometry(QtCore.QRect(120, 40, 113, 25))
        self.WaterFlowRateLineEdit.setObjectName("WaterFlowRateLineEdit")
        self.WaterInOff = QtWidgets.QRadioButton(self.tab_3)
        self.WaterInOff.setGeometry(QtCore.QRect(20, 50, 112, 23))
        self.WaterInOff.setObjectName("WaterInOff")
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 230, 191, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.StatusText = QtWidgets.QTextBrowser(self.groupBox_2)
        self.StatusText.setGeometry(QtCore.QRect(10, 30, 171, 111))
        self.StatusText.setObjectName("StatusText")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 131, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.TurnOnButt = QtWidgets.QPushButton(self.groupBox_3)
        self.TurnOnButt.setGeometry(QtCore.QRect(20, 50, 89, 51))
        self.TurnOnButt.setObjectName("TurnOnButt")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 0, 481, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.SpectrumViewer = QtWidgets.QGraphicsView(self.groupBox_4)
        self.SpectrumViewer.setGeometry(QtCore.QRect(10, 30, 461, 181))
        self.SpectrumViewer.setObjectName("SpectrumViewer")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(350, 230, 481, 151))
        self.groupBox_5.setObjectName("groupBox_5")
        self.HelpText = QtWidgets.QTextBrowser(self.groupBox_5)
        self.HelpText.setGeometry(QtCore.QRect(10, 30, 461, 111))
        self.HelpText.setObjectName("HelpText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Configueation"))
        self.RedLED.setText(_translate("MainWindow", "Red"))
        self.OrangeLED.setText(_translate("MainWindow", "Orange"))
        self.label_3.setText(_translate("MainWindow", "Inensity:"))
        self.GreenLED.setText(_translate("MainWindow", "Green"))
        self.BlueLED.setText(_translate("MainWindow", "Blue"))
        self.WhiteLED.setText(_translate("MainWindow", "White"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LED), _translate("MainWindow", "LEDs"))
        self.FanOn.setText(_translate("MainWindow", "On"))
        self.FanOff.setText(_translate("MainWindow", "Off"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Fans"))
        self.GasInOn.setText(_translate("MainWindow", "On"))
        self.GasInOff.setText(_translate("MainWindow", "Off"))
        self.label.setText(_translate("MainWindow", "FlowRate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gas input"))
        self.WaterInOn.setText(_translate("MainWindow", "On"))
        self.label_2.setText(_translate("MainWindow", "FlowRate"))
        self.WaterInOff.setText(_translate("MainWindow", "Off"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Water Input"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status"))
        self.StatusText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Color: <span style=\" color:#204a87;\">Red</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Intensity (8bit): <span style=\" color:#204a87;\">32</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">intensity (watt): <span style=\" color:#204a87;\">0.04</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Door: <span style=\" color:#204a87;\">Closed!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fans: <span style=\" color:#204a87;\">On!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WaterInput: <span style=\" color:#204a87;\">On!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GasInput: <span style=\" color:#204a87;\">On!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Action!"))
        self.TurnOnButt.setText(_translate("MainWindow", "Turn ON"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Spectrum"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Help"))
