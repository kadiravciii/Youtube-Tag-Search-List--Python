from googleapiclient.discovery import build
import json

DEVELOPER_KEY = "AIzaSyCE5tWkUro0wwxJoJZ3-bKWKo_ag98ChuI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
search_words = "dropshipping"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
        q=search_words,
        type="video",
        order='viewCount',
        part='id,snippet',
        maxResults=5
).execute()

videos = []

for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
        videos.append(search_result)

for i, video in enumerate(videos, start=1):
    print(f"{i}. {video['snippet']['title']}: https://www.youtube.com/watch?v={video['id']['videoId']}")
