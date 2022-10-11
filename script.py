# coding=utf-8
# Program to send bulk customized messages through Telegram Desktop application
# Author @inforkgodara

import pyautogui

import pyperclip
import pandas
import time

import os


api_hash = '7d820d4557af57f57ae3c5d40524ce80'
api_id = '11770907'

# pip install pyinstaller
# pyinstaller -F -c -i python.ico script.py  生成exe 的命令

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')



time.sleep(3)

while True:

      print("open telegram ....")
      os.startfile("D:\soft\Telegram Desktop\Telegram.exe")
      print("open telegram start!")
      count = 0
      for column in excel_data['Username'].tolist():
            pyautogui.press('esc')
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            pyautogui.write(str(excel_data['Username'][count]));
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('enter')

            msg = excel_data['Message'][0]

            pyperclip.copy(msg)
            pyautogui.hotkey('ctrl', 'v')
            # pyautogui.write("nanshanxili  400mi  70fenzhong huanbao  guanshifuwu ");
            pyautogui.press('enter')
            pyautogui.press('esc')
            print("send message :" + msg + " to " + str(excel_data['Username'][count]) + " success!")
            count = count + 1


      print('The script executed successfully. send message '+str(count)+'')
      time.sleep(3600)

