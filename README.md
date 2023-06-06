# Danny's Bot README

## Introduction
This is a bot made to automate a repetitive task. The bot watches a certain pixel on the screen, and when the pixel's color matches a target color, the bot will press a specified key.

## Installation

### Requirements
- Python 3.10+
- Pip (Python package installer)

## Steps

1. Clone the bot project from the GitHub repository or download the project as a zip file and extract it.

2. Open a Command Prompt and navigate to the 'danny-bot' directory. You can do this by using the 'cd' command, followed by the path to the 'danny-bot' directory. For example:
   
```
cd C:\Users\Daniel\danny-bot
```

3. Create a virtual environment. This will help to keep the Python packages installed for 'danny-bot' separate from other Python projects on your machine. You can do this using the following command:

```
python -m venv env

```

4. Activate the virtual environment. You can do this using the following command:

```
.\env\Scripts\activate
```

5. Install the necessary Python packages. These are listed in the requirements.txt file. You can install all required packages using the following command:

```
pip install -r requirements.txt
```

6. You are now ready to run the bot! You can do this using the following command:

```
python main.py
```

## Usage
The bot comes with a graphical user interface for ease of use. Here are some of the functionalities:

- **Set Pixel Coordinate/Color**: These buttons let you pick a pixel to save the x and y coordinates and/or the color of the pixel. Hover over the desired pixel and hit Enter to save the location and/or color.
- **Start Bot / Stop Bot**: This button starts or stops the bot. When the bot is running, it will monitor the specified pixel's color and press a specified key when the color matches the target.
Remember to save your settings before starting the bot.
