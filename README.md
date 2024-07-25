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

1. For `API_KEY` go to https://rapidapi.com/ytjar/api/yt-api and then subscribe to the basic free plan which gives you 500 requests per day.<br>
2. Create a `.env` file in the root directory with the following content:
```env
API_KEY=your_api_key
```
3. Run the main script:
```bash
python main.py
```
4. You can get playlist code in url when you open a playlist it will look like the example given below
![image](https://github.com/user-attachments/assets/631f13b8-f956-40f1-9d0f-4051b2ca5135)<br>
- or you can find the code in video url link <br>
![image](https://github.com/user-attachments/assets/d48b8e94-92e1-472b-8cf4-e5b834e4f4cc)

5. Follow the prompts to input the playlist URL code and other settings.<br>
`EXAMPLE`<br>
![image](https://github.com/user-attachments/assets/b2881fe9-2c78-4ca2-b558-3ed25ab5ada1)

6. While running code on vs code run code with debug <br>
`EXAMPLE option 3`<br>
![image](https://github.com/user-attachments/assets/71c7576d-472d-4563-bc32-8d3ad73a19de)

7. `URL` link will be generated for all the videos one by one click on them `TO follow link : ctrl + click` <br>
`Example`<br>
![image](https://github.com/user-attachments/assets/de0c44ea-71fe-4675-a93d-57f456416389)

8. A video screen will be opened i am not showing complete screen shot due to some reasons
`Example`<br>
![image](https://github.com/user-attachments/assets/390fce41-28d0-4744-a7ef-ad0db90ea8c2)

9. You will see an three dots option below of opened tab
`Example`<br>
![image](https://github.com/user-attachments/assets/fe1d3ede-1579-4f21-999e-27417ed54096)

10. You will see a download button click on it and your download will be started.
`Example`<br>
![image](https://github.com/user-attachments/assets/deb06924-fba8-4225-b324-e5a0cc9c0084)

## CONCLUSION 
- Benifits of this repository is you dont have to deal with ads which you get on other websites while trying to download playlist. It is safe secure none of your data is being tracked and api is good too.
- If you like my work i would apppreciate a star and if you think you can modify add something better it will be very helpful.
- The code is very easy to understand and simple while i have tried my best to addd comments in code for easy readability

