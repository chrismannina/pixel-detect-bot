# Simple logging setup that will create a bot.log file in a logs directory 
# and write log messages to it. It's currently set to only log INFO level
# messages and above, but you can adjust the logging level to suit your needs.

import logging

def setup():
    logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

def log_event(event):
    logging.info(event)
