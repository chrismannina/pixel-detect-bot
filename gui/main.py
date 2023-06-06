import tkinter as tk
from tkinter import messagebox
from threading import Thread
import pyautogui
from bot import bot, config
import keyboard

# Create a global variable bot_thread to manage the bot thread
bot_thread = None

# Functions to handle button clicks
def set_pixel_coordinate():
    set_pixel_value('target_pixel')

def set_pixel_color():
    set_pixel_value('target_color')

def set_pixel_coordinate_and_color():
    set_pixel_value('target_pixel', 'target_color')
    
def set_pixel_value(*args):
    # Create a tkinter window
    info_window = tk.Toplevel()
    info_window.title('Pixel Info')

    # Create a label to show the pixel info
    info_label = tk.Label(info_window, text='')
    info_label.pack()
    
    # Create a label to show the instruction
    instruction_label = tk.Label(info_window, text='Hover over the desired pixel and press the Enter key to save')
    instruction_label.pack()

    # Update the label text with the current mouse position and color
    def update_info():
        x, y = pyautogui.position()
        color = pyautogui.pixel(x, y)
        info_label.config(text=f'Position: {x}, {y}\nColor: {color}')

    # Update the info label every 100ms
    def periodic_update():
        update_info()
        info_window.after(100, periodic_update)
        
    periodic_update()

    # Save the pixel info when the 'Enter' key is pressed
    def save_info():
        x, y = pyautogui.position()
        save_and_close(x, y, *args)
        info_window.destroy()

    # Define a function to save the info when 'Enter' is pressed
    def on_enter(event):
        save_info()
        keyboard.unhook(hooked_key)

    # Hook the function to the 'Enter' key
    hooked_key = keyboard.on_press_key('enter', on_enter)

    info_window.mainloop()

def save_and_close(x, y, *args):
    if 'target_pixel' in args:
        config.settings['target_pixel'] = (x, y)
    if 'target_color' in args:
        config.settings['target_color'] = pyautogui.pixel(x, y)
    config.save_settings()
    update_display_text()

def toggle_bot(button):
    global bot_thread
    if bot_thread is None:
        # Start the bot in a new thread
        bot_thread = Thread(target=bot.start)
        bot_thread.start()
        button.config(text='Stop Bot')
    else:
        # Stop the bot
        bot.stop()
        bot_thread = None
        button.config(text='Start Bot')

def change_settings():
    window = tk.Toplevel()
    window.geometry('300x400')
    window.title('Change Settings')

    tk.Label(window, text='Pixel X Coordinate:').pack()
    pixel_x_entry = tk.Entry(window)
    pixel_x_entry.insert(0, config.settings['target_pixel'][0])  
    pixel_x_entry.pack()

    tk.Label(window, text='Pixel Y Coordinate:').pack()
    pixel_y_entry = tk.Entry(window)
    pixel_y_entry.pack()
    pixel_y_entry.insert(0, config.settings['target_pixel'][1]) 

    tk.Label(window, text='Red:').pack()
    red_entry = tk.Entry(window)
    red_entry.pack()
    red_entry.insert(0, config.settings['target_color'][0])

    tk.Label(window, text='Green:').pack()
    green_entry = tk.Entry(window)
    green_entry.pack()
    green_entry.insert(0, config.settings['target_color'][1])

    tk.Label(window, text='Blue:').pack()
    blue_entry = tk.Entry(window)
    blue_entry.pack()
    blue_entry.insert(0, config.settings['target_color'][2]) 

    save_button = tk.Button(window, text='Save Settings', command=lambda: save_settings(pixel_x_entry, pixel_y_entry, red_entry, green_entry, blue_entry))
    save_button.pack()

def save_settings(pixel_x_entry, pixel_y_entry, red_entry, green_entry, blue_entry):
    try:
        # Validate coordinates
        pixel_x = int(pixel_x_entry.get().strip())
        pixel_y = int(pixel_y_entry.get().strip())
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        if not 0 <= pixel_x <= screen_width and not 0 <= pixel_y <= screen_height:
            raise ValueError('Coordinates are out of bounds!')
        
        # Validate colors
        red = int(red_entry.get().strip())
        green = int(green_entry.get().strip())
        blue = int(blue_entry.get().strip())
        if not 0 <= red <= 255 or not 0 <= green <= 255 or not 0 <= blue <= 255:
            raise ValueError('Color values should be between 0 and 255!')
        
        # Save settings
        config.settings['target_pixel'] = (int(pixel_x_entry.get()), int(pixel_y_entry.get()))
        config.settings['target_color'] = (int(red_entry.get()), int(green_entry.get()), int(blue_entry.get()))
        config.save_settings()
        update_display_text()
        window.destroy()
    except ValueError as e:
        tk.messagebox.showerror('Invalid input', str(e))

def update_display_text():
    pixel_coordinate_text.set(f'Pixel Coordinate: {config.settings["target_pixel"]}')
    pixel_color_text.set(f'Pixel Color: {config.settings["target_color"]}')

def main():
    global window
    global pixel_coordinate_text
    global pixel_color_text
    
    # Load settings
    config.load_settings()

    # Create the GUI window
    window = tk.Tk()
    window.title('Danny Bot - Pixel Detection')
    window.geometry('450x400')

    # Create StringVar objects for the display
    pixel_coordinate_text = tk.StringVar()
    pixel_color_text = tk.StringVar()
    update_display_text()

    # Create GUI components
    pixel_coordinate_label = tk.Label(window, textvariable=pixel_coordinate_text)
    pixel_color_label = tk.Label(window, textvariable=pixel_color_text)
    toggle_button = tk.Button(window, text='Start Bot', command=lambda: toggle_bot(toggle_button))
    set_pixel_coordinate_button = tk.Button(window, text='Set Pixel Coordinate', command=set_pixel_coordinate)
    set_pixel_color_button = tk.Button(window, text='Set Pixel Color', command=set_pixel_color)
    set_pixel_coordinate_and_color_button = tk.Button(window, text='Set Pixel Coordinate & Color', command=set_pixel_coordinate_and_color)
    change_settings_button = tk.Button(window, text='Change Settings', command=lambda: change_settings())

    # Configure GUI layout
    pixel_coordinate_label.pack(pady=10)
    pixel_color_label.pack(pady=10)
    toggle_button.pack(pady=5)
    set_pixel_coordinate_button.pack(pady=5)
    set_pixel_color_button.pack(pady=5)
    set_pixel_coordinate_and_color_button.pack(pady=5)
    change_settings_button.pack(pady=5)
    # Start the GUI event loop
    window.mainloop()
