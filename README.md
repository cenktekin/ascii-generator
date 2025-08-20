# Türkçe Destekli ASCII Art Generator

Bu proje, kullanıcının girdiği Türkçe metni ASCII sanatı olarak ekrana yazdıran bir konsol uygulamasıdır.

## Özellikler

- ✅ Türkçe karakter desteği (ç, ş, ı, ğ, ö, ü)
- ✅ A-Z harfleri ve 0-9 rakamları
- ✅ Maksimum 20 karakter sınırı
- ✅ Hata yönetimi (desteklenmeyen karakterler için placeholder)
- ✅ Güzel formatlanmış çıktı
- ✅ Kullanıcı dostu arayüz

## Kullanım

```bash
python3 ascii_art_generator.py
```

Program çalıştırıldıktan sonra:
1. Maksimum 20 karakterlik bir metin girin
2. ASCII sanatı otomatik olarak oluşturulacak
3. Başka metinler denemek için 'e' tuşlayın
4. Çıkmak için 'h' tuşlayın veya Ctrl+C kullanın

## Örnek Çıktılar

### "Merhaba" metni için:
```
 █   █ █████ ████  █   █  ███  ████   ███  
 ██ ██ █     █   █ █   █ █   █ █   █ █   █ 
 █ █ █ ████  ████  █████ █████ ████  █████ 
 █   █ █     █  █  █   █ █   █ █   █ █   █ 
 █   █ █████ █   █ █   █ █   █ ████  █   █ 
```

### "Türkçe" metni için:
```
█████ ▄ ▄  ████  █   █  ███  █████
  █   █   █ █   █ █   █ █     █    
  █   █████ ████  █████ █     ████ 
  █   █   █ █  █  █   █ █     █    
  █   █   █ █   █ █   █  ███  █████
```

## Teknik Detaylar

- **Dil**: Python 3
- **Karakter Boyutu**: Her karakter 5x5 piksel
- **Encoding**: UTF-8 (Türkçe karakter desteği için)
- **Hata Yönetimi**: Desteklenmeyen karakterler '?' ile değiştirilir

## Desteklenen Karakterler

### Türkçe Harfler
- ç, ş, ı, ğ, ö, ü (küçük harf)
- Büyük harfler otomatik olarak küçük harfe dönüştürülür

### İngilizce Harfler
- a-z (tüm harfler)

### Rakamlar
- 0-9 (tüm rakamlar)

### Özel Karakterler
- Boşluk, nokta, virgül, ünlem, soru işareti

## Geliştirici Notları

- ASCII karakter haritası `ASCII_MAP` sözlüğünde tanımlanmıştır
- Her karakter 5 satır yüksekliğinde ve sabit genişliktedir
- Karakterler arası otomatik boşluk eklenir
- Türkçe karakterler için özel Unicode desteği mevcuttur
