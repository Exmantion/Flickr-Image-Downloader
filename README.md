# __Flickr Full-size Image Downloader__
Handy tool to download photos in full resolution from [Flickr](https://www.flickr.com/). 

# DISCLAIMER
This tool is meant for __personal use only__. Goal of this tool was to obtain image in high resolution - the exact same one which can be viewed on Flickr site. This tool does not allow to download original file if owner of it did not add such option on Flickr site. It is meant only as an alternative for making screenshots of a webpage just to have a wallpaper in good quality. This tool in nutshell, does the exact same thing as going into chromium Developer tools > Network > Filtering by Img and downloading the image this way which will be displayed on the list.

# Features
1. Download nice photos for the pleasure of your eyes.
2. What more do you want it to do?
3. Allows to download multiple photos at once.
4. Numbered or nice filenames.
5. Automatic download, press and forget.
6. Debugging options.

# How to install
Just download .py file and execute it. Python is required to do so:

`python3 Flickr-Image-Downloader.py`

# How to use
At first it is required to have links to the photos. They can be of a form as below:
```
https://www.flickr.com/photos/wernerkrause/52427331246/sizes/l/
https://www.flickr.com/photos/wernerkrause/52427331246/
https://www.flickr.com/photos/wernerkrause/52427331246
https://www.flickr.com/photos/steffe/52491777467/in/contacts/
```
Example and random photos.
Tool allows option to download multiple photos. Just paste all of the links into `input_urls.txt` file. 

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

# Other notes

Tool by default downloads all the photos in the highest possible resolution which is shared with public on Flickr site. It can be original file, if the owner allowed it. In other case, the photo will be with highest resolution which can be displayed on the Flickr site. 

To the filename (whatever to `FlickrFileNames` flag is set) will be added the resolution of the photo, further number is higher resolution:

`['sq', 'q', 't', 's', 'n', 'w', 'm', 'z', 'c', 'l', 'h', 'k', '3k', '4k', '5k', '6k', 'o']`

Other file resolutions can be easily obtained as well, although I do not see the point in doing so. 

# How to obtain the other (smaller) resolutions
Variable which you are looking for is the `all_sizes`. By default it takes last (highest) resolution, but you can program it to download any other. 


