import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def get_url(video_ids):
    try:
        id = video_ids
        url = "https://yt-api.p.rapidapi.com/dl"
        querystring = {"id": id}
        headers = {
                "x-rapidapi-key": os.getenv('API_KEY'),
                "x-rapidapi-host": "yt-api.p.rapidapi.com"
            }
        response = requests.get(url, headers=headers, params=querystring)
        results = response.json()
        main_url = results['adaptiveFormats'][0]['url']
        return main_url
    except Exception as e:
        if response.status_code == 403:
            print("Video ID not valid")
        else:
            print(f"An error occurred: {e}")

