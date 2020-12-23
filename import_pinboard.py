# Get all pinboard bookmarks

# Install requests: pip install requests
import requests

token = input('Enter your pinboard token(username:xxxx): ')

posts = requests.get('https://api.pinboard.in/v1/posts/all?auth_token=' + token + '&format=json')

for post in posts.json():
    print(post)
    print()
