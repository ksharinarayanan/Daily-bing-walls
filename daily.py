import requests, urllib.request, os, random, sys
from datetime import datetime
import argparse

root_dir = "~/Pictures/bing"
wallpaper_setters = ["feh", "nitrogen", "hsetroot"]

parser = argparse.ArgumentParser()

parser.add_argument("--random", help="choose a random image from root_dir", action="store_true")
parser.add_argument("-p", "--preview", help="only preview image, don't set/save", action="store_true")
parser.add_argument("-d", "--root-dir", help="path to root directory", default=root_dir)
parser.add_argument("--viewer", help="specify preview tool", default="xdg-open")
parser.add_argument("--setter", help="specify tool to use when setting wallpaper", choices=wallpaper_setters, default="hsetroot")

args = vars(parser.parse_args())

def set_wallpaper(img_name, setter_app):
    if setter_app == "hsetroot":
        cmd = f"hsetroot -cover {img_name}"
    elif setter_app == "feh":
        cmd = f"feh --bg-fill {img_name}" # note that this sets it on all monitors
    elif setter_app == "nitrogen":
        cmd = f"nitrogen {img_name}"
    os.system(cmd)

def download_daily_image():
    response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").json()
    url = "https://bing.com" + response['images'][0]['url']
    filename, _ = urllib.request.urlretrieve(url, "/tmp/daily.jpg")
    return filename

def save_wallpaper():
    fileName = datetime.now().strftime("bing-%d-%m-%Y")
    savepath = os.path.join(root_dir, fileName) + '.jpg'
    cmd = f"cp /tmp/daily.jpg {savepath}"
    os.system(cmd)
    return savepath

def preview(img_path, preview_tool):
    # this should work for most programs, i think
    cmd = f"{preview_tool} {img_path}"
    os.system(cmd)

def get_random_image(filepath):
    filelist = []
    for root, _, files in os.walk(filepath):
        for filename in files:
            if filename.split(".")[-1] in ["jpeg", "png", "jpg"]: # add more extensions if needed
                filelist.append(os.path.join(root, filename))

    if len(filelist) == 0:
        print("[Error] directory is empty!")
        sys.exit(1)
    return random.choice(filelist)

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return 0
    return 1

def fullpath(shortpath):
    return os.path.expanduser(shortpath)

if __name__ == "__main__":
    # making sure that the root-dir exists at startup
    root_dir = fullpath(root_dir)
    make_dir(root_dir)

    if args["random"]:
        fname = get_random_image(root_dir)
    else:
        # just download
        fname = download_daily_image()

    if args["preview"]:
        preview(fname, args["viewer"])
    else:
        if args["random"]:
            set_wallpaper(fname, args["setter"])
        else:
            savepath = save_wallpaper()
            set_wallpaper(savepath, args["setter"])
