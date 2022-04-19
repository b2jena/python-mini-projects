# YouTube Video Downloader
# install pytube - sudo pip install pytube
# Just give the YouTube link in the input and da da....
from pytube import YouTube

link = input("Enter the YouTube link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
