########## PREPARATION ##########

# Import modules
import sys
import authorization
import pandas as pd
from tqdm import tqdm
import time

# Authorize and call access object 'sp'
sp = authorization.authorize()

# Get all genres
genres = sp.recommendation_genre_seeds()

# Set number of recommendaations per genre
no_recs = 100

# Initiate a dictionary with all the information you want to crawl
data_dict = {"id":[], "genre":[], "track_name":[], "artist_name":[], "valence":[], "energy":[]}

########## CRAWL DATA ##########

# Get recommendations for every genre
for g in tqdm(genres):

    # Get n recommendations
    recs = sp.recommendations(genres = [g], limit = no_recs)
    # json-like string to dictionary
    recs = eval(recs.json().replace("null", "-999").replace("false", "False").replace("true", "True"))["tracks"]

    # Crawl data from each track
    for track in recs:
        # ID and genre
        data_dict["id"].append(track["id"])
        data_dict["genre"].append(g)
        # Metadata
        track_meta = sp.track(track["id"])
        data_dict["track_name"].append(track_meta.name)
        data_dict["artist_name"].append(track_meta.album.artists[0].name)
        # Valence and Energy
        track_features = sp.track_audio_features(track["id"])
        data_dict["valence"].append(track_features.valence)
        data_dict["energy"].append(track_features.energy)

        # Wait 0.2 seconds per track so that API does not overheat
        time.sleeo(0.2)
        
########## PROCESS DATA ##########

# Store data in data frame        
df = pd.DataFrame(data_dict)

# Drop duplicates
df.drop_duplicates(subset = "id", keep = "first", inplace = True)
df.to_csv("valence_arousal_dataset.csv", index = False)