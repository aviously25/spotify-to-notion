import requests
import json
import os
from datetime import datetime

# get the notion env variables defined in a .env file
from dotenv import load_dotenv
load_dotenv()
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_DATABASE = os.getenv('NOTION_DATABASE')

# create requests important info
url = 'https://api.notion.com/v1/pages'
req_headers = {
    'Authorization': 'Bearer {}'.format(NOTION_TOKEN),
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

# creates a page in the database with the given arguments


def create_page(album_name: str, artists: list, released: str):
    body = {
        "parent": {
            "type": "database_id",
            "database_id": NOTION_DATABASE
        },
        "properties": {
            "Album Title": {
                "type": "title",
                "title": [{"type": "text", "text": {"content": album_name}}]
            },
            "Artist(s)": {
                "type": "rich_text",
                "rich_text": [{"type": "text", "text": {"content": ', '.join(artists)}}]
            },
            "Released": {
                "type": "date",
                "date": {
                    "start": released
                }
            }
        }
    }

    r = requests.post(url, headers=req_headers, data=json.dumps(body))

    print(r.text)
