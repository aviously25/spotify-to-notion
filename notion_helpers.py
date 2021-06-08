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
pages_url = 'https://api.notion.com/v1/pages'
req_headers = {
    'Authorization': 'Bearer {}'.format(NOTION_TOKEN),
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

# creates a page in the database with the given arguments


def create_page(album_name: str, artists: list, released: str, image: str):
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
            },
            "Image": {
                "type": "url",
                "url": image
            }
        }
    }

    r = requests.post(pages_url, headers=req_headers, data=json.dumps(body))
    return r.json()['id']


# fills page with tracks
def fill_page(tracks: list, page_id: str):
    children = []
    for track in tracks:
        children.append({
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "text": [{"type": "text", "text": {"content": "{}. {}".format(track['number'], track['name'])}}]
            }
        })
        children.append({
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "text": [{"type": "text", "text": {"content": ""}}]
            }
        })

    block_url = "https://api.notion.com/v1/blocks/{}/children".format(
        page_id)

    r = requests.patch(block_url, headers=req_headers,
                       data=json.dumps({"children": children}))
