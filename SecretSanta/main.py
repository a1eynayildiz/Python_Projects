import tkinter as tk #GUI
import random #isimleri shuffle ile karıştırarak verme

result = {}
# Çekiliş Fonksiyonu
def do_draw():
    names = [list_names.get(i) for i in range(list_names.size())]

    if len(names) < 2:
        return

    matches = names.copy() #names listesini kopyalayarak matchese atadık
    random.shuffle(matches)

    # Kimse kendine çıkmasın
    while any(names[i] == matches[i] for i in range(len(names))):
        random.shuffle(matches)

    # Sözlük şeklinde eşleşme oluştur
    result.clear()
    for i in range(len(names)):
        result[names[i]] = matches[i]


def show_result():
    name = entry_show.get()
    if name in result:
        label_answer.config(text=f"Sana çıkan kişi: {result[name]}")
    else:
        label_answer.config(text="Bu isim listede yok!")


def add_name():
    name = entry_name.get().strip()
    if name:
        list_names.insert(tk.END, name)
        entry_name.delete(0, tk.END)


# GUI
window = tk.Tk()
window.title("Secret Santa Yılbaşı Çekilişi")
window.geometry("400x500")
window.config(bg="#1f4d2e")



# Başlık
tk.Label(window, text=" YILBAŞI ÇEKİLİŞİ ", font=("Arial", 20, "bold"), bg="dark red", fg="white").pack(pady=10)

# İsim ekleme
frame_add = tk.Frame(window, bg="#1f4d2e")
frame_add.pack()

entry_name = tk.Entry(frame_add, width=20, font=("Arial", 12))
entry_name.grid(row=0, column=0, padx=5)

btn_add = tk.Button(frame_add, text="Ekle", command=add_name, bg="#d93b3b", fg="white")
btn_add.grid(row=0, column=1)

# Liste
tk.Label(window, text="Katılımcılar:", font=("Arial", 12, "bold"), bg="#1f4d2e", fg="white").pack(pady=5)
list_names = tk.Listbox(window, width=30, height=8, font=("Arial", 12))
list_names.pack()

# Çekiliş butonu
btn_draw = tk.Button(window, text="Çekilişi Yap", command=do_draw, bg="#d93b3b", fg="white", font=("Arial", 12, "bold"))
btn_draw.pack(pady=10)

# Kişisel sonuç gösterme alanı
tk.Label(window, text="İsmini Yaz:", font=("Arial", 12, "bold"), bg="#1f4d2e", fg="white").pack()
entry_show = tk.Entry(window, width=20, font=("Arial", 12))
entry_show.pack(pady=5)

btn_show = tk.Button(window, text="Sonucumu Göster", command=show_result, bg="#d93b3b", fg="white")
btn_show.pack()

label_answer = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#1f4d2e", fg="yellow")
label_answer.pack(pady=10)

window.mainloop()

#tk.end = listenin sonuna ekleme
#shuffle(): karıştırma yapıyor
#Label: Pencereye yazı eklememizi sağlar
#pack(): bunu yerleştir demek (üst üste dizer)
#Entry() : metin giriş kutusu oluşturur
#listbox(): Pencere içinde liste göstermek için kullanılır
#mainloop(): Programı çalıştırır.