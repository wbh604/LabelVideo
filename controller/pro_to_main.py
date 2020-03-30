from controller.main import main_window
from controller.New_pro import New_window
from controller.activity import Act_window as act_win
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import re
import pandas as pd
import copy
def changeNumToChar(s):
    '''
    把数字转换成相应的字符,1-->'A' 27-->'AA'
    '''
    a = [chr(i) for i in range(65, 91)]
    ss = ''
    b = []
    if s <= 26:
        b = [s]
    else:
        while s > 26:
            c = s // 26  # 商
            d = s % 26  # 余数
            b = b + [d]
            s = c
        b = b + [s]
    b.reverse()
    for i in b:
        ss = ss + a[i - 1]
    return ss

def new_to_main(path1,path2):
    play_win.media_init(path1,path2)

    play_win.show()
    New.hide()
    # play_win.MediaTime()
    play_win.media_change()

def new_act_main():

    act_windows.show()

def action_save(stu_action):
    act_list= stu_action
    tea_action = act_windows.teacher_action
    learn_action = act_windows.learn_action
    act_windows.Stu_list.clear()
    act_windows.listWidget.clear()
    act_windows.lineEdit.setText('')
    act_windows.lineEdit_2.setText('')
    act_windows.teacher_action = ''
    act_windows.learn_action = ''
    act_windows.stu_action={}
    act_windows.hide()
    #-----------------------------
    key_list = list(act_list.keys())
    value_list = list(act_list.values())
    lenth = len(key_list)
    #-----------------------------
    time_duan = play_win.act_value
    pos = time_duan.find('-')
    chazhi = int(time_duan[-pos:])-int(time_duan[0:pos])
    list1 = [(play_win.save_times+1)/2,play_win.act_value,chazhi,tea_action,learn_action,'代码']
    for i in key_list:
        list1.append(i)
    list2 = ['人数']
    for i in value_list:
        list2.append(i)
    series1 = pd.Series(list1,index=range(1,lenth+7),name=changeNumToChar(play_win.save_times+1))
    series2 = pd.Series(list2,index=range(6,lenth+7),name=changeNumToChar(play_win.save_times+2))
    test_list.append(copy.deepcopy(series1))
    test_list.append(copy.deepcopy(series2))
    play_win.data_series.append(copy.deepcopy(series1))
    play_win.data_series.append(copy.deepcopy(series2))
    play_win.save_times=play_win.save_times+2
    del series1
    del series2
    print('save finished')
if __name__ == '__main__':
    test_list = []
    app = QApplication(sys.argv)
    act_windows = act_win()
    act_windows.save_signal.connect(action_save)
    New = New_window()
    play_win = main_window()
    New.show()
    New.path_signal.connect(new_to_main)
    play_win.act_signal.connect(new_act_main)
    sys.exit(app.exec_())
