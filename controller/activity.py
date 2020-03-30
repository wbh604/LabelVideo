from visual.activit_ui import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import re
import pandas as pd

class Act_window(QWidget, Ui_Form):
    stu_action = {}
    save_signal = pyqtSignal(dict)
    teacher_action = ''
    learn_action = ''
    def __init__(self):
        super(Act_window, self).__init__()
        self.setupUi(self)

    def add_student(self):
        value, ok = QInputDialog.getText(self, "动作输入", "请输入当前动作:", QLineEdit.Normal, " ")
        member, ok = QInputDialog.getText(self, "人数", "请输入当前动作的人数:", QLineEdit.Normal, " ")
        if value in self.stu_action:
            pass
        else:
            self.listWidget.addItem(member)
            self.stu_action[value] = member
            self.Stu_list.addItem(value)


    def delete_act(self):
        pos = self.Stu_list.currentRow()
        value = self.Stu_list.currentItem().text()

        # print(value)
        del self.stu_action[value]
        self.Stu_list.takeItem(pos)
        self.listWidget.takeItem(pos)
        # print(pos)
        # print('delete')

    def save_action(self):
        reply = QMessageBox.question(self, '退出', '确定保存？确认后将会对该界面初始化，请确认操作', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                    QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.save_signal.emit(self.stu_action)
            print(self.stu_action)
            print('保存')
        else:
            print('已经取消')

    def add_teacher(self):
        value, ok = QInputDialog.getText(self, "动作输入", "请输入当前动作:", QLineEdit.Normal, " ")

        self.lineEdit.setText(value)
        self.teacher_action = value
        print('add teacher')

    def add_learn(self):
        value, ok = QInputDialog.getText(self, "动作输入", "请输入当前动作:", QLineEdit.Normal, " ")


        self.lineEdit_2.setText(value)
        self.learn_action = value
        print('add learn')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = New_window()
    window.show()
    sys.exit(app.exec_())
