# spotify-to-notion

1. run `pip install -r requirements.txt`
2. create a `.env` file in the root folder
3. enter these lines into the .env file:
```
SPOTIPY_CLIENT_ID=<your client id>
SPOTIPY_CLIENT_SECRET=<client secret>
NOTION_TOKEN=<your notion token>
NOTION_DATABASE=<your notion database url>
```
Note: you can access your spotify client id and secret by creating a new app in the spotify developer dashboard (https://developer.spotify.com/). Obtain the `NOTION_TOKEN` value by creating an integration with the notion api ([instructions here](https://developers.notion.com/docs/getting-started#create-a-new-integration))

4. then run `python3 main.py`