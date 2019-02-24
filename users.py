# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import json
import re
import time
from memory_pic import jpg_4
from memory_pic import jpg_5
from memory_pic import mg_ico
from memory_pic import jpg_7
from memory_pic import jpg_8
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QDateTimeEdit, QMainWindow

import os
import sys
import base64
import random

from spiders import spider_weath


############################图片转换模块##############################################
def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()
    return image

###################################全局图片资源######################################
img = get_pic(jpg_4, '01-4.jpg')
# 在这里使用图片 icon.ico
img2 = get_pic(jpg_5, '01-5.jpg')
img_3 =get_pic(mg_ico, 'mg.ico')
img_6 =get_pic(jpg_7, '01-7.jpg')
img_7 =get_pic(jpg_8, '01-8.jpg')

#######################################################################################

class Ui_Dialog(QWidget):

# --------------------------ui模块--------------------------------------------------
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 900)
###########################################头部控件###################################
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 900))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab1")


        self.tabWidget.setCurrentIndex(1)

        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")

        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab2, "")
        self.tabWidget.addTab(self.tab3, "")

#######################################################################################
        self.msgBox = QMessageBox()#创建弹出框

        self.mongo = QtWidgets.QPushButton(self.tab)
        self.mongo.setGeometry(QtCore.QRect(10, 40, 111, 31))
        self.mongo.setObjectName("pushButton")

        self.jupy = QtWidgets.QPushButton(self.tab)
        self.jupy.setGeometry(QtCore.QRect(160, 40, 101, 31))
        self.jupy.setObjectName("pushButton_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 270, 451, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet('color:#BA55D3')
        self.lineEdit_2.setStyleSheet("background:transparent;border-width:0.5;border-style:outset;color:#BA55D3;border-color:#00008B;")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 220, 451, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background:transparent;border-width:0.5;border-style:outset;color:#FF0000;border-color:#00008B;")


        self.base_str = QtWidgets.QPushButton(self.tab)
        self.base_str.setGeometry(QtCore.QRect(510, 220, 131, 41))
        self.base_str.setObjectName("pushButton_4")

        self.str_base = QtWidgets.QPushButton(self.tab)
        self.str_base.setGeometry(QtCore.QRect(510, 270, 131, 41))
        self.str_base.setObjectName("pushButton_5")

        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(700, 0, 256, 192))
        self.textBrowser.setObjectName("textBrowser")#ip栏

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 80, 100, 200))
        self.textBrowser_2.setObjectName("textBrowser_2")#温度

        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_4.setGeometry(QtCore.QRect(110, 110, 630,111))
        self.textBrowser_4.setObjectName("textBrowser_4")#符号

        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_5.setGeometry(QtCore.QRect(75, 80, 41, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")#温度符号

        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_6.setGeometry(QtCore.QRect(70, 160, 700, 50))
        self.textBrowser_6.setObjectName("textBrowser_6")  # 风向

        self.auth = QtWidgets.QPushButton(self.tab)
        self.auth.setGeometry(QtCore.QRect(600, 120, 150, 40))
        self.auth.setObjectName("auth")#作者蓝

        self.texttime = QtWidgets.QTextBrowser(self.tab)
        self.texttime.setGeometry(QtCore.QRect(280, 40, 200, 50))
        self.texttime.setObjectName("texttime")  # 时间

        self.texttime.setStyleSheet('background:transparent;border-width:0;border-style:outset;color:#00008B')

        self.wx = QtWidgets.QLabel(self.tab)
        self.wx.setGeometry(QtCore.QRect(780, 90, 150, 150))


        jpg = QPixmap('01-5.jpg').scaled(self.wx.width(), self.wx.height())
        self.wx.setPixmap(jpg)
        self.wx.setStyleSheet('background:transparent;border-width:0;border-style:outset;')

#---------------------------文本比较模块----------------------------------------
        self.cmptext1 = QtWidgets.QTextEdit(self.tab)
        self.cmptext1.setGeometry(QtCore.QRect(20, 350, 411, 511))
        self.cmptext1.setObjectName("cmptext1")

        self.cmptext2 = QtWidgets.QTextEdit(self.tab)
        self.cmptext2.setGeometry(QtCore.QRect(540, 350, 411, 511))
        self.cmptext2.setObjectName("cmptext2")

        self.cmps = QtWidgets.QPushButton(self.tab)
        self.cmps.setGeometry(QtCore.QRect(440, 600, 93, 28))
        self.cmps.setObjectName("cmps")




        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.retranslateUi(Dialog)






############################定义事件模块#####################################
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小工具"))
        Dialog.setWindowIcon(QIcon('mg.ico'))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(
            QPixmap('01-4.jpg').scaled(self.tab.width(), self.tab.height())))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "首页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Dialog", "待开发正则模块"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Dialog", "待开发"))

        self.tab.setStyleSheet(r'#tab1{background-image: url(01-4.jpg);}')
        self.tab2.setStyleSheet(r'#tab2{background-image: url(01-7.jpg);}')
        self.tab3.setStyleSheet(r'#tab3{background-image: url(01-8.jpg);}')

        # self.tabWidget.setStyleSheet(r'#tabWidget{border-style:outset;border-radius: 3px;background-color:green;}')
        # self.tabWidget.setStyleSheet(r'#tab1{left:0px;color:red}')

#############################################样式模块###################################################
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

        self.cmps.setText(_translate("Dialog", "文本对比"))
        self.cmps.clicked.connect(self.cmp_text)


        self.cmps.setStyleSheet('QPushButton{background-Color:#00FFFF;border-radius: 10px;}')
        self.jupy.setStyleSheet('QPushButton{background-Color:#00FA9A;border-radius: 10px;}')
        self.mongo.setStyleSheet('QPushButton{background-Color:#00FA9A;border-radius: 10px;}')
        self.base_str.setStyleSheet('QPushButton{background-Color:#00FFFF;border-radius: 10px;}')
        self.str_base.setStyleSheet('QPushButton{background-Color:#00FFFF;border-radius: 10px;}')
        self.auth.setStyleSheet('QPushButton{background-Color:	#FF0000;background:transparent;border-width:0;border-style:outset;color:#00008B}')
        self.auth.setFont(QFont("Mongolian Baiti", 20, QFont.Bold))
        self.cmptext1.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:black;border-color:blue;")
        self.cmptext2.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:black;border-color:blue;")

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

#--------------------------天气预报爬虫模块--------------------------------------------------

    def run_spider(self):
        result = spider_weath()
        self.textBrowser.setText(" 来自：%s %s %s \n 邮编：%s"%( result[0], result[1], result[2], result[3]))

        self.textBrowser.setFont(QFont("Mongolian Baiti",10,QFont.Bold))
        self.textBrowser.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:#9932CC")
        self.textBrowser_6.setText("📢 " + result[10] + "  " + result[11])
        self.textBrowser_6.setFont(QFont("Mongolian Baiti", 10, QFont.Bold))
        self.textBrowser_6.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:#00008B")
        # -----------------------------------------------------------------------------------------
        self.textBrowser_2.setText(" " + result[4])  # 温度
        self.textBrowser_2.setFont(QFont("Mongolian Baiti", 40, QFont.Bold))
        self.textBrowser_2.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	#00008B")

        self.textBrowser_5.setText("°")  # 温度
        self.textBrowser_5.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        self.textBrowser_5.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	#00008B")

        self.textBrowser_4.setText(
            '💧湿度%s%%  %s %s%s级 %s ' % (result[5], result[7], result[8], result[6], result[9]))  # 温度
        self.textBrowser_4.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        self.textBrowser_4.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	#00008B")







#-----------------------------------------文本比较模块--------------------------------
########待完善############################
    def cmp_text(self):
        test1 = self.cmptext1.toPlainText().strip()
        test2 = self.cmptext2.toPlainText().strip()


        a = list(test1)
        b = list(test2)
        indexs = []
        a_len = len(a)
        b_len = len(b)

        if a_len > b_len:
            index_2 = range(b_len,a_len)
            for i, val in enumerate(b):
                try:
                    if val != a[i]:
                        print(val, i)
                        indexs.append(i)
                except:
                    pass
            indexs.extend(index_2)
            for k in indexs:
                a[k] = "<font color='red' >" + a[k] + "</font>"
                self.cmptext1.setHtml("".join(a))

        elif a_len < b_len:
            print('=====')
            index_2 = range(a_len, b_len)

            for i, val in enumerate(a):
                try:
                    if val != b[i]:
                        # print(val, i)
                        indexs.append(i)

                except:
                    pass
            indexs.extend(index_2)
            for m in indexs:
                b[m] = "<font color='red' >" + b[m] + "</font>"
                self.cmptext2.setHtml("".join(b))

        else:
            for i, val in enumerate(a):
                try:
                    if val != b[i]:
                        # print(val, i)
                        indexs.append(i)
                except:
                    pass

            for k in indexs:

                a[k] = "<font color='red' >"+a[k]+"</font>"
                self.cmptext1.setHtml("".join(a))

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
    MainWindow = QMainWindow()

    # app.setStyleSheet('MainWindow{background-color:blue}')
    win = MyCalc()
    win.show()
    # ui = Ui_Dialog()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    os.remove('01-4.jpg')
    os.remove('01-5.jpg')
    os.remove('mg.ico')
    os.remove('01-7.jpg')
    os.remove('01-8.jpg')
    sys.exit(app.exec_())

