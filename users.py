# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import json
import re
import time

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QDateTimeEdit

import os
import sys
import base64
import random
from urllib import parse







class Ui_Dialog(QWidget):

# --------------------------ui模块--------------------------------------------------
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 700)


        self.msgBox = QMessageBox()#创建弹出框

        self.mongo = QtWidgets.QPushButton(Dialog)
        self.mongo.setGeometry(QtCore.QRect(10, 40, 111, 31))
        self.mongo.setObjectName("pushButton")

        self.jupy = QtWidgets.QPushButton(Dialog)
        self.jupy.setGeometry(QtCore.QRect(160, 40, 101, 31))
        self.jupy.setObjectName("pushButton_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 270, 451, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet('color:#BA55D3')
        self.lineEdit_2.setStyleSheet("background:transparent;border-width:0.5;border-style:outset;color:#BA55D3;border-color:#00008B;")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 220, 451, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background:transparent;border-width:0.5;border-style:outset;color:#FF0000;border-color:#00008B;")


        self.base_str = QtWidgets.QPushButton(Dialog)
        self.base_str.setGeometry(QtCore.QRect(510, 220, 131, 41))
        self.base_str.setObjectName("pushButton_4")

        self.str_base = QtWidgets.QPushButton(Dialog)
        self.str_base.setGeometry(QtCore.QRect(510, 270, 131, 41))
        self.str_base.setObjectName("pushButton_5")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(480, 0, 256, 192))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 80, 100, 111))
        self.textBrowser_2.setObjectName("textBrowser_2")#温度

        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(110, 110, 430,111))
        self.textBrowser_4.setObjectName("textBrowser_4")#符号

        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(90, 80, 41, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")#风向

        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(70, 160, 420, 50))
        self.textBrowser_6.setObjectName("textBrowser_6")  # 风向

        self.auth = QtWidgets.QPushButton(Dialog)
        self.auth.setGeometry(QtCore.QRect(360, 600, 150, 40))
        self.auth.setObjectName("auth")

        self.texttime = QtWidgets.QTextBrowser(Dialog)
        self.texttime.setGeometry(QtCore.QRect(280, 40, 200, 50))
        self.texttime.setObjectName("texttime")  # 时间

        self.texttime.setStyleSheet('background:transparent;border-width:0;border-style:outset;color:#00008B')

        self.wx = QtWidgets.QLabel(Dialog)
        self.wx.setGeometry(QtCore.QRect(500, 530, 150, 150))


        jpg = QPixmap(r'C:\Users\zq\Desktop\Project\ceshi\01-5.jpg').scaled(self.wx.width(), self.wx.height())
        self.wx.setPixmap(jpg)
        self.wx.setStyleSheet('background:transparent;border-width:0;border-style:outset;')

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.retranslateUi(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小工具"))
        Dialog.setWindowIcon(QIcon(r'C:\Users\zq\Desktop\Project\ico\ooopic_1548575135.ico'))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(
            QPixmap(r"C:\Users\zq\Desktop\Project\ceshi\01-4.jpg").scaled(Dialog.width(), Dialog.height())))
        Dialog.setPalette(palette)

        self.mongo.setText(_translate("Dialog", "启动mongo"))
        self.mongo.clicked.connect(lambda:Dialog.yunxing(2,))
        self.auth.setText(_translate("Dialog", "*作者*"))
        self.auth.clicked.connect(self.auth_qq)

        self.jupy.setText(_translate("Dialog", "启动jupyter"))


        self.jupy.clicked.connect(lambda:Dialog.yunxing(1,))

        self.base_str.setText(_translate("Dialog", "解码base64"))
        self.base_str.clicked.connect(self.b64_str)

        self.str_base.setText(_translate("Dialog", "转码base64"))
        self.str_base.clicked.connect(self.str_b64)


        self.jupy.setStyleSheet('QPushButton{background-Color:#00FA9A}')
        self.mongo.setStyleSheet('QPushButton{background-Color:#00FA9A}')
        self.base_str.setStyleSheet('QPushButton{background-Color:#00FFFF}')
        self.str_base.setStyleSheet('QPushButton{background-Color:#00FFFF}')
        self.auth.setStyleSheet('QPushButton{background-Color:	#FF0000;background:transparent;border-width:0;border-style:outset;color:#00008B}')
        self.auth.setFont(QFont("Mongolian Baiti", 20, QFont.Bold))

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.showtime)
        self.timer.start()
        self.run_spider()
#--------------------------作者函数--------------------------------------------------
    def auth_qq(self):
        QMessageBox.question(self, 'waring', '仅供学习使用',
                             QMessageBox.Yes, QMessageBox.Yes)


    def b64_str(self):
        """
        解码
        :param input_b64:
        :return:
        """
        input_b64 = self.lineEdit_3.text()

        try:

            str_b6 = base64.b64decode(input_b64).decode(encoding='utf-8')
            self.lineEdit_2.setText(str_b6)

        except:

            QMessageBox.question(self, 'waring', '不是base64编码',
                                 QMessageBox.Yes , QMessageBox.Yes)

    def str_b64(self):
        """
        解码
        :param input_b64:
        :return:
        """
        input_b64 = self.lineEdit_2.text()

        b64_str = base64.b64encode(input_b64.encode('utf-8'))

        self.lineEdit_3.setText((b64_str).decode('utf-8'))

    def showtime(self):
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        test = self.dateEdit.text()
        self.texttime.setText(test)

        self.texttime.setFont(QFont("Mongolian Baiti", 11, QFont.Bold))

