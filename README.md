# __Flickr Full-size Image Downloader DEV__
Handy tool to download photos in full resolution from [Flickr](https://www.flickr.com/). 

# DISCLAIMER
This tool is meant for __personal use only__. Goal of this tool was to obtain images in high resolution - the exact same one which can be viewed on Flickr site. This tool does not allow to download original files if owner of them did not add such option on Flickr site. It is meant only as an alternative for making screenshots of a webpage just to have a wallpaper in a good quality. This tool in a nutshell, does the exact same thing as going into chromium Developer tools > Network > Filtering by Img and downloading the image which will be displayed on the list.

# Description
This handy small tool is design to download full resolution images from Flickr page. It allows downloading multiple photos at once. 

Designed so you can enjoy the eyes with beautiful images as your wallpaper! 

Uses single python file or can be run in Google Colab. Really easy to use, in my opinion.
Free and open-source.

# Features
1. Download nice photos for the pleasure of your eyes.
2. What more do you want?
3. Allows to download multiple photos at once.
4. Numbered or nice filenames.
5. Duplicate finder for input links.
6. Automatic download: press and forget.
7. Debugging options.


# Required packages
### Local install
```
import requests
import os 
from datetime import datetime
import re
```

### [Google Colab](https://colab.research.google.com/)
Doesn't matter since it is already installed for you.

# How to install
Two options are available: Local and in Google Colab.

## Local install 
Just download `*.py` file and execute it. Python is required to do so:

`python3 Flickr-Image-Downloader.py`

If there won't be any `input_urls.txt` file, the script will create one and become very angry.

## [Google Colab](https://colab.research.google.com/)
Google Colab is a free site on which you can use python online in a handy notebook. you don't need to install anything, all packages are already installed. In a matter of fact, you get access to the full linux machine which is quite powerful. Just remember: all files you created in this machine are __temporary and will be deleted__. The code itself will require a re-run but will stay. 

Go to the site: [Google Colab](https://colab.research.google.com/) `https://colab.research.google.com/`.
Click: File > Upload notebook and pick `*.ipynb` from sources. Than, follow the instructions in the following code block. To run the first code block, click on it so that cursor blinks there, and press `Shift+Enter` to execute. First run will take around 10s-15s since virtual machine has to be connected, allocated, etc.

On the Files section there will be folder `gathered` with all your photos. You can download each individually by right-clicking it, but for the easiness of use, make archive with all of your photos and than downlaod it.

# How to use
At first it is required to have links to the photos. They can be of a form as below:
```
https://www.flickr.com/photos/wernerkrause/52427331246/sizes/l/
https://www.flickr.com/photos/wernerkrause/52427331246/
https://www.flickr.com/photos/wernerkrause/52427331246
https://www.flickr.com/photos/steffe/52491777467/in/contacts/
```
Example and random photos.
Tool allows option to download multiple photos. 

Just paste all of the links into `input_urls.txt` file and run. All photos should be saved in `gathered` folder.  

### __Three setup options__
At the current version 3 setup options can be changed:
* `FlickrFileNames = False` 

`False` means file names of each photo will be with numbers, as a Flickr database states.

Example: `52581559660_becc9e6cda_o.jpg`

`True` means title of the photo from photo page on Flickr. Usefull to find author of the photo.

Example: `Bee_Eater_on_a_Wire_o.jpg`

Photo for the example: [here](https://www.flickr.com/photos/wernerkrause/52427331246/).

* `Debugging = 2`

`0` means that the output will contain only final info.

`1` means info of each downloaded photo will be progressively displayed.

`2` means all debugging will also be saved in .txt file called `debugging.txt`

* `DownloadFiles = True`

Download photos (`True`) or don't download photos (`False`).
Helpful in case of Debugging - makes less impact on Flickr servers. When combined with `Debugging = 0` makes the tool pretty useless.

### __Hint__

To easily download more images, you can open each photo in separate tab. Than, click on the first one. While holding `Shift` key click on the last one. All of the tabs should be selected now. Next, right click on the selection and select `Copy sites addresses` and than paste them into the input file. Works on Opera browser but all of the Chromium-based browsers should have such option.


# How it works from kitchen side of things
Basically, it obtains the source of the webpage (variable `html`). In it, script looks for `searchstring` phrase which I discovered to be reliable and repetitive. If this phrase is not found, script skips link. In `outputdict` dictionary is located every available resolution. Following lines extract needed data and assign it for further use:

```
all_sizes = list(outputdict.keys()) 
raw_url = outputdict[all_sizes[-1]]['src']
```

`-1` in here means last from all available sizes, that is the bestest quality.

Then, happens some amount of formatting, obtaining title of the photo and magic stuff which allows to handle errors, like the empty strings and doubled filenames.

Sorry for the mess in the code, adding `Debugging` variable made code less readable, but at some point of writing was very useful so I left it just in case.


# Other notes
Tool by default downloads all the photos in the highest possible resolution which is shared with public on Flickr site. It can be original file, if the owner allowed it. In other case, the photo will be with highest resolution which can be displayed on the Flickr site. 

To the filename (whatever to `FlickrFileNames` flag is set) will be added the resolution of the photo, further number is higher resolution:

`['sq', 'q', 't', 's', 'n', 'w', 'm', 'z', 'c', 'l', 'h', 'k', '3k', '4k', '5k', '6k', 'o']`

Other file resolutions can be easily obtained as well, although I do not see the point in doing so. 

# How to obtain other (smaller) resolutions
Variable which you are looking for is the `all_sizes`. By default it takes last (highest) resolution, but you can program it to download any other. `raw_url = outputdict[all_sizes[-1]]['src']` is the line you want to look at.