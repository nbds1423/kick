import requests
from src.services.Kick import Kick

kick = Kick()
live = True

def send(channelName) -> None:
    global live
    channel = kick.channel(channelName)
    livestream = channel['livestream']

    if livestream and live:
        try:
            username = channel['user']['username']
            profile_pic = channel['user']['profile_pic']
            title = livestream['session_title']
            viewers = livestream['viewer_count']
            game = livestream['categories'][0]['name']
            
            if livestream and 'thumbnail' in livestream and livestream['thumbnail']:
                thumbnail =  livestream['thumbnail']['url']
            else:
                thumbnail = "https://static-cdn.jtvnw.net/ttv-static/404_preview-320x180.jpg"

            webhook(username, profile_pic, title, viewers, game, thumbnail)

            live = False
        except Exception as e:
            raise Exception('Error in file webhook.py', e)

def webhook(name, profile_pic, title, viewers, game, thumbnail) -> None:

    url = f"https://kick.com/{name}"

    payload = {
        "username": "Adriana",
        "avatar_url": profile_pic,
        "content": f"Rapaziada <@&796520086969384961>, {name}, acabou de abrir a live {url}",
        "embeds": [
            {
                "author": {
                    "name": name,
                    "url": url,
                    "icon_url": profile_pic
                },
                "title": title,
                "url": url,
                "color": 13916207,
                "thumbnail": {
                    "url": profile_pic
                },
                "image": {
                    "url": thumbnail
                },
                "fields": [
                    {
                        "name": "Viewers",
                        "value": viewers,
                        "inline": True
                    },
                    {
                        "name": "Game",
                        "value": game,
                        "inline": True
                    }
                ]
            }
        ], }
    requests.post('', json=payload)
    print('Webhook | Sent with success!')
