#!/usr/bin/python3
import os
from sys import platform
print("--> Building...")
if platform.startswith("win"):
    os.system("curl https://github.com/electron/electron/releases/download/v15.0.0-alpha.4/ -o electron-v15.0.0-alpha.4-win32-x64.zip")
print(f"npx electron-packager {os.getcwd()} upm-gui --platform={platform}")
#os.system(f"")
