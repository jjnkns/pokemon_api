
# API's exist for all sorts of meaningless data on the internet. 
# One of these if the [Pokeapi](https://pokeapi.co/) which returns you 
# all the Pokemon-related JSON you could possibly imagine (and then some).

# Create a Python application that can take a list 
# (of strings, names of the Pokemon) and 
# return a dictionary of Pokemon: weight key-value pairs 
# for every name. Use the `requests` library and 
# the pokeapi documentation to complete this assignment.

import requests
import json
from pprint import pprint

stem = "http://pokeapi.co/api/v2/pokemon/"
poke_weights={}

for x in ['bulbasaur', 'pikachu', 'ditto', 'tentacruel']:
    response = requests.get(stem + x)
    data = response.json()
    poke_weights.update({x:data['weight']})
    pprint(data['weight'])

print(poke_weights)

# response = requests.get("http://pokeapi.co/api/v2/pokemon/bulbasaur")
# data = response.json()
# pprint(data['weight'])

# response = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu")
# data = response.json()
# pprint(data['weight'])

# response = requests.get("http://pokeapi.co/api/v2/pokemon/ditto")
# data = response.json()
# pprint(data['weight'])

# response = requests.get("http://pokeapi.co/api/v2/pokemon/tentacruel")
# data = response.json()
# pprint(data['weight'])





# 'Ash Ketchum',
# 'Wobbuffet',
# 'Tracey Sketchit',
# 'May',
# 'Max',
# 'Dawn',
# 'Iris',
# 'Cilan',
# 'Serena',	
# 'Clemont',	
# 'Bonnie',
# 'Lillie',
# 'Kiawe',
# 'Mallow',
# 'Lana',
# 'Sophocles'