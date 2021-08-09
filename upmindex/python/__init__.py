import time
import sys
import getopt
import subprocess
import os
import requests
from sys import platform

def search(args):
    if platform == "win32" or platform == "win64":
        path = r"C:\Windows\System32\upm\resources\python\pypi"
    elif platform == "linux" or platform == "linux2" or platform == "darwin":
        path = "/usr/bin/upm/resources/python/pypi"
    f = open(path,"r")
    if "--all" == args[1] or "-a" == args[1]:
      content = f.read()
      print(content)
    else:
      print("--> Searching...")
      pypi = []
      packages = ""
      argx = args
      argx.remove("search")
      query = ""
      for item in argx:
        if len(argx) != 1:
            if item != argx[len(argx)-1]:
                query += item + " 1"
            else:
                query += item + " "
        else:
            query = item
      q2 = query.replace(" ","-")
      q2 = query.replace(".","-")
      content = f.read()
      line = content.replace("\n"," ")
      contents = line.split(" ")
      for item in contents:
          if item == query:
              print(item)
      for item in contents:
        if query == item or q2 == item or q2 in item or query in item:
          print(f"{item}\n")
      print("--> Finished Search!")

def info(args):
    argx = args
    argx.remove("info")
    for item in argx:
        if len(argx) != 1:
            if item != argx[len(argx)-1]:
                query += item + "-"
            else:
                query += item
        else:
            query = item
    query.replace(" ","")
    query.replace("\n","")
    pkg = requests.request("GET",url=f"https://pypi.org/pypi/{query}/json")

    try:
        pkg = pkg.json()
    except:
        return print("package not found")
    name = query
    author = pkg["info"]["author"]
    desc = pkg["info"]["description"]
    ver = pkg["info"]["version"]
    print(f"Name: {name}\nVersion: {ver}\nAuthor: {author}\nDescription: {desc}")
