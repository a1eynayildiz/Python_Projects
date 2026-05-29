# 🐍 Python Projects

Farklı Python kütüphaneleri kullanılarak geliştirilmiş **mini projeler koleksiyonudur**. Bu repository'nin amacı; küçük ama tamamlanmış uygulamalar üzerinden Python ekosistemindeki popüler kütüphaneleri tanımak, problem çözme alışkanlığı kazanmak ve farklı alanlarda pratik yapmaktır.

Her klasör/dosya bağımsız bir mini projedir. Bir projeyi çalıştırmak için diğer projelere ihtiyacınız yoktur.


---

##  Proje Listesi

### 1. EraseTheBackground
Bir görüntünün **arka planını otomatik olarak silen** uygulama. Girdi olarak verilen resmin nesnesini izole ederek arka planı şeffaf bir PNG haline getirir.

### 2. GIF_CREATE
Birden fazla görselden veya kare dizilerinden **animasyonlu GIF üreten** mini proje. Belirtilen klasördeki görüntüler okunur, sıralanır ve istenen FPS değerinde bir GIF dosyasına dönüştürülür.

###  3. PdfConverter
**PDF dönüştürme** ve PDF üzerinde işlem yapma aracı. Görsel → PDF, metin → PDF ya da PDF'leri birleştirme gibi senaryoları kapsayabilir.

### 4. Qr_Code
Verilen bir **metin veya URL** için QR kod görseli üreten basit Python aracı. QR kod, terminalden alınan girdi ile oluşturulup PNG olarak kaydedilir.

### 5. SecretSanta
Katılımcı listesi alır, herkesin kendisinden farklı birine hediye almasını sağlayacak şekilde **rastgele eşleştirme** yapar; isteğe bağlı olarak sonucu e-posta veya konsol ile bildirebilir.

### 6. YoutubeDownloader
YouTube videolarını yerel diske **indirebilen** mini araç. Video URL'si alır ve istenen kalitede MP4 veya yalnızca ses (MP3) olarak indirme imkânı sunar.

### 7. secret notes
**Gizli/şifreli not** tutma uygulaması. Notlar dosyaya kaydedilirken şifrelenir; ancak doğru parola ile okunabilir.

###  8. subdomain
Belirtilen bir hedef domain için **subdomain keşfi (enumeration)** yapan bir betik. Wordlist'teki her ismi domain'in önüne ekleyip DNS çözümlemesi veya HTTP isteği ile geçerli alt alan adlarını tespit eder.

###  9. turtle
Python'un yerleşik `turtle` modülü kullanılarak yapılmış **çizim örnekleri** ve **küçük grafik animasyonları**. Programlama mantığını öğrenmek için klasik bir başlangıç projesidir.

###  10. HackerNewsTop30Stories.py
**Hacker News** sitesinin resmi Firebase API'sini kullanarak en popüler **ilk 30 haberi** çekip terminale yazdıran script.

###  11. bmi_calculator.py
Boy ve kilo bilgisi girilerek **Vücut Kitle İndeksi (BMI)** hesaplayan, **`tkinter`** ile yapılmış basit bir **masaüstü GUI** uygulaması.


##  Kurulum

### Gereksinimler

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` paket yöneticisi
- (Tercihen) Sanal ortam: `venv` veya `virtualenv`

### Adımlar

```bash
# 1. Depoyu klonlayın
git clone https://github.com/a1eynayildiz/Python_Projects.git
cd Python_Projects

# 2. (Önerilir) Sanal ortam oluşturun
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Çalıştırmak istediğiniz projenin klasörüne girin
cd Qr_Code

# 4. Gerekli paketleri yükleyin (varsa)
pip install -r requirements.txt
# veya doğrudan
pip install qrcode[pil]

# 5. Python dosyasını çalıştırın
python main.py
```

>  Her mini proje **bağımsız** çalışır. Hangi projeyle ilgileniyorsanız sadece o klasöre girip ilgili `.py` dosyasını çalıştırmanız yeterlidir.

---

##  Genel Klasör Yapısı

```
Python_Projects/
├── EraseTheBackground/         # Arka plan kaldırma uygulaması
├── GIF_CREATE/                 # GIF üretici
├── PdfConverter/               # PDF dönüştürme aracı
├── Qr_Code/                    # QR kod oluşturucu
├── SecretSanta/                # Gizli kardeş eşleştirici
├── YoutubeDownloader/          # YouTube video indirici
├── secret notes/               # Şifreli not uygulaması
├── subdomain/                  # Subdomain enumeration
├── turtle/                     # Turtle çizim örnekleri
├── HackerNewsTop30Stories.py   # Hacker News top 30 scraper
├── bmi_calculator.py           # tkinter ile BMI hesaplayıcı
├── .gitignore
└── README.md
```

---

##  Amaç ve Öğrenme Hedefleri

Bu repository ile aşağıdaki konularda pratik yapılması hedeflenmiştir:

-  Python ekosistemindeki **popüler kütüphaneleri** tanımak
-  **Küçük ölçekli problemleri** uçtan uca çözmek
-  **GUI**, **CLI**, **web scraping**, **API tüketimi**, **kriptografi**, **görüntü işleme** gibi farklı konseptleri uygulamak
-  Kod organizasyonu, dosya/klasör yapısı ve **basit modüler tasarım** alışkanlığı kazanmak
-  **Hızlı prototipleme** ve fikirden çalışan uygulamaya geçiş sürecini deneyimlemek

---

##  Katkıda Bulunma

Yeni bir mini proje eklemek veya mevcut bir projeyi geliştirmek isterseniz:

1. Repository'yi **fork**'layın
2. Yeni bir branch oluşturun:
   ```bash
   git checkout -b feature/yeni-proje
   ```
3. Değişikliklerinizi commit'leyin:
   ```bash
   git commit -m "feat: yeni mini proje eklendi"
   ```
4. Branch'inizi push'layın:
   ```bash
   git push origin feature/yeni-proje
   ```
5. **Pull Request** açın 



- GitHub: [@a1eynayildiz](https://github.com/a1eynayildiz)
- Repository: [Python_Projects](https://github.com/a1eynayildiz/Python_Projects)

> ⭐ Projeyi beğendiyseniz GitHub'da yıldız vermeyi unutmayın!
