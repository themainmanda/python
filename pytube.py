pip install pytube
from pytube import YouTube
url = ''
video = YouTube(URL)
stream = video.stream.get_highest_resolution()

stream.download(output_path = 'D:/')