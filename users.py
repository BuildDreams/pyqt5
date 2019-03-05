# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from pdf_word import parser_pdfs
from memory_pic import mg_ico
from memory_pic import start_jpg
from memory_pic import jpg_5
from pdf_str import readPDF



from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QIcon,  QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QDateTimeEdit, QMainWindow, QLCDNumber, QDesktopWidget, \
    QFileDialog, QAction, QMenu, QSystemTrayIcon


import os
import sys
import base64


from spiders import spider_weath


##################################################
# 加载全局图片资源 函数                       #
#                                                #
##################################################
def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()
    return image

    ##################################################
    # 加载全局图片资源                        #
    #                                                #
    ##################################################



# 在这里使用图片 icon.ico

img_3 = get_pic(mg_ico, 'mg.ico')
img_st = get_pic(jpg_5, '01-5.jpg')
img_st = get_pic(start_jpg, 'start.jpg')






##################################################
# 唯一ui类                                        #
#                                                #
##################################################

class Ui_Dialog(QWidget):
    windowList = []
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # Dialog.resize(1000, 950)

        Dialog.setGeometry(400, 50, 1000, 950)

        # Dialog.setDisabled(False)

        Dialog.setWindowOpacity(0.85)  # 设置窗口透明度
        # Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # Dialog.setDisabled(True)
        # Dialog.WindowMinimizeButtonHint()
        Dialog.setStyleSheet("#Dialog{background:red;border-top:1px solid white;border-bottom:1px solid white;border-left:1px solid white;border-top-left-radius:10px;border-bottom-left-radius:10px;}")
        # Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.cwd = os.getcwd()
        self.center()
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 950))
        self.tabWidget.setObjectName("tabWidget")
        # QTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        ##################################################
        # c创建一个tabwidget(上方工具栏)                         #
        #                                                #
        ##################################################
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab1")

        self.tabWidget.setCurrentIndex(1)
        # self.tabWidget.showNormal()

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        # self.tab3.setLayout(self.tabWidget)

        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")

        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")

        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab3, "")
        self.tabWidget.addTab(self.tab4, "")
        self.tabWidget.addTab(self.tab5, "")

        self.tabWidget.setDocumentMode(True)
        self.setAcceptDrops(True)

        ##################################################
        # 创建一个弹出框全局变量                             #
        #                                                #
        ##################################################
        self.msgBox = QMessageBox()  # 创建弹出框

        self.mongo = QtWidgets.QPushButton(self.tab)
        self.mongo.setGeometry(QtCore.QRect(10, 40, 130, 40))
        self.mongo.setObjectName("pushButton_mongo")

        self.jupy = QtWidgets.QPushButton(self.tab)
        self.jupy.setGeometry(QtCore.QRect(160, 40, 130, 42))
        self.jupy.setObjectName("pushButton_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 270, 451, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet('color:#BA55D3')

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 220, 451, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.base_str = QtWidgets.QPushButton(self.tab)
        self.base_str.setGeometry(QtCore.QRect(510, 220, 131, 41))
        self.base_str.setObjectName("pushButton_4")

        self.str_base = QtWidgets.QPushButton(self.tab)
        self.str_base.setGeometry(QtCore.QRect(510, 270, 131, 41))
        self.str_base.setObjectName("pushButton_5")

        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(700, 0, 256, 192))
        self.textBrowser.setObjectName("textBrowser")  # ip栏

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(15, 80, 130, 200))
        self.textBrowser_2.setObjectName("textBrowser_2")  # 温度

        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_4.setGeometry(QtCore.QRect(110, 110, 630, 111))
        self.textBrowser_4.setObjectName("textBrowser_4")  # 符号

        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_6.setGeometry(QtCore.QRect(70, 160, 700, 50))
        self.textBrowser_6.setObjectName("textBrowser_6")  # 风向
        ##################################################
        # 作者按钮init                                     #
        #                                                #
        ##################################################
        self.auth = QtWidgets.QPushButton(self.tab)
        self.auth.setGeometry(QtCore.QRect(600, 120, 150, 40))
        self.auth.setObjectName("auth")  # 作者蓝
        ##################################################
        # 计时器lableui                                   #
        #                                                #
        ##################################################
        self.texttime = QtWidgets.QLCDNumber(self.tab)
        self.texttime.setGeometry(QtCore.QRect(240, 40, 500, 30))
        self.texttime.setMouseTracking(False)
        self.texttime.setDigitCount(19)
        self.texttime.setMode(QLCDNumber.Dec)
        self.texttime.setSegmentStyle(QLCDNumber.Flat)
        self.texttime.setObjectName("texttime")
        self.wx = QtWidgets.QLabel(self.tab)
        self.wx.setGeometry(QtCore.QRect(780, 90, 150, 150))

        ##################################################
        # 作者按钮ui                                       #
        #                                                #
        ##################################################
        jpg = QPixmap('01-5.jpg').scaled(self.wx.width(), self.wx.height())
        self.wx.setPixmap(jpg)
        self.wx.setStyleSheet('background:transparent;border-width:0;border-style:outset;')
        ##################################################
        # 文本对比按钮ui                                   #
        #                                                #
        ##################################################
        self.cmptext1 = QtWidgets.QTextEdit(self.tab)
        self.cmptext1.setGeometry(QtCore.QRect(20, 350, 411, 511))
        self.cmptext1.setObjectName("cmptext1")

        self.cmptext2 = QtWidgets.QTextEdit(self.tab)
        self.cmptext2.setGeometry(QtCore.QRect(540, 350, 411, 511))
        self.cmptext2.setObjectName("cmptext2")

        self.cmps = QtWidgets.QPushButton(self.tab)
        self.cmps.setGeometry(QtCore.QRect(440, 600, 93, 28))
        self.cmps.setObjectName("cmps")

        ##################################################
        # tab3ui                                         #
        #                                                #
        ##################################################
        self.btn_chooseMutiFile = QtWidgets.QPushButton(self.tab3)
        self.btn_chooseMutiFile.setObjectName("btn_chooseMutiFile")
        self.btn_chooseMutiFile.setText("pdf-->txt")
        self.btn_chooseMutiFile.setGeometry(QtCore.QRect(400, 40, 200, 40))
        self.textbrower3 = QtWidgets.QTextBrowser(self.tab3)
        self.textbrower3.setGeometry(QtCore.QRect(15, 80, 960, 800))
        self.textbrower3.setObjectName("textbrower3")

        ##################################################
        # tab4ui配置                                      #
        #                                                #
        ##################################################

        self.btn_chooseMutiFile_tab4 = QtWidgets.QPushButton(self.tab4)
        self.btn_chooseMutiFile_tab4.setObjectName("btn_chooseMutiFile_tab4")
        self.btn_chooseMutiFile_tab4.setText("pdf-->word")
        self.btn_chooseMutiFile_tab4.setGeometry(QtCore.QRect(50, 70, 200, 40))

        self.tab4_brower4 = QtWidgets.QTextBrowser(self.tab4)
        self.tab4_brower4.setGeometry(QtCore.QRect(300, 30, 500, 120))
        self.tab4_brower4.setObjectName("tab4_brower4")

        self.img_py = QtWidgets.QPushButton(self.tab4)
        self.img_py.setObjectName("img_py")
        self.img_py.setText("img-->py")
        self.img_py.setGeometry(QtCore.QRect(50, 360, 200, 40))

        self.tab4_brower_img = QtWidgets.QTextBrowser(self.tab4)
        self.tab4_brower_img.setGeometry(QtCore.QRect(300, 320, 500, 120))
        self.tab4_brower_img.setObjectName("tab4_brower_img")

        self.winIconPix = QPixmap(16, 16)
        self.setWindowIcon(QIcon('mg.ico'))
        self.tray = QSystemTrayIcon(Dialog)
        self.trayIconPix = QPixmap(16, 16)
        self.tray.setIcon(QIcon('mg.ico'))
