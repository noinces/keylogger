# KeyLogger

**KeyLogger** is a harmless Python project that captures key presses and logs them to a JSON file.

## About
The program listens to keyboard input and saves each key press to `keylog.json`. It also runs in the system tray with an icon and can be exited via the tray menu.

## Features
- Logs keyboard input to `keylog.json`
- System tray icon with exit menu
- Supports standard and numpad keys

## Technologies Used
- Python 3
- [pynput](https://pypi.org/project/pynput/) for keyboard input
- [pystray](https://pypi.org/project/pystray/) for tray icon
- [Pillow](https://pypi.org/project/Pillow/) for tray icon graphics

## How to Run
1. Install dependencies:
pip install pynput pystray Pillow

2. Run the program:
python keylogger.py

3. Exit via the tray icon menu.

I did not create this project for any malicious purposes. It’s not a deeply thought-out project, just something I wrote for fun and learning. Do not run it on other people’s devices without permission.
