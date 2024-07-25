# YouTube Playlist Downloader

A Python tool to download YouTube playlists.

## Features

- Download entire YouTube playlists.
- Save videos in specified formats.
- Customizable download settings.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tadano13/youtube-playlist-downloader.git
   ```
2. Navigate to the project directory:
   ```bash
   cd youtube-playlist-downloader
   ```
## Required Libraries

1. Install `requests` library:<br>
```sh
pip install requests
```
2. Install `python-dotenv` library:<br>
```sh
pip install python-dotenv
```

## Usage

1. Create a `.env` file in the root directory with the following content:
   ```env
   API_KEY=your_api_key
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Follow the prompts to input the playlist URL code and other settings.<br>
   `EXAMPLE`<br>
   ![image](https://github.com/user-attachments/assets/b2881fe9-2c78-4ca2-b558-3ed25ab5ada1)

4. For `API_KEY` go to https://rapidapi.com/ytjar/api/yt-api and then subscribe to the basic free plan which gives you 500 requests per day.<br>

