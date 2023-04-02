### accepted urls:
urlss= ''' [ 
https://www.flickr.com/photos/wernerkrause/52427331246/sizes/l/
https://www.flickr.com/photos/wernerkrause/52427331246/
https://www.flickr.com/photos/wernerkrause/52427331246
https://www.flickr.com/photos/steffe/52491777467/in/contacts/
]'''

FlickrFileNames = True 
  # False means file names of each photo will be with numbers, as in Flickr database states
  # True means title of the photo from main page, useful for further debugging or to find author of the photo
Debugging = 2 #0,1(default),2
  # 0 means that the output of below cell will output only final info
  # 1 means info of each downlaoded photo will be progressively displayed
  # 2 means all debbuging will also be saved in txt file called debugging.txt
DownloadFiles = True
  # Download photos yes or no
  # Helpful in case of Debugging 



import requests
import os 
from datetime import datetime
import re

def ddownloader(direct_url, printt, titled_name = -1):
  global outputted_file,statisctics,nr_of_photo
  r = requests.get(direct_url)
  if titled_name == -1:
    file_name = direct_url[direct_url.rfind('/')+1:]
  else:
    file_name = titled_name
  with open(file_name,'wb') as f:
    f.write(r.content)
  outputted_file.write(direct_url+'\n')
  statisctics[0] += 1
  nr_of_photo += 1
  printstring = f"\tFile {file_name} saved!\n"
  if printt == 1:
    print(printstring)
  elif printt == 2:
    print(printstring)
    return printstring
  

exported_file = 'exported_urls.txt'
input_urls = 'input_urls.txt'
output_folder_name = 'gathered'

try:
  input_urls_var = open(input_urls, 'r')
except FileNotFoundError:
  input_urls_var = open(input_urls, 'x')
  print("No input file found, script is sad and angry because of you now")
  # raise SystemExit("No input file found, script is sad and angry becuase of you now")
  exit()

try:
  outputted_file = open(exported_file, 'w')
except FileNotFoundError:
  outputted_file = open(exported_file, 'x')  
  
if Debugging == 2:
  debugging_file = 'debugging.txt'
  try:
    debug = open(debugging_file, 'w')
  except FileExistsError:
    debug = open(debugging_file, 'x')
  
CURR_DIR = os.getcwd()
try:
  os.mkdir(f'{CURR_DIR}\{output_folder_name}')
except FileExistsError:
  pass
os.chdir(f'{CURR_DIR}\{output_folder_name}')
if Debugging == 1:
  print(f"Files will be saved: {os.getcwd()}\n")
elif Debugging == 2:
  print(f"Files will be saved: {os.getcwd()}\n")
  debug.write(f"Files will be saved: {os.getcwd()}\n")

statisctics = [0,0] #[success, error]
nr_of_photo = 1

if FlickrFileNames:
  custom_file_names = set()
seen = set()#find duplicates
duplicates_counter = 0
links_count = 0
for line in input_urls_var:
  if line.strip() in seen:
    duplicates_counter += 1
  else:
    seen.add(line.strip())
    links_count += 1
if Debugging > 0:
  print(f"{duplicates_counter} duplicates were found and removed, photos to download: {links_count}\n")
if Debugging == 2:
  debug.write(f"{duplicates_counter} duplicates were found and removed, photos to download: {links_count}\n\n")

