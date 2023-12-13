
# Download spotify playlist into local storage

## Requirements
- Python 3
- pip
- Edge WebDriver

### Guide to install Edge WebDriver
1. Open Microsoft Edge and go to edge://settings/help to note your version of Microsoft Edge.
2. Visit the Microsoft Edge WebDriver page.
3. In the ‘Get the latest version’ section of the page, select a platform in the channel that matches your version number of Microsoft Edge.
4. After the download completes, extract the msedgedriver executable to your preferred location.
5. Add the path of edge WebDriver to system Variables.

## Dependencies
- requests
- selenium
- pytube
- moviepy
NOTE: These will autometically get installed while running the script.
## Usage

1. Open your command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

```bash
git clone https://github.com/cvishal-19/scrap-spotify-songs.git
```

4. Navigate to the cloned repository:

```bash
cd scrap-spotify-songs
```
5. Run the script:
```bash
python scrap.py
```
6. When prompted, enter the URL of the Spotify playlist you want to download.
7. When prompted, enter the path to the folder where you want to save the songs.
## Disclaimer

This script is for personal use only. Downloading copyrighted content may be illegal in your country. Use at your own risk.

Optional: Please replace the `api_key` in the script with your own YouTube Data API key.
