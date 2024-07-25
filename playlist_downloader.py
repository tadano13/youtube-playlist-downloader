import requests  # Import the requests library to make HTTP requests
import os  # Import the os library to access environment variables
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file

# Load environment variables from a .env file
load_dotenv()

def get_url(video_ids):
    """
    Retrieve the download URL for a given video ID.

    Args:
        video_ids (str): The ID of the video to retrieve the URL for.

    Returns:
        str: The download URL for the video.
    """
    try:
        id = video_ids
        url = "https://yt-api.p.rapidapi.com/dl"  # URL for the video download API endpoint
        querystring = {"id": id}

        # Headers for the API request, including the API key and host from environment variables
        headers = {
            "x-rapidapi-key": os.getenv('API_KEY'),
            "x-rapidapi-host": "yt-api.p.rapidapi.com"
        }

        # Make the API request to get the video download URL
        response = requests.get(url, headers=headers, params=querystring)
        results = response.json()

        # Extract the download URL from the response
        main_url = results['adaptiveFormats'][0]['url']
        return main_url
    except Exception as e:
        # Handle exceptions and print appropriate error messages
        if response.status_code == 403:
            print("Video ID not valid")
        else:
            print(f"An error occurred: {e}")
