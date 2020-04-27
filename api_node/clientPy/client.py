import requests

albums = requests.get("http://localhost:3000/albums")
print(albums.text)

members = requests.get("http://localhost:3000/members")
print(members.text)

tours = requests.get("http://localhost:3000/tours")
print(tours.text)

labels = requests.get("http://localhost:3000/labels")
print(labels.text)
