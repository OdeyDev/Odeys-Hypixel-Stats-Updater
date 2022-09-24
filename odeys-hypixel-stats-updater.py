import os
import wget
import tempfile
import requests
import shutil
import sys
import json
from zipfile import ZipFile

os.system("title " + "Odey's Hypixel Stats Updater (" +
          "1.0.3" + ") github.com/OdeyDev // @odeydev")

latestRelease = requests.get(
    "https://api.github.com/repos/odeydev/odeys-hypixel-stats/releases/latest"
).json()

allReleases = requests.get("https://api.github.com/repos/odeydev/odeys-hypixel-stats/releases"
                           ).json()

releaseAssets = latestRelease["assets_url"]

assets = requests.get(
    releaseAssets).json()

insideAssets = assets[0]

releaseAssets = latestRelease["assets_url"]

fileName = insideAssets["name"]
fileName1 = fileName.replace(".zip", "")
fileVersion = fileName1.replace("odeys-hypixel-stats-", "")

assets = requests.get(
    releaseAssets).json()

insideAssets = assets[0]

settings = open("..\settings.json", "r")
settingsObj = json.load(settings)

tempFolder = tempfile.gettempdir()
tempPath = str(tempFolder)

fileVersionNoBeta = fileVersion.replace("-beta", "")
fileVersionBetaExists = fileVersion.replace(fileVersionNoBeta, "")

rel_data = json.dumps(allReleases)

rel_dict = json.loads(rel_data)

releasesNum = len(rel_dict)

URL = insideAssets["browser_download_url"]

for x in range(releasesNum):
    releaseCheck = allReleases[x]
    inRelAssets = releaseCheck["assets"]
    insideRelAssets = inRelAssets[0]
    fileName = insideRelAssets["name"]
    fileName1 = fileName.replace(".zip", "")
    fileVersion = fileName1.replace("odeys-hypixel-stats-", "")
    fileVersionNoBeta = fileVersion.replace("-beta", "")
    fileVersionBetaExists = fileVersion.replace(fileVersionNoBeta, "")

    if fileVersionBetaExists != "-beta":
        latestIsBeta = False
    else:
        latestIsBeta = True

    if latestIsBeta == False:
        if fileVersionBetaExists != "-beta":
            break

    elif settingsObj["betaupdates"] == True and latestIsBeta == True:
        if fileVersionBetaExists == "-beta":
            break


URL = insideRelAssets["browser_download_url"]

print("Updating release to", fileVersion)

response = wget.download(URL, "LatestVersion.zip")

backDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
statsDir = backDir + "\odeys-hypixel-stats"
if os.path.exists(statsDir) == True:
    shutil.rmtree(statsDir)
ZipFile("LatestVersion.zip").extractall(backDir)
os.remove("LatestVersion.zip")
settings.close()


sys.exit()
