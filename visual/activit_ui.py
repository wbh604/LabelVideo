# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activit_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(687, 701)
        self.add_stu_btn_2 = QtWidgets.QPushButton(Form)
        self.add_stu_btn_2.setGeometry(QtCore.QRect(130, 410, 141, 28))
        self.add_stu_btn_2.setObjectName("add_stu_btn_2")
        self.Stu_list = QtWidgets.QListWidget(Form)
        self.Stu_list.setGeometry(QtCore.QRect(90, 30, 291, 371))
        self.Stu_list.setObjectName("Stu_list")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 510, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.add_tea_btn = QtWidgets.QPushButton(Form)
        self.add_tea_btn.setGeometry(QtCore.QRect(250, 510, 141, 28))
        self.add_tea_btn.setObjectName("add_tea_btn")
        self.save_all_btn = QtWidgets.QPushButton(Form)
        self.save_all_btn.setGeometry(QtCore.QRect(270, 620, 93, 28))
        self.save_all_btn.setObjectName("save_all_btn")
        self.del_act_btn = QtWidgets.QPushButton(Form)
        self.del_act_btn.setGeometry(QtCore.QRect(290, 410, 93, 28))
        self.del_act_btn.setObjectName("del_act_btn")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(390, 30, 51, 371))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 10, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 10, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 570, 113, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.add_tea_btn_2 = QtWidgets.QPushButton(Form)
        self.add_tea_btn_2.setGeometry(QtCore.QRect(240, 570, 141, 28))
        self.add_tea_btn_2.setObjectName("add_tea_btn_2")

        self.retranslateUi(Form)
        self.add_stu_btn_2.clicked.connect(Form.add_student)
        self.del_act_btn.clicked.connect(Form.delete_act)
        self.add_tea_btn.clicked.connect(Form.add_teacher)
        self.save_all_btn.clicked.connect(Form.save_action)
        self.add_tea_btn_2.clicked.connect(Form.add_learn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_stu_btn_2.setText(_translate("Form", "添加学生行为"))
        self.add_tea_btn.setText(_translate("Form", "添加教师行为"))
        self.save_all_btn.setText(_translate("Form", "保存"))
        self.del_act_btn.setText(_translate("Form", "删除行为"))
        self.label.setText(_translate("Form", "动作列表"))
        self.label_2.setText(_translate("Form", "人数"))
        self.add_tea_btn_2.setText(_translate("Form", "添加学习方式"))
