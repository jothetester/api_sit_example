from behave import *
from test_data import secrets
from lib.create_playlist import createPlaylist
from lib.search_songs import searchSongs
from lib.add_items_to_playlist import addItemsPlaylist
from lib.list_items_in_playlist import listTracks
from lib.delete_playlist import deletePlaylist

song_uri = None
playlist_id = None


@given('that a playlist called {playlist_name} is created in my spotify account')
def step_impl(context, playlist_name):
    path = 'v1/users/{}/playlists'.format(secrets.spotify_userid)
    new_playlist = createPlaylist(context, path, playlist_name, "a new playlist", False)
    new_playlist.create_a_new_playlist()
    assert (new_playlist.response.status_code == 201,
            "status code incorrect - Expected 201 found {}".format(new_playlist.response.status_code))
    global playlist_id
    playlist_id = new_playlist.response.json()["id"]


@when('I search for a {item} from album called {song}')
def step_impl(context, item, song):
    path = 'v1/search'
    search_songs = searchSongs(context, path, song, item)
    search_songs.search_for_a_track()
    assert (search_songs.response.status_code == 200,
            "status code incorrect - Expected 200 found {}".format(search_songs.response.status_code))
    search_songs.get_song_uri()
    global song_uri
    song_uri = search_songs.song_uri


@step('I add my favourite track to my playlist')
def step_impl(context):
    path = 'v1/playlists/{}/tracks'.format(playlist_id)
    add_items = addItemsPlaylist(context, path, song_uri)
    add_items.add_items_to_a_playlist()
    assert (add_items.response.status_code == 201,
            "status code incorrect - Expected 201 found {}".format(add_items.response.status_code))


@step('my favourite track is available in my playlist')
def step_impl(context):
    path = 'v1/playlists/{}/tracks'.format(playlist_id)
    search_playlist = listTracks(context, path)
    search_playlist.get_playlist_tracks()
    added_song_uri = search_playlist.response.json()["items"][0]["track"]["uri"]
    assert (added_song_uri == song_uri,
            "Expected song not added - track URIs don't match. Expected - {}, Found - {}"
            .format(song_uri, added_song_uri))
    unfollow_playlist(context)


'''
This removes the data created and enables the tests to start clean. 
'''


def unfollow_playlist(context):
    path = 'v1/playlists/{}/followers'.format(playlist_id)
    delete_playlist = deletePlaylist(context, path)
    deletePlaylist.unfollow_playlist()
    assert (delete_playlist.response.status_code == 200,
            "status code incorrect - Expected 201 found {}".format(delete_playlist.response.status_code))