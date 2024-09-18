import os
import googleapiclient.discovery
import pandas as pd
import sys
from datetime import datetime
from googleapiclient.discovery import build



def get_channel_id(api_key, channel_name):    
    request = youtube.search().list(
        q=channel_name,
        part='snippet',
        type='channel',
        maxResults=1
    )
    response = request.execute()
    
    if response['items']:
        channel_id = response['items'][0]['snippet']['channelId']
        return channel_id
    else:
        return None
                                                                                

def get_channel_videos(channel_id):
    request = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    )
    response = request.execute()
    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while True:
        playlist_request = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()

        for item in playlist_response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_title = item['snippet']['title']
            video_published_at = item['snippet']['publishedAt']
        
            video_request = youtube.videos().list(
                part='statistics,contentDetails',
                id=video_id
            )
            video_response = video_request.execute()
            video_duration_ytb = video_response['items'][0]['contentDetails']['duration']
            video_duration = video_duration_ytb[2:]
            try:
                view_count = video_response['items'][0]['statistics']['viewCount']
            except KeyError:
                view_count = "No views"
            try:
                video_like = video_response['items'][0]['statistics']['likeCount']
            except KeyError:
                video_like = "No likes"
            try:
                video_comment = video_response['items'][0]['statistics']['commentCount']
            except KeyError:
                video_comment = "Comments have been disabled"
        
            
            videos.append({
                'title': video_title,
                'published at': video_published_at,
                'views count': view_count,
                'duration': video_duration,
                'likes': video_like,
                'comments': video_comment
            })

        next_page_token = playlist_response.get('nextPageToken')
        if next_page_token is None:
            break

    return videos

def save_to_excel(videos, channel_name):
    today_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{channel_name}_{today_date}.xlsx"
    df = pd.DataFrame(videos)
    df.to_excel('./Results/{filename}', index=False)
    print(f"The data has been saved in the file {filename} inside the folder Results")



if __name__ == "__main__":
    API_KEY = 'AIzaSyC8VRoeokncs5zdKEo03C4J4rPgbox-HgA'
    channel_name = sys.argv[1]
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    channel_id = get_channel_id(API_KEY, channel_name)
    if channel_id:
        print(f"The channel ID '{channel_name}' is : {channel_id}")
    else:
        print(f"No channel found with the name '{channel_name}'.")

    videos = get_channel_videos(channel_id)
    save_to_excel(videos, channel_name)