### Install Python
https://www.python.org/downloads/ \

### Create Google API Key

To create your application's API key:

1 - Go to the [API Console](https://console.cloud.google.com/welcome?project=scrapcomplo).\
2 - From the projects list, select a project or create a new one.\
3 - If the APIs & services page isn't already open, open the left side menu and select APIs & services.\
4 - On the left, choose Credentials.\
5 - Click Create credentials and then select API key.
6 - Inside the searchbar find "Youtube Data API V3", click and enable it.

https://support.google.com/googleapi/answer/6158862?hl=en \

### Add your API Key inside script

Insert your API key inside var `API_KEY = ''` at line 100 on the full_youtube_fetch.py script. \

### Install packages
Run the command inside your terminal :\
```pip install google-api-python-client openpyxl pandas``` \


### Run Script
python3.9 full_youtube_fetch.py ChannelName
