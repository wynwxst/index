#!/usr/bin/python3
import argparse
import time
import sys
import getopt
import subprocess
import os
import sys
from sys import platform
from upmcore import python as corepy
from upmindex import python as indexpy
from upmcore import njs as corenjs
from upmindex import njs as indexnjs
from upmcore import ruby as corerb
from upmindex import ruby as indexrb
from upmcore import elisp as coreel
import upmguess as guess
import ctypes
from funcs import *
import requests


def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin



if platform == "win32" or platform == "win64":
    dpath = f"{os.getenv('APPDATA')}/upm"
    path = os.getenv('APPDATA')
elif platform == "linux" or platform == "linux2" or platform == "darwin":
    dpath = "/etc/upm"
    path = "/etc"

files = []
for file in os.listdir(f"{path}/"):
   files.append(file)
if "upm" not in files:
    if isAdmin() == False:
        print("Error: Administrator is required for the first run !")
    else:

       print("--> Creating data core...")
       os.system(f"cd {path} && mkdir upm")
       os.system(f"cd {path}/upm && mkdir plugins")
       os.system(f"touch {path}/upm/config.json")
       os.system(f"touch {path}/upm/sources.json")
       with open(f"{path}/upm/config.json") as config:
           config.write("{}")
       with open(f"{path}/upm/sources.json") as sources:
           sources.write("{}")
       version = requests.request("GET",url="https://raw.githubusercontent.com/k0nami/upm/main/version.txt")
       with open(f"{path}/upm/version.txt") as ver:
           ver.write(version.text)
       print("--> Created data core !")

try:
    version = requests.request("GET",url="https://raw.githubusercontent.com/k0nami/upm/main/version.txt")
    version = int(version.text)
    f = open(f"{dpath}/version.txt","r")
    content = f.load()
    content = int(content)
    if version > content:
        print("An update is availiable! Please type upm --update or get it manually from the github.")
except:
    ok = "ok"

def send_help():
    print('USAGE: upm [options]')
    print('A Universal package manager created by k0nami\n')
    print('Basic options:\n')
    print('--language : Pick a language to use\n')
    print('--install  : install package(s)\n')
    print('--remove   : remove package(s)\n')
    print('--list     : list package(s) installed\n')
    print('--info     : get information on a package\n')
    print('--search   : search a package\n')
    print("--lock     : install from the lockfile\n")
    print("--listlangs: list lanuages availiable\n")
    print("--als      : check aliases for lanuages\n")
    print("--guess    : guess the main language\n")
    print("--default  : upm guesses the main language and runs that default installation eg. npm install\n")


advanced = ["language =","help","guess","install =","install","project","remove =","remove","lock","info =","search =","listlangs","als","default","plugin =","dep","dependencies","pm ="]

def run(command):
    subprocess.check_output(command,shell=True)

