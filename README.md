Instructions:
Setup Git
As always, create a repository on GitHub for this project.
Include an informative README, a .gitignore file, a requirements.txt file and at least 8 commits.
Get the Data
Create a `data/` directory in your repo.

From kaggle.com, download the ‘Spotify Tracks’ dataset CSV, and put it in your data directory: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset/data

If for any reason that fails, you can get the dataset file by cloning the repo at https://github.com/alma-frankenstein/spotify_dataset

In your `.gitignore`, have Git ignore the data file (don’t push it to GitHub).

Include the link to the Kaggle dataset in your README, so users can download it themselves.

Write the following in a file called main.py or a notebook called main.ipynb:

Use the pandas `.read_csv()` method to assign the contents of the Spotify dataset to a variable called `songs`.

Use `head()` to show the first five rows of `songs`.


This dataset includes a column called ‘duration_ms’ that has a string of each track’s length in milliseconds.
Convert the values in the ‘duration_ms’ column from strings to integers.
Convert from milliseconds to minutes, by dividing each value by 60000.
Use `.rename()` to change the name of the 'duration_ms' column to  'minutes_long'.


Use `.count()` to show how many times ‘FKA twigs’ is a value in the ‘artists’ column.


Use `.groupby()` to get the max ‘danceability’ rating for each track_genre.
Notice that ‘danceability’ and ‘track_genre’ are both columns in the dataset.


Use `.shape` to show the number of rows and columns of `songs`
Drop the "valence","tempo", and "time_signature" columns.
Use `.shape` again to confirm that there are now three fewer columns.

