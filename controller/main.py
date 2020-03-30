from visual.main_ui import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import re
import pandas as pd
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class main_window(QWidget, Ui_Form):
    __sta = 1
    __label_time = 0
    save_times = 1
    data = {'pos1':[],
            'pos2':[]}
    data_series = [pd.Series(['时间段序号','时间段','时间长度','教师行为','学习方式','学生行为'],index=[1,2,3,4,5,6],name='A')]
    act_signal = pyqtSignal()
    act_value=''
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        self.final_slider.hide()
        self.final_start_bnt.hide()
        self.final_stop_bnt.hide()
        self.final_time.hide()
        self.bq_btn.hide()

    def media_init(self,path1,path2):
        self.mplayer1 = QMediaPlayer(self)
        self.mplay1List = QMediaPlaylist()
        self.mplay1List.addMedia(QMediaContent(path1))
        self.mplay1List.setCurrentIndex(0)
        self.mplayer1.setPlaylist(self.mplay1List)
        self.mplayer1.setVideoOutput(self.media1)

        self.mplayer2 = QMediaPlayer(self)
        self.mplay2List = QMediaPlaylist()
        self.mplay2List.addMedia(QMediaContent(path2))
        self.mplay2List.setCurrentIndex(0)
        self.mplayer2.setPlaylist(self.mplay2List)
        self.mplayer2.setVideoOutput(self.media2)
        self.mplayer2.play()
        self.mplayer1.play()

    def show_final(self):
        self.final_slider.show()
        self.final_start_bnt.show()
        self.final_stop_bnt.show()
        self.final_time.show()
        self.bq_btn.show()
        self.v1_slider.hide()
        # self.time1.hide()
        # self.time2.hide()
        self.tongbu.hide()
        self.v1_start_bnt.hide()
        self.v1_stop_bnt.hide()
        self.v2_slider.hide()
        self.v2_start_bnt.hide()
        self.v2_stop_bnt.hide()
    def v1_stop(self):
        self.mplayer1.pause()
        # print("暂停1视频")

    def v2_stop(self):
        self.mplayer2.pause()
        # print('暂停2视频')

    def all_stop(self):
        self.mplayer1.pause()
        self.mplayer2.pause()
        # print('暂停所有')

    def tongbu_media(self):
        self.all_stop()
        self.start1_time = self.v1_slider.value() * 1000
        print(self.start1_time)
        self.start2_time = self.v2_slider.value() * 1000
        print(self.start2_time)
        reply = QMessageBox.question(self, '退出', '确定同步？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.total_time = self.v1_time * 1000 - self.start1_time
            print(self.total_time)
            self.chazhi = self.start2_time - self.start1_time
            print(self.total_time)
            self.mplayer1.setPosition(self.start1_time)
            self.mplayer2.setPosition(self.start2_time)
            self.final_slider.setRange(self.start1_time / 1000, int(self.total_time / 1000) + self.start1_time / 1000)
            self.show_final()
            # print("同步")

    def go_active(self):
        self.act_value = self.time_list.currentItem().text()

        self.act_signal.emit()
        print("开始设置具体内容")

    def v1_start(self):
        if self.__sta == 1:
            self.MediaTime()
            self.__sta = 0
        self.mplayer1.play()

        print('v1播放')

    def v2_start(self):
        self.mplayer2.play()

        print('v2播放')

    def all_start(self):
        self.mplayer1.play()
        self.mplayer2.play()

        print('全员开始')

    def label(self):
        start_time = self.__label_time
        end_time = self.final_slider.value()
        string = str(start_time)+"-"+str(end_time)
        data = pd.Series({'pos1':start_time,'pos2':end_time})
        # self.__label_time_df = self.__label_time_df.append(data,ignore_index=True)
        self.time_list.addItem(string)
        self.__label_time = end_time
        print("打标签")

    def save_all(self):
        print(self.data_series)
        canshu = {}
        lenth = len(self.data_series)
        for i in self.data_series:
            canshu[i.name] = i

        final = pd.DataFrame(canshu)
        final.to_excel('Label.xlsx')
        print(final)
        print("保存信息")

    def v1_set_time(self):
        if (qAbs(self.v1_slider.value() * 1000 - self.mplayer1.position()) > 1000 and (self.v1_slider.value() != 0)):
            self.mplayer1.pause()
            self.mplayer1.setPosition(self.v1_slider.value() * 1000)
        # print('设置V1时间')

    def v2_set_time(self):
        if (qAbs(self.v2_slider.value() * 1000 - self.mplayer2.position()) > 1000 and (self.v2_slider.value() != 0)):
            self.mplayer2.pause()
            self.mplayer2.setPosition(self.v2_slider.value() * 1000)
        # print('设置V2时间')

    def all_set_time(self):
        if (qAbs(self.final_slider.value() * 1000 - self.mplayer1.position()) > 1000 and (self.final_slider.value() != 0)):
            self.mplayer1.pause()
            self.mplayer2.pause()
            self.mplayer1.setPosition(self.final_slider.value() * 1000)
            self.mplayer2.setPosition(self.final_slider.value() * 1000+self.chazhi)


    def media_change(self):
        self.mplayer1.positionChanged.connect(self.PlaySlider1)
        self.mplayer2.positionChanged.connect(self.PlaySlider2)
        self.mplayer1.positionChanged.connect(self.PlaySliderAll)

    def MediaTime(self):
        self.v1_time = 0
        self.v1_slider.setValue(0)
        self.v2_slider.setValue(0)
        print(self.mplayer1.duration())

        self.v1_time = self.mplayer1.duration() / 1000
        self.v2_time = self.mplayer2.duration() / 1000
        print(self.v1_time)
        self.v1_slider.setRange(0, int(self.v1_time))  # 设置进度条1为时间/1000
        self.v2_slider.setRange(0, int(self.v2_time))  # 设置进度条2为时间/1000
        self.time1.setText(str(int(self.v1_time)))
        self.time2.setText(str(int(self.v2_time)))

    def PlaySlider1(self,val):
        self.v1_slider.setValue(int(val / 1000))
        self.time1.setText(str(int(val/1000)))
    def PlaySlider2(self,val):
        self.v2_slider.setValue(int(val / 1000))
        self.time2.setText(str(int(val / 1000)))
    def PlaySliderAll(self,val):
        self.final_slider.setValue(int(val / 1000))
        self.final_time.setText(str(int(val / 1000)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())
