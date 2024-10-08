## Install Python
https://www.python.org/downloads/ 

## Install Git
### For Windows Users :
Download git bash using the following link : \
https://git-scm.com/downloads \
Or open cmd and run : \
`winget install --id Git.Git -e --source winget` 
### For Linux Users
Use the appropriate package manager command, followed by `git` \
Example for Rel distro \
`sudo dnf install git`

## Create Google API Key

To create your application's API key:

1 - Go to the [API Console](https://console.cloud.google.com/welcome?project=scrapcomplo).\
2 - From the projects list, select a project or create a new one.\
3 - If the APIs & services page isn't already open, open the left side menu and select APIs & services.\
4 - On the left, choose Credentials.\
5 - Click Create credentials and then select API key. \
6 - Inside the searchbar find "Youtube Data API V3", click and enable it.

https://support.google.com/googleapi/answer/6158862?hl=en 

## Git clone
Run the following command in a terminal :
`git clone https://github.com/ElodieSavignard/fetch-social-network-data.git`

## Add your API Key inside script

Insert your API key in var `api_key = ''` inside the config.py file. 

## Install packages
Run the following command in a terminal :\
```pip install google-api-python-client openpyxl pandas``` 


### Run Script
For Linux Users :
`python3 full_youtube_fetch.py ChannelName` \
For Windows Users :
`python full_youtube_fetch.py ChannelName`
