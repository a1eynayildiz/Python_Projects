from rembg import remove

input_path = "sincap.jpg"
output_path= "output.png"

#rb = read binary yani 0lar 1lerle okuyor
#wb = write binary
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_file = i.read()
        output_file = remove(input_file) #asıl silme işlemini yapan kısım
        o.write(output_file)
