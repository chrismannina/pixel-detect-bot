# This is the entry point to the application. It sets up logging and then starts 
# the main GUI.

from gui import main as gui_main
from bot import logging as bot_logging

if __name__ == '__main__':
    bot_logging.setup()  # setup logging
    gui_main.main()  # start the main GUI
