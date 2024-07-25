import requests  # Import the requests library to make HTTP requests
from playlist_downloader import get_url  # Import the get_url function from playlist_downloader.py
import os  # Import the os library to access environment variables
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file

# Load environment variables from a .env file
load_dotenv()

# URL for the playlist API endpoint
url = "https://yt-api.p.rapidapi.com/playlist"

# Prompt the user to enter a playlist ID
query = input("Enter Playlist id :")
querystring = {"id": query}

# Headers for the API request, including the API key and host from environment variables
headers = {
    "x-rapidapi-key": os.getenv('API_KEY'),
    "x-rapidapi-host": "yt-api.p.rapidapi.com"
}

# Make the API request to get playlist information
response = requests.get(url, headers=headers, params=querystring)

# Check if the API key is invalid
if response.status_code == 403:
    print("API Key is invalid")
else:
    # Parse the response JSON if the request is successful
    main = response.json()

# Print playlist metadata
print(f"Playlist Title: {main['meta']['title']}\n")
print(f"Playlist Description: {main['meta']['description']}")
print(f"Total Videos: {main['meta']['videoCountText']}")
print(f"Total Views: {main['meta']['viewCountText']}")

# Get the total number of videos in the playlist
total_video = int(main['meta']['videoCount'])

# Print video links
print("\nVideo Links:\n")

# Loop through each video in the playlist and print its title and URL
for i in range(total_video):
    v_id = main['data'][i]['videoId']
    set_url = get_url(v_id)
    print(f"\n{i+1}.{main['data'][i]['title']}\n")
    print(set_url)
