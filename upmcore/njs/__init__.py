import time
import sys
import getopt
import subprocess
import os
import json

amt = 0
files = []



def list():
  toprint = ""
  with open("package.json",'r') as pkgjson:
      pkg = json.load(pkgjson)
  for item in pkg["dependencies"]:
      ver = pkg["dependencies"][item]
      toprint += f"{item} : {ver}\n"
  print(toprint)

def remover(args):
  print("[Index]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "package.json" not in files:
    print("--> npm init -y")
    os.system("npm init -y")
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
          print(f"--> npm remove {item}")
          os.system(f"npm remove {item}")
    else:
      print("Exiting...")
      exit()
  if conf == False:
    for item in packages:
      if item != "-y":
        print(f"--> npm remove {item}")
        os.system(f"npm remove {item}")


def install(args):
  conf = True
  print("[Index]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "package.json" not in files:
    print("--> npm init -y")
    os.system("npm init -y")
  if len(args) == 1 or args == []:
    print("--> npm install")
    os.system("npm install")
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
            print(f"--> npm add {item}")
            os.system(f"npm add {item}")
      else:
        print("Exiting...")
        exit()
    if conf  == False:
        for item in packages:
          if item != "-y":
            print(f"--> npm add {item}")
            os.system(f"npm add {item}")
