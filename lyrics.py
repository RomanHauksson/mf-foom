# This script downloads the lyrics of all MF DOOM songs from Genius.com into a JSON file

import os
from lyricsgenius import Genius
import json

# https://lyricsgenius.readthedocs.io/en/master/examples/snippets.html#getting-the-lyrics-for-all-songs-of-a-search
token = os.getenv("GENIUS_API_KEY")
genius = Genius(token)
lyrics = []

# If the song title contains any of these words, it will be excluded from the results
genius.excluded_terms = ["remix", "mix", "live", "instrumental"]

artist = genius.search_artist("MF DOOM")
for song in artist.songs:
    lyrics.append(song.lyrics)

# Save lyrics to a file called "lyrics.json"
with open('lyrics.json', 'w') as f:
    json.dump(lyrics, f)