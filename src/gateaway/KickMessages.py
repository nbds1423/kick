import websocket
import json

class KickMessages:
    def __init__(self, channel, message):
        self._url = "wss://ws-us2.pusher.com/app/eb1d5f283081a78b932c?protocol=7&client=js&version=7.4.0&flash=false"
        self._channel = channel
        self._message = message
        self._ws = websocket.WebSocketApp(
            self._url, on_open=self.on_open, on_message=self.on_message)

    def on_open(self, ws) -> None:

        id = self._channel['chatroom']['id']
        name = self._channel['user']['username']

        subscribe_event = {
            'event': 'pusher:subscribe',
            'data': {'auth': '', 'channel': f'chatrooms.{id}.v2'}
        }

        self._ws.send(json.dumps(subscribe_event))
        print(f'Irelia | Connected to {name} chat.')

    def on_message(self, ws, message) -> None:
        json_data = json.loads(message)
        data = json.loads(json_data['data'])

        self._message({
            'channel_id': data['chatroom_id'],
            'message': data['content'],
            'sender_id': data['sender']['id'],
            'sender_username': data['sender']['username'],
            'sender_slug': data['sender']['slug']
        })

    def run(self) -> None:
        self._ws.run_forever()
