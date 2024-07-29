import pandas as pd
import requests, zipfile, io
from bs4 import BeautifulSoup as bs

path_to_save_hps_data = 'YOUR_PATH_HERE' # This will be where you want to save the hps csv's

hps_html = requests.get('https://www.census.gov/programs-surveys/household-pulse-survey/datasets.html') # Make the initial request to hps
if hps_html.status_code == 200: # If request status code is good, proceed

    
    soup = bs(hps_html.content, "html.parser") # Get all content with bs html.parser
    
    links = soup.find_all('a', href=True) # Find all elements with the tag <a>

    
    out = []
    for link in links:
        out.append(link.get("href")) # For each item, get all the href's
    
    zip_data = [y for y in out if "PUF_CSV.zip" in y] # Get just the ones that contain PUF_CSV.zip
    
    for link in zip_data:
        if link.startswith('//'): # If the link has an inncorrect url, fix it and move on
            link = 'https:'+link
            
        # Extract zip file from path and save to a location
        r = requests.get(link) # Make inital request
        z = zipfile.ZipFile(io.BytesIO(r.content)) # open the zipfile using the ZipFile package

        #Inside each zip, there are 3 files, the data dictionary, a regwgt file, and the file we want
        newlist = [x for x in z.namelist()  if "csv" in x] # Only keep the csv's
        newlist = [x for x in newlist  if not "repwgt" in x] # remove repwgt from zipfile
        member_name = newlist[0] # The file left will be the csv we want
        
        z.extract(member = member_name,path = path_to_save_hps_data) # Extract the files and save them
        print(f'{member_name} saved to {path_to_save_hps_data}')
else:
    print('Error: Response code != 200')
