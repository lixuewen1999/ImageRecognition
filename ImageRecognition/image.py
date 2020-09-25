'''
@author: lixuewen
@file: image.py
@time: 2020/9/24 14:05
@desc:
'''
import cv2 as cv,os
from PIL import ImageGrab
from time import sleep
from pykeyboard import PyKeyboard
from pymouse import PyMouse
class Image:
    def __init__(self):
        self.mouse = PyMouse()
        self.keboard = PyKeyboard()

    def find_image(self,target):
        basefolder = os.path.abspath('.\\source')
        ImageGrab.grab().save(basefolder+'\\screen.png')
        source = cv.imread(basefolder+'\\screen.png')
        template = cv.imread(basefolder + '\\' + target)
        result = cv.matchTemplate(source,template,cv.TM_CCOEFF_NORMED)
        pos_start = cv.minMaxLoc(result)[3]
        print(cv.minMaxLoc(result))
        print(template.shape)
        x = int(pos_start[0]) + int(template.shape[1]/2)
        y = int(pos_start[1]) + int(template.shape[0]/2)
        simiarity = cv.minMaxLoc(result)[1]
        if simiarity < 0.95:
            return (-1,-1)
        else:
            return (x,y)

    def click(self,target):
        x,y = self.find_image(target)
        print(x,y)
        self.mouse.click(x,y)

    def double_click(self,target):
        x,y = self.find_image(target)
        self.mouse.click(x,y,1,2)

    def right_click(self,target):
        x,y = self.find_image(target)
        self.mouse.click(x,y,2,1)

    def clear(self,target):
        self.double_click(target)
        self.keboard.control_key(self.keboard.backspace_key)

    def input(self,target,content):
        self.click(target)
        self.keboard.type_string(content)

if __name__ == '__main__':
    sleep(3)
    ig = Image()
    ig.input('pwd.png','@0802101')
    ig.click('login.png')