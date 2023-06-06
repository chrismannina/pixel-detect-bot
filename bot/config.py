# This module provides a default setting dictionary. When load_settings is called, 
# it updates these defaults with the values in the settings file if it exists.

import json
import os

SETTINGS_FILE = 'settings.json'

settings = {
    'target_pixel': (None, None),
    'target_color': (0x9B, 0x50, 0x2F),
    'key_to_press': '1',
    'sleep_range': (30, 100)
}

def load_settings():
    global settings
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            content = f.read()
            if content:
                loaded_settings = json.loads(content)
                settings.update(loaded_settings)
            else:
                save_settings()
        # # Update only existing keys
        # for key in settings.keys():
        #     if key in loaded_settings:
        #         settings[key] = loaded_settings[key]

def save_settings():
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)
