import requests
import json
import os
import shutil

def getgithubcom(repolink):
    repostuffs = repolink.replace("https://github.com/","")
    repostuffs = repolink.replace("github.com/","")
    print(repostuffs)
    repostuffs = repostuffs.replace("/"," ")
    print(repostuffs)
    repolist = repostuffs.split()
    print(repolist)
    author = repolist[0]
    modname = repolist[1]
    linktocfg = f"https://raw.githubusercontent.com/{author}/{modname}/main/"
    return linktocfg

def add2upm(lang,args):
    exec = args
    files = []
    for file in os.listdir(os.getcwd()):
        files.append(file)
    if "upm.json" in files:
        with open(f"{os.getcwd()}/upm.json") as l:
            upx = json.load(l)
    if exec[0] in ["install","i","add"]:
        packages = args
        packages.remove(exec[0])

        for item in packages:
            if item not in upx[lang]:
                upx[lang].append(item)
    if exec[0] in ["remove","r"]:
        packages = args
        packages.remove(exec[0])
        for item in packages:
            if item not in upx[lang]:
                upx[lang].remove(item)
    with open(f"{os.getcwd()}/upm.json","w") as l:
        json.dump(upx,l)
def addsrc(dpath,alias,link):
    link = link.replace("https://","")
    link = f"https://{link}"
    try:
        if link.startswith("https://github.com"):
            link = getgithubcom(link)
        if link.startswith("github.com"):
            link = getgithubcom(link)
        release = f"{link}/release.json"
        release = release.replace("//","/")
        release = release.replace("https:/","https://")
        packages = f"{link}/packages.json"
        packages = packages.replace("//","/")
        packages = packages.replace("https:/","https://")
        rel = requests.request("GET",url=release)
        rel = rel.json()
        pkgs = requests.request("GET",url=packages)
        pkgs = pkgs.json()
    except:
        return print("ERROR: 'Unable to get release.json/packages.json from source'")
    with open(f"{dpath}/sources.json","r") as k:
        srcs = json.load(k)
    for item in srcs:
        if item == alias:
            return print("ERROR:'Alias for source exists, please pick new alias'")
    for item in srcs:
        if srcs[item] == link:
            return print("ERROR:'Source exists, please use edit action'")
    srcs[alias] = link
    with open(f"{dpath}/sources.json","w") as k:
        json.dump(srcs,k)
    print(f"--> Successfully added {alias} to sources !")

def removesrc(dpath,alias):
    with open(f"{dpath}/sources.json","r") as k:
        srcs = json.load(k)
    if alias in srcs:
        del srcs[alias]
    else:
        return print("Error: alias not found")

    with open(f"{dpath}/sources.json","w") as k:
        json.dump(srcs,k)
    print(f"--> Successfully removed {alias} from sources !")

def update(dpath):
    failed = 0
    got = 0
    with open(f"{dpath}/sources.json","r") as k:
        srcs = json.load(k)
    for item in srcs:
        link = srcs[item]
        alias = item
        link = link.replace("https://","")
        link = f"https://{link}"
        try:
            if link.startswith("https://github.com"):
                link = getgithubcom(link)
            if link.startswith("github.com"):
                link = getgithubcom(link)
            print(f"--> Getting {link}")
            release = f"{link}/release.json"
            release = release.replace("//","/")
            release = release.replace("https:/","https://")
            packages = f"{link}/packages.json"
            packages = packages.replace("//","/")
            packages = packages.replace("https:/","https://")
            rel = requests.request("GET",url=release)
            rel = rel.json()
            pkgs = requests.request("GET",url=packages)
            pkgs = pkgs.json()
            print(f"--> Got {link}")
            got += 1
        except:
            print(f"--> Failed: {link}")
            failed += 1
            print("ERROR: 'Unable to get release.json/packages.json from source'")
    print(f"---------\nGot {got} source(s)\nFailed {failed} source(s)")

def zip(out,dir):
    shutil.make_archive(out, 'zip', dir)
