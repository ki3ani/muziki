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
    
        scope = 'user-read-private user-read-email'
    
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    
        scope=scope)
    
        auth_url = sp_oauth.get_authorize_url()
    
        return redirect(auth_url)




