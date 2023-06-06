import time
import random
import pyautogui
from bot import config

running = False

# Function to check if a pixel color matches the target color
def is_target_color(pixel):
    return pixel == config.settings['target_color']

# Function to press the key
def press_key():
    pyautogui.press(config.settings['key_to_press'])

# Function to get the pixel color at the target coordinate
def get_pixel_color():
    x, y = config.settings['target_pixel']
    if x is not None and y is not None:
        return pyautogui.pixel(x, y)
    return None

# Main function
def start():
    global running
    running = True
    while running:
        pixel_color = get_pixel_color()
        if is_target_color(pixel_color):
            press_key()
        time.sleep(random.uniform(*config.settings['sleep_range']) / 1000)

def stop():
    global running
    running = False
