import cloudscraper
from src.config.config import env

class Kick:
    def __init__(self):
        self._config = env()
        self._baseURL = "https://kick.com"
        self._instance = cloudscraper.create_scraper()
        self._headers = {
            "Cookie": self._config['cookie'],
            "X-XSRF-TOKEN": self._config['token'],
        }

    def message(self, channel, message) -> None:

        channelInfo = self.channel(channel)

        id = channelInfo['chatroom']['id']
        slug = channelInfo['slug']

        payload = {"content": message, "type": "message"}
        self._headers.update({"Referer": f'{self._baseURL}/{slug}'})
        self._instance.post(
            f'{self._baseURL}/api/v2/messages/send/{id}', headers=self._headers, data=payload)

    def channel(self, channel):
        request = self._instance.get(
            f'{self._baseURL}/api/v2/channels/{channel}', headers=self._headers)

        if request.status_code != 200:
            return

        data = request.json()
        return data
