from PIL import ImageGrab
import cv2
import numpy as np
import time
import pyautogui
import ctypes
from directkeys import PressKey, ReleaseKey, Q, W, E, R, A, S, D, F,  TAB, SPACE, ENTER, CONTROL, k1, k2, k3, k4, k5, k6
import win32gui

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection with more detail
    processed_img = cv2.Canny(original_image, threshold1=100, threshold2=100, apertureSize=3)
    #vertices is whole screen
    return processed_img


def main():
    window_name = "League of Legends (TM) Client"
    window = win32gui.FindWindow(None, window_name)
    if window == 0:
        print("Could not find the window")
        return
    else:
        print("Found the window")

    while True:
        window_rect = win32gui.GetWindowRect(window)
        screen = np.array(ImageGrab.grab(bbox=(window_rect[0], window_rect[1], window_rect[2], window_rect[3])))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
main()