#################################################################################################
        self.js = QtWidgets.QPushButton(self.tab5)
        self.js.setGeometry(QtCore.QRect(80, 40, 130, 42))
        self.js.setObjectName("js")

        self.ht = QtWidgets.QPushButton(self.tab5)
        self.ht.setGeometry(QtCore.QRect(260, 40, 130, 42))
        self.ht.setObjectName("ht")

        self.scp = QtWidgets.QTextBrowser(self.tab5)
        self.scp.setGeometry(QtCore.QRect(16, 160, 700, 500))
        self.scp.setObjectName("scp")
        

        ##################################################
        # 挂载到主界面                                     #
        #                                                #
        ##################################################


        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.retranslateUi(Dialog)

    ##################################################
    # 自定义样式、点击事件模块                           #
    #                                                #
    ##################################################
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小工具"))
        # Dialog.setStyleSheet("#Dialog{background-color:red;}")
        Dialog.setWindowIcon(QIcon('mg.ico'))
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(
        #     QPixmap('01-4.jpg').scaled(self.tab.width(), self.tab.height())))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "首页"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("Dialog", "浏览器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Dialog", "pdf转换为text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("Dialog", "pdf转换为word"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("Dialog", "tools"))

        "QTabBar::tab{min-height: 30px; min-width: 80px;border-top-right-radius:20px;border-radius:20px;}"
        self.tabWidget.setStyleSheet(
            "QTabBar{background-color:#333300;outline:solid 2px;}QTabBar::tab{border-bottom-color:#C2C7CB;min-width: "
            "150px;border-right:2px solid black;border-style: outset;min-height: 40px;"
            "color:white;background-color:#4169E1;}QTabBar::tab:selected{background-color: white;"
            "color:green;border-top-right-radius:10px;border-top-left-radius:10px;border:none}QTabBar::tab:first{margin-left:10px;}"
            "QTabBar::tab:hover:!selected{color:red;background-color:black;}")

        # self.tabWidget.setStyleSheet("QTabBar::tab:first:selected{background-color: white;}")  # 有问题
        self.tab.setStyleSheet("#tab1{background-color:#012456;}")
        self.tab3.setStyleSheet('#tab3{background-color:#012456;}')
        self.tab4.setStyleSheet('#tab4{background-color:#012456;}')
        self.tab5.setStyleSheet('#tab5{background-color:#012456;}')
        ##################################################
        # tab1按钮模块 样式 事件                            #
        #                                                #
        ##################################################
        self.mongo.setText(_translate("Dialog", "mongo"))
        icon = QIcon()

        icon.addPixmap(QPixmap("start.jpg"), QIcon.Normal, QIcon.Off)

        self.mongo.setIcon(icon)

        self.mongo.setIconSize(QtCore.QSize(60, 30))
        self.mongo.setAutoRepeatDelay(200)
        self.mongo.clicked.connect(lambda: Dialog.yunxing(2, ))

        self.auth.setText(_translate("Dialog", "*作者*"))
        self.auth.clicked.connect(self.auth_qq)

        self.jupy.setIcon(icon)
        self.jupy.setIconSize(QtCore.QSize(60, 30))
        self.jupy.setAutoRepeatDelay(200)
        self.jupy.setText(_translate("Dialog", "jupyter"))
        self.jupy.clicked.connect(lambda: Dialog.yunxing(1, ))

        self.base_str.setText(_translate("Dialog", "解码base64"))
        self.base_str.clicked.connect(self.b64_str)

        self.str_base.setText(_translate("Dialog", "转码base64"))
        self.str_base.clicked.connect(self.str_b64)

        self.cmps.setText(_translate("Dialog", "文本对比"))
        self.cmps.clicked.connect(self.cmp_text)

        ##################################################
        # 样式模块                                       #
        #                                                #
        ##################################################
        self.lineEdit_3.setStyleSheet(
            "background:transparent;border-width:0.5;border-style:outset;color:#FF0000;border-color:white;")
        self.lineEdit_2.setStyleSheet(
            "background:transparent;border-width:0.5;border-style:outset;color:#BA55D3;border-color:white;")
        self.cmps.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')
        self.jupy.setStyleSheet(
            'QPushButton{background-Color:white;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color: red;}')
        self.mongo.setStyleSheet(
            '#pushButton_mongo{background-Color:white;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red}')
        self.base_str.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')
        # self.base_str.setStyleSheet("")

        self.str_base.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')
        self.auth.setStyleSheet(
            'QPushButton{background-Color:	#FF0000;background:transparent;border-width:0;border-style:outset;color:#87CEFA}QPushButton:hover{color: red;}')
        self.auth.setFont(QFont("Mongolian Baiti", 20, QFont.Bold))
        self.cmptext1.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:white;border-color:#FFF5EE;")
        self.cmptext2.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:white;border-color:#FFF5EE;")

        ##################################################
        # tab3模块                                       #
        #                                                #
        ##################################################
        self.btn_chooseMutiFile.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color: red}')
        self.btn_chooseMutiFile.clicked.connect(self.slot_btn_chooseMutiFile)
        self.textbrower3.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:#FF8C00;border-color:white;font-size:30px;")

        ##################################################
        # tab4模块                                       #
        #                                                #
        ##################################################

        self.btn_chooseMutiFile_tab4.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color: red}')
        self.btn_chooseMutiFile_tab4.clicked.connect(self.run_pdf_parse)

        self.tab4_brower4.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:#FF8C00;border-color:white;font-size:15px;")

        self.img_py.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color: red}')
        self.img_py.clicked.connect(self.imgTopy)

        self.tab4_brower_img.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:#FF8C00;border-color:white;font-size:15px;")
