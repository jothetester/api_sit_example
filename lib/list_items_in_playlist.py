import requests
import json
import test_data.secrets as secrets


class listTracks:
    def __init__(self, context, path ):
        self.context = context
        self.endpoint = self.context.base_url + path
        self.header={
          "Content-Type": "application/json",
          "Authorization": "Bearer {}".format(secrets.spotify_token)
        }


    def get_playlist_tracks(self):
        self.response = requests.get(
            self.endpoint,
            headers=self.header
        )
