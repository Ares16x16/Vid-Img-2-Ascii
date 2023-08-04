import cv2
import numpy as np
import pyautogui
from image2ascii import ImageToAsciiConverter

class ScreenCapture:
    def __init__(self):
        self.screen_size = pyautogui.size()
        cv2.namedWindow("Screen Capture", cv2.WINDOW_NORMAL)

    def start_capture(self):
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resized_frame = cv2.resize(frame, (960, 540))
            cv2.imshow("Screen Capture", resized_frame)
            if cv2.waitKey(1) == ord("q"):
                break
            
        cv2.destroyAllWindows()
        
screen_capture = ScreenCapture()
screen_capture.start_capture()