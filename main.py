import pandas as pd


# Use the pandas `.read_csv()` method to assign the contents of the Spotify dataset to a variable called `songs`.
songs = pd.read_csv("./data/dataset.csv", header=0)

# Use `head()` to show the first five rows of `songs`.
print(songs.head())

# This dataset includes a column called ‘duration_ms’ that has a string of each track’s length in milliseconds.

# Convert the values in the ‘duration_ms’ column from strings to integers.
print(songs["duration_ms"].dtype) 


# Convert from milliseconds to minutes, by dividing each value by 60000
def milliseconds_to_minutes(value):
    return value / 60000
songs["duration_ms"] = songs["duration_ms"].map(milliseconds_to_minutes)
# display(songs["duration_ms"])

# Use `.rename()` to change the name of the 'duration_ms' column to  'minutes_long'
songs.rename(columns={"duration_ms": "minutes_played"}, inplace=True)
print(songs)

# Use `.count()` to show how many times ‘FKA twigs’ is a value in the ‘artists’ column
songs["artists"].value_counts()["FKA twigs"]

# Use `.groupby()` to get the max ‘danceability’ rating for each track_genre.
max_danceability = songs.groupby(["danceability", "track_genre"]).track_genre.max()
print(max_danceability)

# Use `.shape` to show the number of rows and columns of `songs`
songs.shape

# Drop the "valence","tempo", and "time_signature" columns.
# Use `.shape` again to confirm that there are now three fewer columns.
songs = songs.drop(columns=["valence", "tempo", "time_signature"])
songs.shape