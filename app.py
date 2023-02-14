from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import secrets
from flask import redirect
from flask import request


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)




@app.route('/auth')

def auth():
    
    
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv('CLIENT_ID'),
    
        client_secret=os.getenv('CLIENT_SECRET'),
    
        redirect_uri='http://localhost:5000/callback',
    
        scope='user-top-read')
    
        auth_url = sp_oauth.get_authorize_url()
    
        return redirect(auth_url)


@app.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'),
                            client_secret=os.getenv('CLIENT_SECRET'),
                            redirect_uri='http://localhost:5000/callback',
                            scope='user-top-read')
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    sp = spotipy.Spotify(auth=access_token)
    top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=10)
    track_list = []
    for track in top_tracks['items']:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        track_list.append(f"{track_name} by {artist_name}")
    return render_template('top_tracks.html', tracks=track_list)









