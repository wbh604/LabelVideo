from visual.New_pro_ui import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import re
import pandas as pd

class New_window(QWidget, Ui_Form):
    __path1 = ''
    __path2 = ''
    path_signal = pyqtSignal(QUrl,QUrl)
    def __init__(self):
        super(New_window, self).__init__()
        self.setupUi(self)

    def get_path(self):
        path = QFileDialog.getOpenFileUrl()[0]
        print(path)
        return path

    def media_path1(self):
        path = self.get_path()
        self.__path1 = path
        str_path = str(path)
        # print(str_path)
        mat = r"///(.*?)\'"
        match_name = re.findall(mat,str_path)[0]
        self.video1_path.setText(match_name)
        print('视频一路径设置')

    def media_path2(self):
        path = self.get_path()
        self.__path2 = path
        str_path = str(path)
        # print(str_path)
        mat = r"///(.*?)\'"
        match_name = re.findall(mat,str_path)[0]
        self.video2_path.setText(match_name)
        print('视频2路径设置')

    def create_csv(self):
        pro_name = self.pro_name.text() #项目名称
        class_name = self.class_name.text()#课程名称
        grade = self.grade.text()#年级
        tea_name = self.tea_name.text()#教师名称
        tea_sex = self.tea_sex.text()#教师性别
        tea_time = self.tea_time.text()#教龄
        stu_num = self.stu_name.text()#学生数量
        path1 = self.video1_path.text()#视频1路径
        path2 = self.video2_path.text()#视频2路径
        self.path_signal.emit(self.__path1,self.__path2)

        print('创建csv')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = New_window()
    window.show()
    sys.exit(app.exec_())
