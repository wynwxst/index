from sys import platform
import os
import zipfile
from funcs import zip



def run(command):
    return subprocess.check_output(command,shell=True).decode("utf-8")

if platform == "win32" or platform == "win64":
    ver = input("Build Version: ")
    print("--> Creating directories...")
    os.system(f"cd dist && mkdir {ver}")
    os.system(f"cd dist/{ver} && mkdir src")
    print("--> Building binary....")
    os.system(f"python setup.py py2exe -d dist/{ver}/src/")
    print(f"--> Built binary in dist/{ver}/src/")
    print("--> Building zip...")
    zip(f"dist/{ver}/{ver}",f"dist/{ver}/src/")
elif platform == "linux" or platform == "linux2":
    print("--> Installing dependencies...")
    run("sudo pip install nuitka")
    print("--> Building...")
    run("sudo python -m nuitka --follow-imports --include-plugin-directory=core --include-plugin-directory=index --include-plugin-directory=guess --include-plugin-directory=resources upm.py")
