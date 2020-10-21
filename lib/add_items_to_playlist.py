import requests
import test_data.secrets as secrets

class addItemsPlaylist:
    def __init__(self, context, path, song_uri):
        self.context = context
        self.endpoint = self.context.base_url + path
        self.song_uri = "uris={}".format(song_uri)
        self.header={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(secrets.spotify_token)
        }

    def add_items_to_a_playlist(self):
        self.response = requests.post(
            self.endpoint,
            params=self.song_uri,
            headers=self.header

        )