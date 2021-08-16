from sys import platform
import os



def run(command):
    subprocess.check_output(command,shell=True)

if platform == "win32" or platform == "win64":
    print("--> Building binary....")
    os.system("python setup.py py2exe")
    print("--> Built binary in dist/")
elif platform == "linux" or platform == "linux2" or platform == "darwin":
    print("--> Installing dependencies...")
    run("sudo pip install nuitka")
    print("--> Building...")
    run("sudo python -m nuitka --follow-imports --include-plugin-directory=core --include-plugin-directory=index --include-plugin-directory=guess --include-plugin-directory=resources upm.py")
