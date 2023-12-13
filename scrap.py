import pip
import warnings
warnings.filterwarnings("ignore")
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
        
        
requirements = ['requests', 'selenium', 'pytube', 'moviepy']

for i in requirements:
    install(i)        

import requests
import json
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# url = 'https://open.spotify.com/playlist/3IM0rmcNYIU8WpKtIVJt6G'
url = input("enter the url of spotify playlist:     ")
url = str(url)
ls = []
driver = webdriver.Edge()
driver.get(url)
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#onetrust-close-btn-container > button[aria-label='Close']"))).click()
body = driver.find_element(By.TAG_NAME, 'body')

prev_len = 0
while True:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(30)
    ls = [my_elem.text for my_elem in WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,  "div[data-testid=tracklist-row] div[dir=auto][data-encore-id=type]")))]
                                                   
    if len(ls) == prev_len:
        break
    prev_len = len(ls)

driver.quit()



def search_videos_by_keyword(api_key, keyword):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'maxResults': 20,
        'q': keyword,
        'type': 'video',
        'key': api_key
    }
    response = requests.get(url, params=params)
    return json.loads(response.text)

api_key = "AIzaSyDEDDCNfVyjCNQFY3L6wgvJBnlInG3Hkv4"
# keyword = "Barse More Naina"


path = input("enter the path to folder where u want to save the songs:     ")

path = path.replace("\\\\", "/")


# print(path)

for song_name in ls:
    result = search_videos_by_keyword(api_key, song_name)    
    data_dict =  dict(result.items())
    video_id = data_dict['items'][0]['id']['videoId']
    url = "https://www.youtube.com/watch?v=" + str(video_id)
    yt =YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    outfile = audio_stream.download(output_path=path)
    base, ext = os.path.splitext(outfile)
    new_file = base + '.mp3'
    os.rename(outfile,new_file)
    
    