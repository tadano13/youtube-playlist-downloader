import requests
from playlist_downloader import get_url
import os 
from dotenv import load_dotenv

load_dotenv()

url = "https://yt-api.p.rapidapi.com/playlist"

query = input("Enter Playlist id :")
querystring = {"id":query}

headers = {
	"x-rapidapi-key": os.getenv('API_KEY'),
	"x-rapidapi-host": "yt-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
if response.status_code == 403:
    print("API Key is invalid")
else:
	main = response.json()

print(f"Video Title:{main['meta']['title']}\n")
print(f"Video Title:{main['meta']['description']}")
print(f"Total Videos:{main['meta']['videoCountText']}") 
print(f"Toral Views:{main['meta']['viewCountText']}")
total_video = int(main['meta']['videoCount'])

print("\nVideo Links :\n")

for i in range(total_video):
    v_id = main['data'][i]['videoId']
    set_url = get_url(v_id)
    print(f"\n{main['data'][i]['title']}\n")
    print(set_url)
    
    
    

    


    


