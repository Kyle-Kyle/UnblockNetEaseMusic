import os
import json

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
           "X-Real-IP": "211.161.244.70"}

def get_music_u():
    music_u = os.environ.get("MUSIC_U", None)
    assert music_u is not None, "Set MUSIC_U in environment variables first!"
    return music_u

def run():
    music_u = get_music_u()
    
    s = requests.Session()
    s.cookies.set("MUSIC_U", music_u, domain=".music.163.com")
    
    r = s.get("https://music.163.com/discover/toplist", headers=headers)
    html = BeautifulSoup(r.text, "html.parser")
    songs = json.loads(html.find(id="song-list-pre-data").text)
    assert len(songs), "Failed to obtain toplist!"
    print(len(songs))

run()
