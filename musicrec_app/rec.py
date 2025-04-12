#Using a rule based content filtering system
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.feature_extraction.text import TfidfVectorizer

file_path = r"musicrec_app\data\Music.csv"

SONG_DATA = pd.read_csv(file_path, sep=',')
SONG_DATA.dropna(subset=['name', 'artist'], inplace=True)  

scaler = MinMaxScaler()
SONG_DATA[['valence', 'energy', 'danceability', 'acousticness']] = scaler.fit_transform(
    SONG_DATA[['valence', 'energy', 'danceability', 'acousticness']]
)

# Apply TF-IDF to encode artist names efficiently
tfidf_vectorizer = TfidfVectorizer()
artist_tfidf_matrix = tfidf_vectorizer.fit_transform(SONG_DATA['artist'])

def get_recommendations(search_query, top_n=30):
    search_query = search_query.strip().casefold()  
    recommendations = []

    # 1. Search for exact matches in artist and album_name
    exact_matches = SONG_DATA[
       (SONG_DATA['artist'].str.contains(search_query, case=False, na=False)) |
       (SONG_DATA['album_name'].str.contains(search_query, case=False, na=False))

    ]
    
    if not exact_matches.empty:
        recommendations.extend(exact_matches[['name', 'artist', 'img', 'track_url']].values.tolist())

    # 2. Search for exact matches in song names
    song_matches = SONG_DATA[SONG_DATA['name'].str.casefold() == search_query]
    
    if not song_matches.empty:
        recommendations.extend(song_matches[['name', 'artist', 'img', 'track_url']].values.tolist())

    # 3. If no matches were found, recommend songs by the same artist
    if song_matches.empty and exact_matches.empty:
        return []  

    matched_artists = set(song_matches['artist']) | set(exact_matches['artist'])

    artist_songs = SONG_DATA[
        (SONG_DATA['artist'].isin(matched_artists)) & 
        (~SONG_DATA['name'].str.casefold().isin([search_query]))
    ]

    recommendations.extend(artist_songs[['name', 'artist', 'img', 'track_url']].values.tolist())

    return recommendations[:top_n]  
