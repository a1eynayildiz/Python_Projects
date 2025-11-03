from PIL import Image

frames = [
    Image.new("RGB", (200, 200), c) #Her renk için 200x200 piksel renkli kare oluştur
    for c in ["pink", "green", "blue", "yellow", "purple"]]
frames[0].save(
    "renkler.gif",
    save_all=True, #Çoklu animasyon kaydet
    append_images=frames[1:],
    duration=400, loop=0) #Sonsuz döngüye alır ve 400 msde bir bir kare gözükür
