import time
import sys
import getopt
import subprocess
import os
import requests
import json

def search(args):
    print("--> Searching...")
    argx = args
    argx.remove("search")
    for item in argx:
        if len(argx) != 1:
            if item != argx[len(argx)-1]:
                query += item + " 1"
            else:
                query += item + " "
        else:
            query = item
    query.replace(" ","+")
    query.replace("\n","")
    response = requests.request("GET",url=f"https://api.npms.io/v2/search?q={query}")
    response = response.json()


    amt = 0
    toprint = ""
    while amt != "exit":
        try:
            var = response["results"][amt]["package"]["name"]
            print(f"{var}\n")
            amt += 1
        except KeyError:
            amt = "exit"
        except IndexError:
            amt = "exit"

    print("--> Finished Search!")

def info(args):
    argx = args
    argx.remove("info")
    for item in argx:
        if len(argx) != 1:
            if item != argx[len(argx)-1]:
                query += item + " 1"
            else:
                query += item + " "
        else:
            query = item
    query.replace(" ","+")
    query.replace("\n","")
    response = requests.request("GET",url=f"https://api.npms.io/v2/package/{query}")
    response = response.json()
    name = response["collected"]["metadata"]["name"]
    ver = response["collected"]["metadata"]["version"]
    desc = response["collected"]["metadata"]["description"]
    author = response["collected"]["metadata"]["author"]["name"]
    print(f"Name: {name}\nVersion: {ver}\nAuthor: {author}\nDescription: {desc}")
