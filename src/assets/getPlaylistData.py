##File for retreiving spotify most popular songs from different countries and saving them in a pickle file

import requests
import time 
import pickle

playlist_ids=[
    ["Argentina", "37i9dQZEVXbMMy2roB9myp"],
    ["Australia", "37i9dQZEVXbJPcfkRz0wJ0"],
    ["Austria", "37i9dQZEVXbKNHh6NIXu36"],
    ["Belgium", "37i9dQZEVXbJNSeeHswcKB"],
    ["Bolivia", "37i9dQZEVXbJqfMFK4d691"],
    ["Brazil", "37i9dQZEVXbMXbN3EUUhlg"],
    ["Bulgaria", "37i9dQZEVXbNfM2w2mq1B8"],
    ["Canada", "37i9dQZEVXbKj23U1GF4IR"],
    ["Chile", "37i9dQZEVXbL0GavIqMTeb"],
    ["Colombia", "37i9dQZEVXbOa2lmxNORXQ"],
    ["Costa Rica", "37i9dQZEVXbMZAjGMynsQX"],
    ["Czech Republic", "37i9dQZEVXbIP3c3fqVrJY"],
    ["Denmark", "37i9dQZEVXbL3J0k32lWnN"],
    ["Dominican Republic", "37i9dQZEVXbKAbrMR8uuf7"],
    ["Ecuador", "37i9dQZEVXbJlM6nvL1nD1"],
    ["El Salvador", "37i9dQZEVXbLxoIml4MYkT"],
    ["Estonia", "37i9dQZEVXbLesry2Qw2xS"],
    ["Finland", "37i9dQZEVXbMxcczTSoGwZ"],
    ["France", "37i9dQZEVXbIPWwFssbupI"],
    ["Germany", "37i9dQZEVXbJiZcmkrIHGU"],
    ["Greece", "37i9dQZEVXbJqdarpmTJDL"],
    ["Guatemala", "37i9dQZEVXbLy5tBFyQvd4"],
    ["Honduras", "37i9dQZEVXbJp9wcIM9Eo5"],
    ["Hong Kong", "37i9dQZEVXbLwpL8TjsxOG"],
    ["Hungary", "37i9dQZEVXbNHwMxAkvmF8"],
    ["Iceland", "37i9dQZEVXbKMzVsSGQ49S"],
    ["India", "37i9dQZEVXbLZ52XmnySJg"],
    ["Indonesia", "37i9dQZEVXbObFQZ3JLcXt"],
    ["Ireland", "37i9dQZEVXbKM896FDX8L1"],
    ["Israel", "37i9dQZEVXbJ6IpvItkve3"],
    ["Italy", "37i9dQZEVXbIQnj7RRhdSX"],
    ["Japan", "37i9dQZEVXbKXQ4mDTEBXq"],
    ["Latvia", "37i9dQZEVXbJWuzDrTxbKS"],
    ["Lithuania", "37i9dQZEVXbMx56Rdq5lwc"],
    ["Luxembourg", "37i9dQZEVXbKGcyg6TFGx6"],
    ["Malaysia", "37i9dQZEVXbJlfUljuZExa"],
    ["Mexico", "37i9dQZEVXbO3qyFxbkOE1"],
    ["Netherlands", "37i9dQZEVXbKCF6dqVpDkS"],
    ["New Zealand", "37i9dQZEVXbM8SIrkERIYl"],
    ["Nicaragua", "37i9dQZEVXbISk8kxnzfCq"],
    ["Norway", "37i9dQZEVXbJvfa0Yxg7E7"],
    ["Panama", "37i9dQZEVXbKypXHVwk1f0"],
    ["Paraguay", "37i9dQZEVXbNOUPGj7tW6T"],
    ["Peru", "37i9dQZEVXbJfdy5b0KP7W"],
    ["Philippines", "37i9dQZEVXbNBz9cRCSFkY"],
    ["Poland", "37i9dQZEVXbN6itCcaL3Tt"],
    ["Portugal", "37i9dQZEVXbKyJS56d1pgi"],
    ["Romania", "37i9dQZEVXbNZbJ6TZelCq"],
    ["Singapore", "37i9dQZEVXbK4gjvS1FjPY"],
    ["Slovakia", "37i9dQZEVXbKIVTPX9a2Sb"],
    ["South Africa", "37i9dQZEVXbMH2jvi6jvjk"],
    ["Spain", "37i9dQZEVXbNFJfN1Vw8d9"],
    ["Sweden", "37i9dQZEVXbLoATJ81JYXz"],
    ["Switzerland", "37i9dQZEVXbJiyhoAPEfMK"],
    ["Taiwan", "37i9dQZEVXbMnZEatlMSiu"],
    ["Thailand", "37i9dQZEVXbMnz8KIWsvf9"],
    ["Turkey", "37i9dQZEVXbIVYVBNw9D5K"],
    ["United Kingdom", "37i9dQZEVXbLnolsZ8PSNw"],
    ["United States of America", "37i9dQZEVXbLRQDuF5jeBp"],
    ["Uruguay", "37i9dQZEVXbMJJi3wgRbAy"],
]

client_id = 'xxx'
client_secret = 'xxx'

auth_url = 'https://accounts.spotify.com/api/token'

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

auth_response = requests.post(auth_url, data=data)

access_token = auth_response.json().get('access_token')

base_url = 'https://api.spotify.com/v1/'

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

for playlist_id in playlist_ids:
    response = requests.get("https://api.spotify.com/v1/playlists/" + playlist_id[1],headers=headers)

    data = []
    tracks = response.json().get('tracks').get('items')

    for track in tracks:
        id = track.get('track').get('id')
        data.append(id)

    print(data)

    with open('src/assets/CountryData/'+playlist_id[0]+'.pkl', 'wb') as file: 
        pickle.dump(data, file) 

    time.sleep(2) ##attempt to keep spotify from blocking api for too many requests at once