# Book Bot
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Book Bot is a python program that takes a text file as input and details its word and character counts. This project was mainly intended as practice as its function is not novel. Currently Book Bot runs on a Gooey produced GUI.

### Status
This is a completed project and I am unlikely to return to it.

## Installation

This repo can be cloned directly to your device. It uses Gooey library so this will need to be installed.
```
pip install Gooey
```
You can also use pyinstaller to package this program into a .EXE file. Within the analysis section of the build.spec file you will need to change the pathex arguemnt to whatever path you have cloned the repo to.
```
pip install pyinstaller
pyinstaller build.spec
```

## Usage

Run main.py and the Gooey interface will prompt you to select a text file. The program will then output details of this text, including words count and individual character counts.

## Contributing

This program is complete but feel free to raise any issues.

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