for url in seen:
  url = url.replace('\n',"")
  if Debugging > 0:
    print(f"{nr_of_photo}: Gathering data for: {url}")
  if Debugging == 2:
    debug.write(f"{nr_of_photo}: Gathering data for: {url}\n")

  if url.rfind("sizes") != -1: #check if photo link is in change sizes site
    url = url[0:url.rfind("sizes")]
    if Debugging > 0:
      print("\tURL has been corrected")
    if Debugging == 2:
      debug.write(f"\tURL has been corrected\n")
       
  html = requests.get(url).text
  output = []
  searchstring ='params: {"photoModel":'
  for line in iter(html.splitlines()):
    if searchstring in line:
      output.append(line)
  try:
    output = output[0][13:]
  except IndexError:
    if Debugging > 0:
      print("\tPhoto could not be obtained, wrong address probably")
    if Debugging == 2:
      debug.write(f"\tPhoto could not be obtained, wrong address probably\n")
    statisctics[1] += 1
    continue
  if Debugging > 0:
    print("\tGathered source... continuing")
  if Debugging == 2:
    debug.write(f"\tGathered source... continuing\n")

  # yup, it is required
  false = False
  true = True
  null = -1
  outputdict = dict(eval(output))["photoModel"]['sizes']
  # outputdict = outputdict["photoModel"]['sizes']
  # print(outputdict)
  all_sizes = list(outputdict.keys()) 
  raw_url = outputdict[all_sizes[-1]]['src']
  direct_url = 'https://' + raw_url.replace('\/', '/')[2:]
  if Debugging > 0:
    print(f"\tAll image sizes available: {all_sizes}")
    print(f"\tDirect url: {direct_url}, raw url for debugging: {raw_url}")
  if Debugging == 2:
    debug.write(f"\tAll image sizes available: {all_sizes}\n")
    debug.write(f"\tDirect url: {direct_url}, raw url for debugging: {raw_url}\n")


  if FlickrFileNames:
    try:
      titled_name = html[html.find('<title>'):html.find('</title>')].replace("<title>", '')
      # titled_name = titled_name[:titled_name.find(' |')].replace(' ','_').replace("'","").replace("(", '').replace(")",'').replace("-", "_")
      titled_name = titled_name[:titled_name.find(' |')]
      titled_name = re.sub('[^a-zA-Z0-9 \n\.]', '', titled_name).replace('.','').replace(' ','_')
      if titled_name[:8] == 'Untitled':
        titled_name = titled_name + "_" + str(datetime.now().strftime("%d%m%Y_%H%M%S%f"))
      titled_name = f'{titled_name}_{str(all_sizes[-1])}{direct_url[direct_url.rfind("."):] }'
      titled_name = re.sub(r'&#x\.\.;',r'_', titled_name) 
    except:
      titled_name = f'NoCuteFilenameFound.{direct_url[direct_url.rfind("."):]}'
      
    #check if photo title was a duplicate 
    if titled_name in custom_file_names:
      titled_name = titled_name[:titled_name.find(".")] + "_" + str(datetime.now().strftime("%d%m%Y_%H%M%S%f")) + titled_name[titled_name.find("."):]
      custom_file_names.add(titled_name)
    else:
      custom_file_names.add(titled_name)

    if Debugging == 0 and DownloadFiles:
      ddownloader(direct_url, 0, titled_name)
    elif Debugging == 1:
      print(f"\tCustom filename: {titled_name}\n")
      if DownloadFiles:
        ddownloader(direct_url, 0, titled_name)
    elif Debugging == 2:
      print(f"\tCustom filename: {titled_name}\n")
      if DownloadFiles:
        ddownloader(direct_url, 0, titled_name)
      debug.write(f"\tFile saved with a cute {titled_name} custom filename!\n\n") 
      
  else: #if no flickr file names
    if Debugging == 0 and DownloadFiles:
      ddownloader(direct_url, 0)
    elif Debugging == 1 and DownloadFiles:
      ddownloader(direct_url, 1)
    elif Debugging == 2 and DownloadFiles:
      outputt = ddownloader(direct_url, 2)
      debug.write(outputt + '\n')  
  
try:
  if sum(statisctics) != links_count:
    print("some files were not downloaded")
  print(f"Total files requested: {links_count} ({sum(statisctics)}), Success: {statisctics[0]}, Errors: {statisctics[1]}\nSuccess percentage: {statisctics[0]/sum(statisctics)*100:.2f}%")
  if Debugging == 2:
    debug.write(f"Total files requested: {links_count} ({sum(statisctics)}), Success: {statisctics[0]}, Errors: {statisctics[1]}\nSuccess percentage: {statisctics[0]/sum(statisctics)*100:.2f}%")
except ZeroDivisionError:
  pass

input_urls_var.close()
outputted_file.close()
if Debugging == 2:
  debug.close()

  
  