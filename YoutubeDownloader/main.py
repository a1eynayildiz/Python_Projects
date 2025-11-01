import yt_dlp

url = input("Video linkini yapıştır: ")

ayarlar = {'noplaylist': True}

yt_dlp.YoutubeDL(ayarlar).download([url])
print("Video başarıyla indirildi!")
