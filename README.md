# Daily bing walls

A script to set the daily bing image as the wallpaper. It can also set from a random set of previously fetched wallpapers.

```
usage: daily.py [-h] [--random] [-p] [-d ROOT_DIR] [--viewer VIEWER]
                [--setter {feh,nitrogen,hsetroot}]

optional arguments:
  -h, --help            show this help message and exit
  --random              choose a random image from root_dir
  -p, --preview         only preview image, don't set/save
  -d ROOT_DIR, --root-dir ROOT_DIR
                        path to root directory
  --viewer VIEWER       specify preview tool
  --setter {feh,nitrogen,hsetroot}
                        specify tool to use when setting wallpaper
```

> You may change the default directory and default application by making small edits to the `daily.py` file.

## Dependencies

* python libraries
    * `requests`
    * `urllib`
    * `argparse`
* others
    * `hsetroot` | `nitrogen` | `feh` - application that can set wallpaper
