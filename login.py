#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pyautogui
import os,time
import datetime
from chinese_calendar import is_workday
#os.environ['DISPLAY'] = ':0'
def open_trade():
    anchor_loc = pyautogui.locateCenterOnScreen('/root/Q7.png')
    if anchor_loc== None:
        anchor_loc = pyautogui.locateCenterOnScreen('/root/Q7bak.png')
    print(anchor_loc)
    pyautogui.click(anchor_loc)
    pyautogui.press( 'enter' )
    time.sleep(1)
    pyautogui.press( 'enter' )

    time.sleep(15)
    pyautogui.write("********")
    pyautogui.press( 'enter' )
    time.sleep(15)
    login = pyautogui.locateCenterOnScreen('/root/login.png')
    if login is not None:
        print(login)
        print("登录成功了...")
        pyautogui.click(login)
    else:
        print("登录失败,结束进程...")
        os.system('killall q7_release.exe')


date = datetime.datetime.now().date()
h = int(time.strftime("%H"))  
if is_workday(date):
    print("是工作日")
    if h >=9 and h <=11  or h>=13 and h<=15  or h >= 21 and h <= 23 :
        print("当前为交易时间")
        process = os.popen("ps -x |grep q7")
        txt = process.read()
        if 'q7_release.exe' in txt :
            print("进程已经存在了")
        else:
            open_trade()   #如果进程不存在并且在交易时间内就再次打开。
        
        

else:
    print("是休息日")
            
        
