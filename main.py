import pandas as pd

print("hello world")

songs = pd.read_csv("./data/dataset.csv", header=0)

print(songs.head())