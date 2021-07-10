from pyautogui import *
import pyautogui

class Fishing:
    def __init__(self, max_fishing):
        self.max_fishing = max_fishing
        self.position = 0
        self.amount = 0

    def throw(self):
        throw_position = pyautogui.locateCenterOnScreen('image/lempar.png', confidence=.8)
        if throw_position != None:
            btnThrow = pyautogui.moveTo(throw_position)
            pyautogui.click(btnThrow)
            print("Lempar umpan!")
            self.position = 1

    def pull(self):
        pull_position = pyautogui.locateCenterOnScreen('image/angkat.png', confidence=.8)
        if pull_position != None:
            btnPull = pyautogui.moveTo(pull_position)
            pyautogui.click(btnPull)
            print("Tarik mang!")
            self.amount += 1
            print("Dapat ikan ", self.amount)
            self.position = 0

    def fishing(self):
        while True:
            if self.amount >= self.max_fishing:
                break
            elif self.position == 0:
                self.throw()
            elif self.position == 1:
                print("Tunggu...")
                self.pull()

if __name__ == "__main__":
    print("Mulai memancing")
    
    letsgo = Fishing(10)
    letsgo.fishing()
