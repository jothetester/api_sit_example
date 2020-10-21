import requests
import json
import test_data.secrets as secrets

class createPlaylist:
    def __init__(self, context, path, playlist_name, playlist_description,playlist_permission):
        self.context = context
        self.endpoint = self.context.base_url + path
        self.playlist_name = playlist_name
        self.playlist_description = playlist_description
        self.playlist_permission = playlist_permission
        self.header={
          "Content-Type": "application/json",
          "Authorization": "Bearer {}".format(secrets.spotify_token)
        }

    def create_request_body(self):
        request_body = json.dumps({
            "name": self.playlist_name,
            "description": self.playlist_description,
            "public": self.playlist_permission
        })
        return request_body

    def create_a_new_playlist(self):
        data = self.create_request_body()
        self.response = requests.post(
            self.endpoint,
            data=data,
            headers=self.header
        )