import time
import sys
import getopt
import subprocess
import os
import requests
from sys import platform

def search(args):
    from lxml import html
    import requests

    response = requests.get("https://pypi.org/simple/")

    tree = html.fromstring(response.content)

    content = [package for package in tree.xpath('//a/text()')]


    if "--all" == args[1] or "-a" == args[1]:
      for i in content:
          print(f"{i}")
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


      for item in content:

        if query.lower() == item.lower() or q2.lower() == item.lower() or q2.lower() in item.lower() or query.lower() in item.lower():
          print(f"{item}")
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
