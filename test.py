playlist_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'

def get_video_ids(youtube,playlist_id):

    video_ids = [ ] 

    request = youtube.playlists().list(
        part="snippet,contentDetails",
        playlistId = playlist_id , 
        maxResults=25
    )
response = request.execute()
for item in response['items']: 
    video_ids.append(item['contentDetails'][videoId])


