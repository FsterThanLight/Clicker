# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(11, 11, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.plainTextEdit.setPalette(palette)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/下移.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 1, 7, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(40, 20))
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 1, 1, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/刷新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon2)
        self.toolButton_5.setIconSize(QtCore.QSize(40, 20))
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout.addWidget(self.toolButton_5, 1, 2, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QtCore.QSize(40, 20))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 8)
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/上移.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon4)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 1, 6, 1, 1)
        self.toolButton_6 = QtWidgets.QToolButton(self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/清除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(40, 20))
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout.addWidget(self.toolButton_6, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setMaximum(9999)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_5.addWidget(self.spinBox, 1, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_5.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 2, 0, 1, 2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_5.addWidget(self.radioButton, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 3, 0, 1, 3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 127);")
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 2, 0, 1, 3)
        self.gridLayout_4.addWidget(self.groupBox_4, 2, 1, 1, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 3)
        self.gridLayout_4.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionabout = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/关于.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionabout.setIcon(icon6)
        self.actionabout.setObjectName("actionabout")
        self.actionj = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/更新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionj.setIcon(icon7)
        self.actionj.setObjectName("actionj")
        self.actions = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/帮助.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actions.setIcon(icon8)
        self.actions.setObjectName("actions")
        self.actionb = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionb.setIcon(icon9)
        self.actionb.setObjectName("actionb")
        self.setting = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon10)
        self.setting.setObjectName("setting")
        self.actionf = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/按钮图标/窗体/res/导入指令.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionf.setIcon(icon11)
        self.actionf.setObjectName("actionf")
        self.actions_2 = QtWidgets.QAction(MainWindow)
        self.actions_2.setIcon(icon10)
        self.actions_2.setObjectName("actions_2")
        self.actiong = QtWidgets.QAction(MainWindow)
        self.actiong.setObjectName("actiong")
        self.menu.addAction(self.actionb)
        self.menu.addAction(self.actionf)
        self.menu_2.addAction(self.actionabout)
        self.menu_2.addAction(self.actionj)
        self.menu_2.addAction(self.actions)
        self.menu_4.addAction(self.actions_2)
        self.menu_3.addAction(self.actiong)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.actionb)
        self.toolBar.addAction(self.actionf)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actions_2)
        self.toolBar.addAction(self.actions)
        self.toolBar.addAction(self.actionj)
        self.toolBar.addAction(self.actionabout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动点击"))
        self.groupBox.setTitle(_translate("MainWindow", "处理状态"))
        self.groupBox_2.setTitle(_translate("MainWindow", "指令集合"))
        self.toolButton_4.setText(_translate("MainWindow", "下移"))
        self.toolButton_2.setText(_translate("MainWindow", "删除"))
        self.toolButton_5.setText(_translate("MainWindow", "修改"))
        self.toolButton.setText(_translate("MainWindow", "添加指令"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "图像名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "键鼠指令"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "参数"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "重复"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID"))
        self.toolButton_3.setText(_translate("MainWindow", "上移"))
        self.toolButton_6.setText(_translate("MainWindow", "清除指令"))
        self.groupBox_3.setTitle(_translate("MainWindow", "控制"))
        self.radioButton_2.setText(_translate("MainWindow", "重复次数："))
        self.checkBox_2.setText(_translate("MainWindow", "运行时隐藏窗口"))
        self.radioButton.setText(_translate("MainWindow", "无限循环"))
        self.groupBox_4.setTitle(_translate("MainWindow", "操作"))
        self.pushButton_5.setText(_translate("MainWindow", "开始运行"))
        self.label.setText(_translate("MainWindow", "运行时长："))
        self.label_2.setText(_translate("MainWindow", "秒"))
        self.pushButton_6.setText(_translate("MainWindow", "结束任务"))
        self.pushButton_7.setText(_translate("MainWindow", "暂停/恢复"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_4.setTitle(_translate("MainWindow", "工具"))
        self.menu_3.setTitle(_translate("MainWindow", "视图"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionj.setText(_translate("MainWindow", "检查更新"))
        self.actions.setText(_translate("MainWindow", "使用说明"))
        self.actionb.setText(_translate("MainWindow", "保存"))
        self.setting.setText(_translate("MainWindow", "设置"))
        self.actionf.setText(_translate("MainWindow", "导入指令"))
        self.actions_2.setText(_translate("MainWindow", "设置"))
        self.actiong.setText(_translate("MainWindow", "工具栏"))
import images_rc
