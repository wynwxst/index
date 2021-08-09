import time
import sys
import getopt
import subprocess
import os


amt = 0
files = []



def list():
  os.system("cask list")

def remover(args):
  conf = True
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "Cask" not in files:
    print("--> cask init")
    os.system("cask init")
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
      print("--> Removing packages...")
      for item in packages:
        if item != "-y":
          print(f"--> upm -l el remove {item}")
          with open("Cask","r") as ck:
              f = ck.read()

          f = f.replace("""\n(depends-on """ + item + """)""","")
          with open("Cask","w") as ck:
              ck.write(f)

    else:
      print("Exiting...")
      exit()
  if conf == False:
    for item in packages:
      if item != "-y":
        print(f"--> upm -l el remove {item}")
        with open("Cask","r") as ck:
            f = ck.read()

        f = f.replace("""\n(depends-on """ + item + """)""","")
        with open("Cask","w") as ck:
            ck.write(f)
    print("--> Cask install")
    os.system(f"cask install")

def lock():
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "Cask" not in files:
    print("--> cask init")
    os.system("cask init")
  print("--> cask install")
  os.system("cask install")

def install(args):
  conf = True
  print("[Upm]: Updating package configuration")
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "Cask" not in files:
    print("--> cask init")
    os.system("cask init")
  if len(args) == 1 or args == []:
    print("--> cask install")
    os.system("cask install")
  else:
    toprint = ""
    packages = args
    packages.remove(packages[0])
    for item in packages:
      if item != "-y":
        toprint += f"{item}, "
      if item == "-y":
        conf = False
    if conf == True:
      query = input(f"Do you want to install\n{toprint}(y/n)? ")
      if query == "y":
        for item in packages:
          if item != "-y":
            print("--> Writing packages...")
            with open("Cask","a") as ck:
                print(f"--> upm -l el install {item}")
                ck.write("""\n(depends-on """ + item + """)""")
      else:
        print("Exiting...")
        exit()
    if conf == False:
        for item in packages:
          if item != "-y":
            print("--> Writing packages...")
            with open("Cask","a") as ck:
                print(f"--> upm -l el install {item}")
                ck.write("""\n(depends-on """ + item + """)""")
    print("--> Cask install")
    os.system(f"cask install")
