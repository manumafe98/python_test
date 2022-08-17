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
import numpy as np

# As they are 14.267 ID of animes that the API can fetch i would make an array of them
# I will limit the search at 100 animes
ids_array = np.arange(1,100)
anime_array = []

# Get request and format to json, making an array of only the anime titles
for id in ids_array:
    anime_array.append(requests.get(f"https://kitsu.io/api/edge/anime?filter[id]={id}").json()['data'][0]['attributes']['canonicalTitle'])

# Getting a random anime from the array
random_anime = random.choice(anime_array)

# Getting the average ratin of the anime that was selected randomly
average_rating = requests.get(f"https://kitsu.io/api/edge/anime?filter[text]={random_anime}").json()['data'][0]['attributes']['averageRating']

print("Your randomized anime is:" + " " + random_anime + "," + " " +  "The rating of the show is:" + " " + average_rating)

# Get the genres of the anime
