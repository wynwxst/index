import time
import sys
import getopt
import subprocess
import os
import json
from sys import platform
oopen = open
def load(f,m="r"):
    if sys.platform.startswith("win") == False:
        f = f.replace("\\","/")
        return open(f,m)
    else:
        f = f.replace("/","\\")
        return open(f,m)
if platform == "win32" or platform == "win64":
    dpath = f"{os.getenv('APPDATA')}\\index"
    path = os.getenv('APPDATA')
elif platform == "linux" or platform == "linux2" or platform == "darwin":
    dpath = "/etc/index"
    path = "/etc"

config = load(f"{dpath}\\config.json","r")
global pack
pack = json.load(config)["pypackager"]
def rl(the_list, val):
   return [value for value in the_list if value != val]

amt = 0
files = []

def guess_import(f):
    c = ""
    try:
        with open(f,"r") as x:
            c = x.readlines()
        pkgs = []
        for l in c:
            p = ""
            l = l.rstrip()
            l = l.replace("\t","")
            l = l.replace("  ","")
            l = l.replace(" , ",",")
            if l.startswith("from"):
                p = l.split("import",1)
                p = p[0]
                p = p.replace("from ","")
            if l.startswith("import"):
                p = l.split("import",1)[-1]
                if "as" in p:
                    p = p.split("as",1)[0]
                if "," in p:
                    p = p.split(",")
            if type(p) == list:
                for i in p:
                    pkgs.append(i)
            else:
                pkgs.append(p)
        pkgs = rl(pkgs,'')
        pkgs = rl(pkgs,"")
        pk = []
        for i in pkgs:

            pk.append(i.replace(" ",""))
        return pk




    except FileNotFoundError:
        print("Error: File not found")
        return []




def list():
  amt = 0
  file1 = open('pyproject.toml', 'r')
  Lines = file1.readlines()
  # Strips the newline character
  for line in Lines:
      if "[tool.poetry.dev-dependencies]" in line:
        amt = 0
      if "[tool.poetry.dependencies]" in line:
        amt = 1
      if amt == 1 and "[tool.poetry.dependencies]" not in line:
        line = line.replace("=", ":")
        line = line.replace("\n","")
        print(line)

def remover(args):
  conf = True
  print("[Index]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "pyproject.toml" not in files:
    print("--> python -m {pack} init --no-interaction")
    os.system("python -m {pack} init --no-interaction")
  toprint = ""
  packages = args
  packages.remove(packages[0])
  for item in packages:
    if item != "-y":
      toprint += f"{item}, "
    if item == "-y":
      conf = False
  if conf == True:
    query = input(f"Do you want to remove\n{toprint}(y/n)? ")
    if query == "y":
      for item in packages:
        if item != "-y":
          print(f"--> python -m {pack} remove {item}")
          os.system(f"python -m {pack} remove {item}")
    else:
      print("Exiting...")
      exit()
  if conf == False:
      for item in packages:
          if item != "-y":
            print(f"--> python -m {pack} remove {item}")
            os.system(f"python -m {pack} remove {item}")

def lock():
  print("[Index]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "pyproject.toml" not in files:
    print(f"--> python -m {pack} init --no-interaction")
    os.system(f"python -m {pack} init --no-interaction")
  print(f"--> python -m {pack} lock")
  os.system(f"python -m {pack} lock")
  print(f"--> python -m {pack} install")
  os.system(f"python -m {pack} install")

def install(args):

  conf = True
  print("[Index]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "pyproject.toml" not in files:
    print(f"--> python -m {pack} init --no-interaction")
    os.system(f"python -m {pack} init --no-interaction")
  if len(args) == 1 or args == []:
    print(f"--> python -m {pack} install")
    os.system(f"python -m {pack} install")
  else:
    toprint = ""
    packages = args
    packages.remove(packages[0])
    for item in packages:
      if item != "-y":
        if item == packages[-1]:
            toprint += f"{item} "
        else:
            toprint += f"{item}, "
      if item == "-y":
        conf = False
    if conf == True:
      query = input(f"Do you want to install\n{toprint}(y/n)? ")
      if query == "y":
        for item in packages:
          if item != "-y":
            print(f"--> python -m {pack} add {item}")
            os.system(f"s:python -m {pack} add {item}")
      else:
        print("Exiting...")
        exit()
    if conf == False:
      for item in packages:
          if item != "-y":
            print(f"--> python -m {pack} add {item}")
            os.system(f"s:python -m {pack} add {item}")