#####################################################################################################################
        self.js.setText(_translate("Dialog", "计算器"))
        self.js.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color: red}')
        self.js.clicked.connect(lambda: Dialog.yunxing(3, ))

        self.ht.setText(_translate("Dialog", "画图"))
        self.ht.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color: red};background-attachment:scroll;')
        self.ht.clicked.connect(lambda: Dialog.yunxing(4, ))
        ##################################################
        # 计时器模块                                       #
        #                                                #
        ##################################################
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.showtime)

        self.timer.start()

        # self.timer1 = QTimer()
        # self.timer1.setInterval(1000)
        # # self.timer1.timeout.connect(self.showtime)
        # self.timer1.timeout.connect(self.scp_r)
        # self.timer1.start()


        ################################################################################
        # 初始调用爬虫模块
        #
        ##################################################################################
        self.run_spider()

    def auth_qq(self):
        QMessageBox.question(self, 'waring', '仅供学习使用',
                             QMessageBox.Yes, QMessageBox.Yes)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    ################################################################################
    # 两个转码函数
    #
    ##################################################################################

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
                                 QMessageBox.Yes, QMessageBox.Yes)

    def str_b64(self):
        """
        解码
        :param input_b64:
        :return:
        """
        input_b64 = self.lineEdit_2.text()

        b64_str = base64.b64encode(input_b64.encode('utf-8'))

        self.lineEdit_3.setText((b64_str).decode('utf-8'))


    ################################################################################
    # 计时器函数
    #
    ##################################################################################
    def showtime(self):
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        test = self.dateEdit.text()
        # self.texttime.setText(test)
        self.texttime.display(test)
        self.texttime.setStyleSheet('font: italic 6pt \"Arial\";border-width:0;border-style:outset;color:#DC143C;')
        # self.texttime.setFont(QFont("Mongolian Baiti", 11, QFont.Bold))



    # def scp_r(self):
    #
    #     aqs = "于我而言，你是淌过摩尔曼斯克的暖流，亦是填满亚马逊坳陷的长河。"
    #     all_len  = len(aqs)
    #
    #     self.scp.setText(aqs[0:self.inx])
    #     self.inx +=1
    #     if self.inx == all_len-1:
    #         self.inx = 0
    #         self.scp.setText(aqs+" "*self.inx)
    #         self.inx += 1

        # print(self.inx)
        # print(aqs[0:self.inx])
        # self.inx +=1
        # if self.inx+1 == all_len:
        #     self.inx=0


    ################################################################################
    # 天气预报爬虫样式运行模块
    #
    ##################################################################################
    def run_spider(self):
        result = spider_weath()
        QMessageBox.question(self, 'HI', '来自 %s %s %s的你,你好吖！'%(result[0], result[1], result[2]),
                             QMessageBox.Yes, QMessageBox.Yes)
        self.textBrowser.setHtml(
            " &nbsp;<font color='red' >📍 &nbsp;</font>：%s %s %s \n <font color='blue' >🔜 &nbsp;</font>：%s" % (
            result[0], result[1], result[2], result[3]))

        self.textBrowser.setFont(QFont("Mongolian Baiti", 10, QFont.Bold))
        self.textBrowser.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:white")
        self.textBrowser_6.setHtml("<font color='#FF8C00' >📢 💦</font>" + result[10] + "  " + result[11])
        self.textBrowser_6.setFont(QFont("Mongolian Baiti", 10, QFont.Bold))
        self.textBrowser_6.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:white")
        # -----------------------------------------------------------------------------------------
        self.textBrowser_2.setText("%s°" % result[4])  # 温度
        self.textBrowser_2.setFont(QFont("Mongolian Baiti", 40, QFont.Bold))
        self.textBrowser_2.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	white")

        # self.textBrowser_5.setText("")  # 温度
        # self.textBrowser_5.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        # self.textBrowser_5.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	white")

        self.textBrowser_4.setHtml(
            "<font color='#00008B' >💧</font> 湿度%s%%  %s %s%s级 %s " % (
            result[5], result[7], result[8], result[6], result[9]))  # 温度
        self.textBrowser_4.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        self.textBrowser_4.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	white")

    ################################################################################
    # 图片转换模块
    #
    ##################################################################################
    def imgTopy(self, evn):
        self.tab4_brower_img.clear()
        QMessageBox.question(self, 'waring', '将在当前目录生成pics.py文件',
                             QMessageBox.Yes, QMessageBox.Yes)

        py_name = 'pics'
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "选择文件",
                                                       self.cwd,  # 起始路径
                                                       "JPG Files (*.jpg);;PNG Files (*.png);;GIF Files (*.gif);;ICO Files (*.ico);;")
        if len(files) == 0:
            return
        # print(len(files))
        for inx,file in enumerate(files):
            (file_path, tempfilename) = os.path.split(file)
            (filename, extension) = os.path.splitext(tempfilename)
            open_pic = open("%s" % file, 'rb')
            b64str = base64.b64encode(open_pic.read())
            open_pic.close()
            # 注意这边b64str一定要加上.decode()
            sy = len(files) - inx-1
            with open('%s.py' % py_name, 'a+') as f:
                f.write('%s = "%s"\n' % (filename, b64str.decode()))

            self.tab4_brower_img.append("<font color='red' >"+"正在处理:"+tempfilename+ "</font>"+"<br />"+"当前剩余:%s张"%sy)

    ##################################################################################
    # 选择文件模块
    ##################################################################################
    def slot_btn_chooseMutiFile(self):
        self.textbrower3.clear()
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "选择文件",
                                                       self.cwd,  # 起始路径
                                                       "PDF Files (*.pdf);;")

        if len(files) == 0:
            # print("\n取消选择")
            return

        # print("\n你选择的文件为:")
        for file in files:
            texts = readPDF(file)
            self.textbrower3.append(texts + "-" * 122)


    ##################################################################################
    # 运行转换为word模块
    ##################################################################################

    def run_pdf_parse(self):
        self.tab4_brower4.clear()
        files, filetype = QFileDialog.getOpenFileNames(self,"选择文件",self.cwd,"PDF Files (*.pdf);;")

        if len(files) == 0:
            # print("\n取消选择")
            return

        # print("\n你选择的文件为:")
        space = "&nbsp;&nbsp;&nbsp;&nbsp;"
        for file in files:
            texts = parser_pdfs(file)

            (filepath, tempfilename) = os.path.split(file)
            for text in texts:
                self.tab4_brower4.append(
                    "<font color='red' >" + "处理对象:" + tempfilename + "</font>" + "<br />" + "%s页面数:" % space + str(
                        text[0]) + "<br />" + "%s图片数:" % space + str(text[1]) + "<br />" + "%s曲线数:" % space +
                    str(text[2]) + "<br />" + "%s水平文本框:" % space + str(
                        text[3]) + "<br />" + "<font color='red' >" + "-" * 40 + "</font>")

    ################################################################################
    # 待完善
    #
    ##################################################################################
    def cmp_text(self):
        test1 = self.cmptext1.toPlainText().strip()
        test2 = self.cmptext2.toPlainText().strip()

        a = list(test1)
        b = list(test2)
        indexs = []
        a_len = len(a)
        b_len = len(b)

        if a_len > b_len:
            index_2 = range(b_len, a_len)
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
                a[k] = "<font color='red' >" + a[k] + "</font>"
                self.cmptext1.setHtml("".join(a))




