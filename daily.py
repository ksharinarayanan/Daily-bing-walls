import requests, urllib.request, os, random, time, sys
from datetime import datetime

root_dir = "~/Pictures/BingWallpapers/"

def dailyImage (): 

    response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").json()

    url = "https://bing.com" + response['images'][0]['url']

    urllib.request.urlretrieve(url, "daily.jpg")
    
    cmd = "hsetroot -cover daily.jpg"
    os.system(cmd) 

    fileName = datetime.now().strftime("%d%m%Y")

    cmd = "cp daily.jpg " + (root_dir + fileName + ".jpg")
    os.system(cmd)

def randomImage (): 

    command = "ls " + root_dir

    ls = os.popen(command).read().split('\n')

    if (len(ls) == 0 or set(ls) == set([''])): 
        print ("No images found")
        return

    random.seed(time.perf_counter())
    picture = root_dir + (random.choice(ls))

    print ("Setting " + picture)

    command = "hsetroot -cover " + picture

    os.system(command)

command = "ls ~/Pictures"

ls = os.popen(command).read().split('\n')

if ("BingWallpapers" not in ls):
    os.system("mkdir ~/Pictures/BingWallpapers/")

argumentList = sys.argv[1:]

if len(argumentList) > 0:

    argumentList = argumentList[0]

    if argumentList in ["-h", "--help"]:
        print ("Help menu\n\
default: Set today's bing wallpaper\n\
-r: Set a random image from the past bing wallpapers")

    elif argumentList in ["-r", "--random"]:
        randomImage()

else:
    dailyImage()
