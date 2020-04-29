import pandas as pd
import os


data = pd.read_csv('data.csv')

genres_raw = data['genres']
genres = []
for line in genres_raw:
    genres_in_line = line.split('|')
    for genre in genres_in_line:
        if genre not in genres:        
            genres.append(genre)
            
genre_films = {}

for genre in genres:    
    films_number = data[data.genres.str.contains(genre, na=False)].original_title.count()
    genre_films[genre] = films_number
    
print(max(genre_films.items(), key=operator.itemgetter(1))[0])