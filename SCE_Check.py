import requests
import os
from bs4 import BeautifulSoup
from discord import SyncWebhook

WEBHOOK_URL = ''
ARCHIVE_FILE = os.path.join(os.path.dirname(__file__),'events.txt')

def main():
    if os.path.exists(ARCHIVE_FILE):
        with open(ARCHIVE_FILE,'r') as f:
            old_events = f.read().splitlines() 
    url = 'https://www.steamcardexchange.net/index.php?showcase-filter-genre-999'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('div', class_='showcase-game-list-item')
    event_names = [ item.find('h2').text for item in items]
    for event_name in event_names:
        if not event_name in old_events:
            webhook = SyncWebhook.from_url(WEBHOOK_URL)
            webhook.edit(name="SCE")
            webhook.send(f"New Steam event added to SCE: {event_name}")
            with open(archive_file,'a') as f:
                f.write(f"{event_name}\n")

if __name__ == '__main__':
    main()
