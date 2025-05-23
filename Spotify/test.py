from tbearlib.spotify.authenticator import *
from tbearlib.spotify.decades import *
from tbearlib.spotify.playlist_data import *
import pandas as pd

# Authetication
cred = pd.read_csv(r"/Users/osito/Repositories/Scientia/Spotify/credentials.csv", header=None)
client_id = cred.iloc[0, 1]
client_secret = cred.iloc[1, 1]
redirect_uri = cred.iloc[2, 1]

auth = SpotifyAuthenticator(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri
)
sp = auth.authenticate()

# Playlist data
playlist_uri = 'https://open.spotify.com/playlist/4scXszKyPSHBuJJvgYk0HA?si=500e74758fb24633'
fetcher = PlaylistFetcher(sp)
all_tracks = fetcher.fetch_all_tracks(playlist_uri)

# Classify by Decade
classifier = DecadeClassifier()
decade_dataframes = classifier.classify_tracks(all_tracks)

# Export to Excel
output_path = "tracks_by_decade.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    for decade, df in decade_dataframes.items():
        if not df.empty:
            df.to_excel(writer, sheet_name=decade, index=False)
