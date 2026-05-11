# Türkçe Destekli ASCII Art Generator

Bu proje, kullanıcının girdiği Türkçe metni ASCII sanatı olarak ekrana yazdıran gelişmiş bir konsol uygulamasıdır. **🎉 YENİ ÖZELLİK:** İsimden şekil oluşturma! Artık "kuş" yazıp hem KUŞ yazısını hem de kuş şeklini görebilirsiniz!

## Özellikler

### 📝 Normal ASCII Sanatı
- ✅ Türkçe karakter desteği (ç, ş, ı, ğ, ö, ü)
- ✅ A-Z harfleri ve 0-9 rakamları
- ✅ Maksimum 20 karakter sınırı
- ✅ 7 farklı renk teması
- ✅ Hata yönetimi (desteklenmeyen karakterler için placeholder)

### 🎭 İsim + Şekil ASCII Sanatı (YENİ!)
- ✅ İsimden otomatik şekil oluşturma ("kuş" → KUŞ yazısı + kuş şekli)
- ✅ 15+ farklı şekil desteği (hayvanlar, doğa, objeler)
- ✅ Türkçe ve İngilizce isim desteği
- ✅ Renkli şekil çıktıları
- ✅ Kategori bazlı isim listesi

### 🎨 Genel Özellikler
- ✅ İki farklı mod: Normal ASCII ve İsim+Şekil
- ✅ Güzel formatlanmış çıktı
- ✅ Kullanıcı dostu menü sistemi

## Kullanım

```bash
python3 ascii_art_generator.py
```

Program çalıştırıldıktan sonra:
1. **Ana menüden mod seçin:**
   - `1`: Normal ASCII Sanatı (metin → ASCII)
   - `2`: İsim + Şekil ASCII Sanatı (isim → ASCII + şekil)
   - `3`: Çıkış

2. **Normal ASCII Modu:**
   - Renk teması seçin (1-7)
   - Maksimum 20 karakterlik metin girin
   - ASCII sanatı oluşturulacak

3. **İsim + Şekil Modu:**
   - Desteklenen isimler listesini görün
   - Renk teması seçin (1-7)
   - Bir isim girin (örn: kuş, kedi, çiçek)
   - Hem isim hem de şekil ASCII sanatı oluşturulacak

4. Her modda başka örnekler denemek için 'e', çıkmak için 'h' tuşlayın

## 📸 Ekran Görüntüleri

### Ana Menü
Program başladığında karşınıza çıkan ana menü:

![Ana Menü](Ekran%20Görüntüsü_20250820_094637.png)

### Renk Seçenekleri
7 farklı renk teması arasından seçim yapabilirsiniz:

![Renk Seçenekleri](Ekran%20Görüntüsü_20250820_095020.png)

### Normal ASCII Sanatı Örneği
Klasik metin → ASCII dönüşümü:

![Normal ASCII](Ekran%20Görüntüsü_20250820_094655.png)

### İsim + Şekil ASCII Sanatı Örneği
Yeni özellik: İsimden hem yazı hem şekil oluşturma:

![İsim + Şekil ASCII](Ekran%20Görüntüsü_20250820_094917.png)


## Teknik Detaylar

- **Dil**: Python 3
- **Karakter Boyutu**: Her karakter 5x5 piksel
- **Encoding**: UTF-8 (Türkçe karakter desteği için)
- **Hata Yönetimi**: Desteklenmeyen karakterler '?' ile değiştirilir
- **Yeni Özellik**: İsim-şekil eşleştirme sistemi

## Desteklenen Karakterler

### Normal ASCII Modu
- **Türkçe Harfler:** ç, ş, ı, ğ, ö, ü (küçük harf)
- **İngilizce Harfler:** a-z (tüm harfler)
- **Rakamlar:** 0-9 (tüm rakamlar)
- **Özel Karakterler:** Boşluk, nokta, virgül, ünlem, soru işareti
- Büyük harfler otomatik olarak küçük harfe dönüştürülür

## Desteklenen İsimler (İsim + Şekil Modu)

### 🐾 Hayvanlar
- kuş, kus, bird
- kedi, cat
- köpek, kopek, dog
- balık, balik, fish
- kelebek, butterfly

### 🌿 Doğa
- çiçek, cicek, flower
- ağaç, agac, tree
- güneş, gunes, sun
- ay, moon
- yıldız, yildiz, star

### 🏠 Objeler
- kalp, heart
- ev, house
- araba, car

### 💝 Duygular/Kavramlar
- sevgi, love, aşk, ask → kalp şekli
- mutluluk, happiness → güneş şekli
- güzel, guzel, beautiful → çiçek şekli

## Renk Temaları

1. 🌈 **Gökkuşağı** - Çok renkli
2. 🔥 **Ateş** - Kırmızı, turuncu, sarı tonları
3. 🌊 **Okyanus** - Mavi, cyan tonları
4. 🌸 **Pembe Dünya** - Pembe, mor tonları
5. 🌿 **Doğa** - Yeşil tonları
6. ⭐ **Altın** - Altın, sarı tonları
7. 🎭 **Rastgele** - Karışık renkler

## Geliştirici Notları

### Normal ASCII Modu
- ASCII karakter haritası `ASCII_MAP` sözlüğünde tanımlanmıştır
- Her karakter 5 satır yüksekliğinde ve sabit genişliktedir
- Karakterler arası otomatik boşluk eklenir
- Türkçe karakterler için özel Unicode desteği mevcuttur

### İsim + Şekil Modu
- `ASCII_SHAPES` sözlüğünde şekil şablonları tanımlanmıştır
- `NAME_TO_SHAPE` sözlüğünde isim-şekil eşleştirmeleri yapılır
- Hem Türkçe hem İngilizce isim desteği
- Şekiller de renklendirme desteğine sahiptir
- Desteklenmeyen isimler için uyarı mesajı gösterilir
