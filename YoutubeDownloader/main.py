import pytube
url = input("Enter video url: ")

pytube.YouTube(url).streams
