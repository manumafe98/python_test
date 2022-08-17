# Python project
# Docs: https://hummingbird-me.github.io/api-docs/
# Ex_API: https://kitsu.io/api/edge/anime?filter[text]=one%20piece
# Bring animes from an API
# Order them from genres in a csv 
# Order them for they average rating in a csv 
# Generate inputs to the user thats trying to get a random anime
# If the user is not satisfied with the anime in result that he can re randomize with conditions like:
#   average rating above 70 or horror genre has to be included in the anime

import random
import requests
import pandas as pd
import numpy as np

# As they are 14.267 ID of animes that the API can fetch i would make an array of them
# I will limit the search at 100 animes
ids_array = np.arange(1,101)
anime_array = ['Anime']
rating_array = ['Rating']

# Get request and format to json, making an array of only the anime titles
for id in ids_array:
    anime_array.append(requests.get(f"https://kitsu.io/api/edge/anime?filter[id]={id}").json()['data'][0]['attributes']['canonicalTitle'])
    
# Make a list of the 100 animes average_rating
for i in range(1, 101):
    rating_array.append(requests.get(f"https://kitsu.io/api/edge/anime?filter[id]={i}").json()['data'][0]['attributes']['averageRating'])

# Write the anime with the corresponding rating to a csv file
np.savetxt('/home/manuel/python/python_test/animeRating.csv', [p for p in zip(anime_array, rating_array)], delimiter=',', fmt='%s')

# Order Animes by rating in the csv
csv = pd.read_csv("/home/manuel/python/python_test/animeRating.csv")
sorted_csv = csv.sort_values(by=['Rating'], ascending=False)
sorted_csv.to_csv('sorted_animeRating.csv', index=False)

# Getting a random anime from the list
random_anime = random.choice(anime_array)
while random_anime == 'Anime':
    random_anime = random.choice(anime_array)

# Getting the average rating of the anime that was selected randomly
average_rating = requests.get(f"https://kitsu.io/api/edge/anime?filter[text]={random_anime}").json()['data'][0]['attributes']['averageRating']

# Getting the genres of the anime
anime_id = requests.get(f"https://kitsu.io/api/edge/anime?filter[text]={random_anime}").json()['data'][0]['id']
len_get_genres = len(requests.get(f"https://kitsu.io/api/edge/anime/{anime_id}/genres").json()['data'])

genre_list = []
for i in range(0, len_get_genres):
    get_genres = requests.get(f"https://kitsu.io/api/edge/anime/{anime_id}/genres").json()['data'][i]['attributes']
    for key, value in get_genres.items():
        if key == 'name':
            genre_list.append(value)
separator = ", "
s = separator.join(genre_list)

print("Your randomized anime is: " + random_anime + "," + " The rating of the show is: " + average_rating + "," + " The main genres of the anime are: " + s )