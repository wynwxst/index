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
    response = requests.request("GET",url=f"https://rubygems.org/api/v1/search.json?query={query}")
    response = response.json()


    amt = 0
    toprint = ""
    while amt != "exit":
        try:
            #var = response[0]["metadata"]["package"]["name"]
            for var in response[amt]:
                print(var)
                #if query in str(var):
                #for word in str(var):
                    #print(word)
                    #if word.startswith("https://") == False and word.startswith("{") == False:
                        #print(f"{word}\n")

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
    response = requests.request("GET",url=f"https://rubygems.org/api/v1/gems/{query}.json")
    response = response.json()
    name = response["name"]
    ver = response["version"]
    desc = response["info"]
    author = response["authors"]
    print(f"Name: {name}\nVersion: {ver}\nAuthor: {author}\nDescription: {desc}")
