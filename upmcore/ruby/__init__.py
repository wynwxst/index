import time
import sys
import getopt
import subprocess
import os
import json

amt = 0
files = []



def list():
  amt = 0
  file1 = open('pyproject.toml', 'r')
  Lines = file1.readlines()
  # Strips the newline character
  for line in Lines:
      if line.startswith("gem"):
        line = line.replace("~>", ":")
        line = line.replace(""" " ""","")
        line = line.replace(",","")
        print(line)

def remover(args):
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "Gemfile" not in files:
    print("--> bundle init")
    os.system("bundle init")
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
          print(f"--> bundle remove {item}")
          os.system(f"bundle remove {item}")
    else:
      print("Exiting...")
      exit()
  if conf == False:
    for item in packages:
      if item != "-y":
        print(f"--> bundle remove {item}")
        os.system(f"bundle remove {item}")

def install(args):
  conf = True
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "Gemfile" not in files:
    print("--> bundle init")
    os.system("bundle init")
  if len(args) == 1 or args == []:
    print("--> bundle install")
    os.system("bundle install")
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
            print(f"--> bundle add {item}")
            os.system(f"bundle add {item}")
      else:
        print("Exiting...")
        exit()
    if conf == True:
        for item in packages:
          if item != "-y":
            print(f"--> bundle add {item}")
            os.system(f"bundle add {item}")
