import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, redirect, request, session
import requests
import pprint


client_id="4063cdbe68ea499a92861b915ff0e537"
client_secret="4d5c47c885634e32a745ca8e4e87912b"
redirect_uri = "http://127.0.0.1:5000/redirect"
scope = 'playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,scope=scope))


# # shows ueer playlists
# results = sp.current_user_playlists(limit=50)
# for i, item in enumerate(results['items']):
#     print("%d %s" % (i, item['name']))


