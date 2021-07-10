from pyautogui import *
import pyautogui
from time import sleep

jumlah = 100
i = 0
while i < jumlah :
    lembar = pyautogui.locateCenterOnScreen('image/lempar.png', confidence=.8)
    angkat = pyautogui.locateCenterOnScreen('image/angkat.png', confidence=.8)
    if lembar != None:
        btnLempar = pyautogui.moveTo(lembar)
        pyautogui.click(btnLempar)
        print("Lempar umpan!")
        sleep(0.1)
    elif angkat != None:
        btnAngkat = pyautogui.moveTo(angkat)
        pyautogui.click(btnAngkat)
        i+=1
        print("Tarik mang!")
        print("Dapat ikan ", i)
        sleep(0.1)
    else:
        print("Tunggu...")
        sleep(0.1)
