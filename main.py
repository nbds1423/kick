from src.webhook.webhook import send
from src.gateaway.KickClient import KickClient
from time import sleep
from src.database.KickDatabase import KickDatabase
import threading

def run_client():
    client = KickClient('IreliaBot')
    client.run()

"""
def run_webhook():
    while True:
        send('b0aty')
        sleep(60)
webhook_thread = threading.Thread(target=run_webhook)
"""

client_thread = threading.Thread(target=run_client)
client_thread.start()
#webhook_thread.start()
