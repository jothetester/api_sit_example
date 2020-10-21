import requests
import os
import json
import test_data.secrets as secrets


class searchSongs:

    def __init__(self, context, path, song_name, item_type):
        self.context = context
        self.endpoint = self.context.base_url + path
        self.song_name = song_name
        self.item_type = item_type
        self.params = {'q': self.song_name,
                       'type': self.item_type
                       }
        self.header={
          "Content-Type": "application/json",
          "Authorization": "Bearer {}".format(secrets.spotify_token)
        }
        self.response = None
        self.song_uri = None

    def search_for_a_track(self):
        self.response = requests.get(
            self.endpoint,
            params=self.params,
            headers=self.header
        )

    def get_song_uri(self):
        response_json = self.response.json()
        songs = response_json["tracks"]["items"]
        self.song_uri = songs[0]["uri"]
