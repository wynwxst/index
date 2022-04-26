import time
import sys
import getopt
import subprocess
import os


amt = 0
files = []



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
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "pyproject.toml" not in files:
    print("--> python -m poetry init --no-interaction")
    os.system("python -m poetry init --no-interaction")
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
          print(f"--> python -m poetry remove {item}")
          os.system(f"python -m poetry remove {item}")
    else:
      print("Exiting...")
      exit()
  if conf == False:
      for item in packages:
          if item != "-y":
            print(f"--> python -m poetry remove {item}")
            os.system(f"python -m poetry remove {item}")

def lock():
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "pyproject.toml" not in files:
    print("--> python -m poetry init --no-interaction")
    os.system("python -m poetry init --no-interaction")
  print("--> python -m poetry lock")
  os.system("python -m poetry lock")
  print("--> python -m poetry install")
  os.system("python -m poetry install")

def install(args):

  conf = True
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "pyproject.toml" not in files:
    print("--> python -m poetry init --no-interaction")
    os.system("python -m poetry init --no-interaction")
  if len(args) == 1 or args == []:
    print("--> python -m poetry install")
    os.system("python -m poetry install")
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
            print(f"--> python -m poetry add {item}")
            os.system(f"python -m poetry add {item}")
      else:
        print("Exiting...")
        exit()
    if conf == False:
      for item in packages:
          if item != "-y":
            print(f"--> python -m poetry add {item}")
            os.system(f"python -m poetry add {item}")