################################################################################
# 自定义多线程模块
#
##################################################################################
class Runthread(QtCore.QThread):
    updata_date = QtCore.pyqtSignal(str)

    def __init__(self, *args):
        super(Runthread, self).__init__()
        self.st = args

    def run(self):
        if self.st[0] == 1:
            self.run_junpyter()
        elif self.st[0] == 2:
            self.run_mongo()

        elif self.st[0] == 3:
            self.run_js()
        elif self.st[0] == 4:
            self.run_ht()

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


    def run_js(self):
        """
        jupyter
        :param starts:
        :return:
        """
        starts = 'calc'
        os.system(starts)

    def run_ht(self):
        os.system('mspaint')


################################################################################
# 自定义启动线程
#
##################################################################################
class MyCalc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #############################################################################
        #设置系统托盘
        # minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        # maximizeAction = QAction("Ma&ximize", self, triggered=self.showMaximized)
        restoreAction = QAction("&还原", self, triggered=self.showNormal)
        quitAction = QAction("&退出", self, triggered=QApplication.instance().quit)  # 退出APP
        self.trayMenu = QMenu(self)
        # self.trayMenu.addAction(minimizeAction)
        # self.trayMenu.addAction(maximizeAction)
        self.trayMenu.addAction(restoreAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.ui.tray.setContextMenu(self.trayMenu)
        ########################################################
############################################
#忽略退出按钮
###########################################
    def closeEvent(self, event):
        event.ignore()  # 忽略关闭事件
        self.hide()  # 隐藏窗体

    def yunxing(self, *args):
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
    # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    # MainWindow.setWindowFlags(Qt::FramelessWindowHint)
    win = MyCalc()
    win.show()

    # ui = Ui_Dialog()
    # ui.setupUi(MainWindow)
    # MainWindow.show()

    os.remove('mg.ico')
    os.remove('start.jpg')
    os.remove('01-5.jpg')
    sys.exit(app.exec_())
