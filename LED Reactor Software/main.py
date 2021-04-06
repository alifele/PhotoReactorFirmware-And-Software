import sys
from layout import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import time
import serial


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status = 'off'
        self.color = "none" #Red, Green, Blue, Orange, White
        self.intensity = 2
        self.noSelectedColorFlag=0
        self.setUiElements()
        self.show()


    def setUiElements(self):
        self.UARTConnection()
        self.setTurnOnButt()
        self.setIntensityBar()
        self.setIntensityLineEdit()
        self.ActionStatusBox()

    def UARTConnection(self):
        print("Stablishing Connection with MCU ...")
        self.serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        time.sleep(0.5)
        print("Connection Stablished!")

    def setIntensityLineEdit(self):
        self.ui.IntensityLineEdit.setText('45')
        self.ui.IntensityLineEdit.returnPressed.connect(self.ActionIntensityLineEdit)
    def ActionIntensityLineEdit(self):
        if self.status == 'off':
            value = int(self.ui.IntensityLineEdit.text())
            self.ui.IntensityBar.setValue(value)
        else:
            value = int(self.ui.IntensityLineEdit.text())
            self.ui.IntensityBar.setValue(value)
            _translate = QtCore.QCoreApplication.translate
            self.AutomaticTurnOff()
            time.sleep(0.1)
            self.ui.StatusText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status:<span style=\" color:red;\"> System is OFF</span></p>\n"))


    def setIntensityBar(self):
        self.ui.IntensityBar.setTickPosition(3)
        self.ui.IntensityBar.setTickInterval(10)
        self.ui.IntensityBar.setMinimum(0)
        self.ui.IntensityBar.setMaximum(255)
        self.ui.IntensityBar.setValue(45)
        self.ui.IntensityBar.valueChanged.connect(self.ActionIntensityBar)
    def ActionIntensityBar(self):
        if self.status == 'off':
            self.ui.IntensityLineEdit.setText(str(self.ui.IntensityBar.value()))
        else:
            self.ui.IntensityLineEdit.setText(str(self.ui.IntensityBar.value()))
            _translate = QtCore.QCoreApplication.translate
            self.AutomaticTurnOff()
            time.sleep(0.1)
            self.ui.StatusText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status:<span style=\" color:red;\"> System is OFF</span></p>\n"))

    def AutomaticTurnOff(self):
        self.ui.TurnOnButt.setText('Turn ON')
        self.status = "off"
        print("Turning Off the System...")
        self.serialPort.write(b'stop')
        time.sleep(0.5)
        print("System is Turned Off!")
        print("Select your configuration and press TurnOn again! ...")



    def setTurnOnButt(self):
        self.ui.TurnOnButt.clicked.connect(self.ActionTurnOnButt)
    def ActionTurnOnButt(self):
        if self.status == 'off': # Turn On System
            self.noSelectedColorFlag = 0
            self.ui.TurnOnButt.setText('Turn OFF')
            self.status = 'on'
            self.getSelectedColor()
            self.getIntensity()
            self.ActionStatusBox()
            if self.noSelectedColorFlag==0:
                self.sendDataToMCU()
        else: # Turn Off System
            self.ui.TurnOnButt.setText('Turn ON')
            self.status = "off"
            self.ActionStatusBox()




    def sendDataToMCU(self):
        if self.status == 'on':
            self.serialPort.write(b"start")
            time.sleep(0.2)
            print("start is sent!")
            # Now Sending the Color 1,2,3,4,5 -> R,G,B,O,W
            if self.color == 'red':
                colorval = b'1'
            if self.color == 'gree':
                colorval = b'2'
            if self.color == 'blue':
                colorval = b'3'
            if self.color == 'orange':
                colorval = b'4'
            if self.color == 'white':
                colorval = b'5'
            self.serialPort.write(colorval)

            #Now Sending the intensity as 8 bit number. Note that it should be in b' ' format
            intensityval = self.intensity
            intensityByte = bytes(str(self.intensity), 'ascii')
            self.serialPort.write(intensityByte)
            time.sleep(0.2)
            print("intensity is sent!")
            time.sleep(0.5)
            print("LEDs are Now On")
            print("Press TurnOff to turn the LEDs off")





    def ActionStatusBox(self):
        _translate = QtCore.QCoreApplication.translate
        if self.status == "off":
            print("Turning Off the System...")
            self.serialPort.write(b'stop')
            time.sleep(0.5)
            print("System is Turned Off!")
            print("Select your configuration and press TurnOn again! ...")
            self.ui.StatusText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status:<span style=\" color:red;\"> System is OFF</span></p>\n"))
        else:
            if self.color == 'none':
                self.ui.StatusText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status:<span style=\" color:red;\"> No Color Selected</span></p>\n"))
                self.status = 'off'
                self.ui.TurnOnButt.setText('Turn ON')
                self.noSelectedColorFlag=1

            else:
                self.Color = self.color
                if self.color == "white":
                    self.Color = 'gray'
                self.ui.StatusText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status: <span style=\" color:green;\">" + "system is ON"+ "</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Color: <span style=\" color:" + self.Color + ";\">" + self.color + "</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Intensity (8bit): <span style=\" color:#204a87;\">" + str(self.intensity) + "</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">intensity (watt): <span style=\" color:#204a87;\">0.04</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Door: <span style=\" color:#204a87;\">Closed!</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fans: <span style=\" color:#204a87;\">On!</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WaterInput: <span style=\" color:#204a87;\">On!</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GasInput: <span style=\" color:#204a87;\">On!</span></p>\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.color = "white"

    def getIntensity(self):
        self.intensity = self.ui.IntensityBar.value()
    def getSelectedColor(self):
        if self.ui.RedLED.isChecked():
            self.color = 'red'
        if self.ui.GreenLED.isChecked():
            self.color = 'green'
        if self.ui.BlueLED.isChecked():
            self.color = 'blue'
        if self.ui.OrangeLED.isChecked():
            self.color = 'orange'
        if self.ui.WhiteLED.isChecked():
            self.color = 'white'



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())
