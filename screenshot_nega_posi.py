#Screenshot to Negative Image Maker by Tsubasa Kato (C) 2019
#Referenced https://github.com/umentu/opencv/blob/master/negaposi.py
import pyautogui
import cv2
import numpy as np
import time

#Time to wait to take screenshot
time.sleep(3)
sc = pyautogui.screenshot()
sc.save('screenshot.png')

 
#Read Image
img_src = cv2.imread("screenshot.png", 1)
#Make Negative to Positive
img_negaposi = 255 - img_src
 
#Show image
cv2.imwrite('img_reverse.png', img_negaposi)
cv2.imshow("Show NEGAPOSI Image", img_negaposi)
cv2.waitKey(0)
cv2.destroyAllWindows()