#--------------------------爬虫模块--------------------------------------------------

    def run_spider(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
        }
        url1 = 'https://mat1.gtimg.com/pingjs/ext2020/weather/2017/scripts/main-b0d370c158.js'

        resw = requests.get(url=url1, headers=headers)
        resw.encoding = 'utf-8'

        sf = re.search(r'"(//apis.map.qq.com/.*?)",', resw.text).groups(1)[0]
        a = random.random()
        num = int(a * (10 ** 16))
        times = int(time.time())
        par = "jQuery11130%s_%s"%(num,times)
        city_info = requests.get(url="http:" + sf+"&callback="+par+"&_%s"%(times+1))


        new_str = par+"&&"+par+'\('


        js = re.sub(new_str, "", city_info.text).strip(')')
        result = json.loads(js)
        current_ip = result['result']['ip']
        province = result['result']['ad_info']['province']
        city = result['result']['ad_info']['city']
        district = result['result']['ad_info']['district']
        adcode = result['result']['ad_info']['adcode']

        ti = times+1
        self.weather(province,city,par,ti)

        self.textBrowser.setText("    IP：%s   \n 来自：%s %s %s \n 邮编：%s"%(current_ip, province, city, district, adcode))

        self.textBrowser.setFont(QFont("Mongolian Baiti",10,QFont.Bold))
        self.textBrowser.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:#9932CC")

    def weather(self,provinces,city,par,ti):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
            "Referer": "https://tianqi.qq.com/index.htm?dc212.htm"
        }
        url = 'https://wis.qq.com/weather/common'
        params={
            "source": "pc",
            # "weather_type": "observe|forecast_1h|forecast_24h|index|alarm|limit|tips|rise",
            "weather_type":'forecast_1h|observe|air|tips',
            "province": "%s"%provinces,
            "city": "%s"%city

            # "callback": "%s"%par,
            # "_":"%s"%ti
        }
        response = requests.get(url=url,params=params,headers=headers)

        response  = json.loads(re.sub('jQuery1113045821053825236335_1550813982681\(', '', response.text).strip(')'))['data']

        degree = response['observe']['degree']#温度
        humidity = response['observe']['humidity']  # 湿度
        wind_power = response['observe']['wind_power']  # 风级
        weather = response['observe']['weather']  # 多云
        wind_direction = response['forecast_1h']['0']['wind_direction']  # 风风向
        weather_short = response['air']['aqi_name']  # 霾


        tips1= response['tips']['observe']['0']
        tips2 = response['tips']['observe']['1']


        self.textBrowser_6.setText("📢 "+tips1+"  "+tips2)
        self.textBrowser_6.setFont(QFont("Mongolian Baiti", 10, QFont.Bold))
        self.textBrowser_6.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:#00008B")
        #-----------------------------------------------------------------------------------------
        self.textBrowser_2.setText(" "+degree)  # 温度
        self.textBrowser_2.setFont(QFont("Mongolian Baiti", 40, QFont.Bold))
        self.textBrowser_2.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	#00008B")

        self.textBrowser_5.setText("°")  # 温度
        self.textBrowser_5.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        self.textBrowser_5.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	#00008B")

        self.textBrowser_4.setText('💧湿度%s%%  %s %s%s级 %s '%(humidity,weather,wind_direction,wind_power,weather_short))  # 温度
        self.textBrowser_4.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        self.textBrowser_4.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	#00008B")
#--------------------------线程模块--------------------------------------------------
class Runthread(QtCore.QThread):
    updata_date = QtCore.pyqtSignal(str)

    def __init__(self,*args):
        super(Runthread,self).__init__()
        self.st = args

    def run(self):
        if self.st[0] == 1:
            self.run_junpyter()
        elif self.st[0] == 2:
            self.run_mongo()


    def run_junpyter(self):
        """
        jupyter
        :param starts:
        :return:
        """
        starts = 'jupyter notebook'
        os.system(starts)


    def run_mongo(self):
        os.system('mongod --dbpath d:\data\db')




class MyCalc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


    def yunxing(self,*args):
        #

        self.myThread = Runthread(*args)

        # 6.接收信号并产生回调函数
        self.myThread.updata_date.connect(self.Display)

        self.myThread.start()




    # 7我是回调函数
    def Display(self, data):
        pass






if __name__ == '__main__':
    app = QApplication(sys.argv)
    # MainWindow = QMainWindow()

    win = MyCalc()
    win.show()
    # ui = Ui_Dialog()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())