def upm():

    argv = sys.argv[1:]
    opts = []
    try:
      opts, args = getopt.getopt(argv, "l:hgi:pr:rcn:s:dp:a:",advanced)

    except:
        print("ERROR: Invalid arguments provided.")
        send_help()

    for opt, arg in opts:
        if opt in ["-h","--help"]:
          send_help()
        if opt in ["-g","--guess"]:
            guess.guess()
        if opt in ['-l',"--language"]:
          if arg == "py" or arg == "python":
            if "search" == args[0]:
              indexpy.search(args)
            if "li" == args[0] or "list" == args[0]:
                corepy.list()
            if "r" == args[0] or "remove" == args[0]:
              corepy.remover(args)
            if "l" == args[0] or "lock" == args[0]:
                corepy.lock()
            if "i" == args[0] or "install" == args[0] or "add" == args[0]:
                corepy.install(args)
            if "in" == args[0] or "info" == args[0]:
                indexpy.info(args)
          if arg == "njs" or arg == "nodejs":
            if "search" == args[0]:
              indexnjs.search(args)
            if "li" == args[0] or "list" == args[0]:
                corenjs.list()
            if "r" == args[0] or "remove" == args[0]:
              corenjs.remover(args)
            if "i" == args[0] or "install" == args[0] or "add" == args[0]:
                corenjs.install(args)
            if "in" == args[0] or "info" == args[0]:
                indexnjs.info(args)
          if arg == "rb" or arg == "ruby":
            if "search" == args[0]:
              indexrb.search(args)
            if "li" == args[0] or "list" == args[0]:
                corerb.list()
            if "r" == args[0] or "remove" == args[0]:
              corerb.remover(args)
            if "i" == args[0] or "install" == args[0] or "add" == args[0]:
                corerb.install(args)
            if "in" == args[0] or "info" == args[0]:
                indexrb.info(args)
          if arg == "el" or arg == "elisp":
            if "li" == args[0] or "list" == args[0]:
                coreel.list()
            if "r" == args[0] or "remove" == args[0]:
              coreel.remover(args)
            if "i" == args[0] or "install" == args[0] or "add" == args[0]:
                coreel.install(args)
        if opt in ["-i","--install"]:
            list = ["install"]
            list.append(arg)
            for item in args:
                list.append(item)
            lang = guess.alz()
            if lang == "python":
                corepy.install(list)
            if lang == "njs":
                corenjs.install(list)
            if lang == "rb":
                corerb.install(list)
        if opt in ["-c","--lock"]:
            lang = guess.alz()
            if lang == "python":
                corepy.lock()
            if lang == "njs":
                corenjs.lock()
            if lang == "rb":
                corerb.lock()
        if opt in ["-dep","--dependencies"]:
            lang = guess.alz()
            if lang == "python":
                corepy.list()
            if lang == "njs":
                corenjs.list()
            if lang == "rb":
                corerb.list()
        if opt in ["-r","--remove"]:
            list = ["remove"]
            list.append(arg)
            for item in args:
                list.append(item)
            lang = guess.alz()
            if lang == "python":
                corepy.remover(list)
            if lang == "njs":
                corenjs.remover(list)
            if lang == "rb":
                corerb.remover(list)
        if opt in ["-n","--info"]:
            list = ["info"]
            list.append(arg)
            for item in args:
                list.append(item)
            lang = guess.alz()
            if lang == "python":
                indexpy.info(list)
            if lang == "njs":
                indexnjs.info(list)
            if lang == "rb":
                corerb.info(list)
        if opt in ["-s","--search"]:
            list = ["search"]
            list.append(arg)
            for item in args:
                list.append(item)
            lang = guess.alz()
            if lang == "python":
                indexpy.search(list)
            if lang == "njs":
                indexnjs.search(list)
            if lang == "rb":
                corerb.search(list)
        if opt in ["--listlangs"]:
            print("Python (Poetry)\nNodejs (Npm)")
        if opt in ["--als"]:
            print("Aliases[python]: [python,py]")
            print("Aliases[nodejs]: [njs,nodejs]")
            print("Aliases[ruby]  : [rb,ruby]")
        if opt in ["-d","--default"]:
            list = ["install"]
            for item in args:
                list.append(item)
            lang = guess.alz()
            if lang == "python":
                corepy.install(list)
            if lang == "njs":
                corenjs.install(list)
            if lang == "rb":
                corerb.install(list)
        if opt in ["-p","--plugin"]:
            plugins = []
            for file in os.listdir(f"{dpath}/plugins"):
                plugins.append(file)
            if args[0] not in plugins:
                return print("[Upm]: Plugin not found.")
            else:
                output = ""
                for item in args:
                    if item != args[0]:
                        output += item
                os.system(f"cd {dpath}/plugins && python {args[0]} {output}")
        if opt in ["-a","--pm"] or sys.argv[1] in ["-a","--pm"]:
            if isAdmin() == False:
                return print("Error: Administrator is required for sources")
            if "add" == arg or "+" == arg:
                if args == []:
                    return print("Error: Please include add arguments eg. upm --source add <alias> <link to source>")
                addsrc(dpath,args[0],args[1])
            if "remove" == arg or "-" == arg:
                if args == []:
                    return print("Error: Please include add arguments eg. upm --source remove <alias>")
                removesrc(dpath,args[0])
            if "update" == arg:
                update(dpath)



upm()
