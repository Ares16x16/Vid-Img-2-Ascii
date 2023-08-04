import numpy as np
import pyautogui
import cv2
import time
import os

ASCII_CHARS = "@WM%#&$~^[]`\')(|\\/:+=-,.            "
ascii_chars = list(ASCII_CHARS)

class ScreenCapture:
    def __init__(self):
        self.screen_size = pyautogui.size()
        rows, columns = os.get_terminal_size()
        self.terminal_width = int(rows)
        self.terminal_height = int(columns)
    def start_capture(self):
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized_frame = cv2.resize(frame, (self.terminal_width, self.terminal_height - 1))
            
            os.system("cls")
            
            ascii_art = ""
            for row in resized_frame:
                for pixel in row:
                    ascii_art += ascii_chars[int(pixel / (256 / len(ASCII_CHARS)))]
                ascii_art += "\n"
                
            print(ascii_art)

if __name__ == "__main__":
    screen_capture = ScreenCapture()
    screen_capture.start_capture()