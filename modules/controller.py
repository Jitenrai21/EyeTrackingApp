import pyautogui
import time

class CursorController:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.last_click_time = 0
        self.click_cooldown = 1  # seconds

    def move_cursor_to_iris(self, iris_x_norm, iris_y_norm):
        x = int(iris_x_norm * self.screen_width)
        y = int(iris_y_norm * self.screen_height)
        pyautogui.moveTo(x, y, duration=0.05)

    def click_if_wink(self, wink_type):
        now = time.time()
        if now - self.last_click_time < self.click_cooldown:
            return
        if wink_type == "left":
            pyautogui.click(button='left')
        elif wink_type == "right":
            pyautogui.click(button='right')
        self.last_click_time = now
