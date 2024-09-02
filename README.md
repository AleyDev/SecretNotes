# Secret Notes Uygulaması

**Secret Notes** uygulaması, kullanıcının özel notlarını Vigenère şifreleme yöntemiyle şifreleyip kaydeder ve gerektiğinde şifre çözme işlemi yaparak notları geri getirir.

## Özellikler

- **Not Şifreleme-Encryption:** Kullanıcıların özel notlarını Vigenère şifreleme algoritması ile güvenli bir şekilde şifreler.
- **Not Şifre Çözme:-Decryption** Kullanıcıların şifrelenmiş notlarını geri çözerek okunabilir hale getirir.

## Gereksinimler

Bu uygulamayı çalıştırmak için aşağıdaki paketlerin kurulu olması gerekmektedir:

- Python 3.x
- Tkinter (Python ile birlikte gelir)
- Pillow (Python Imaging Library) - `pip install pillow`

## Kullanım

1. **Not Girme:** `Enter your title` ve `Enter your secret` alanlarına not başlığı ve not içeriğini girin.
2. **Şifreleme:** `Enter master key` alanına bir anahtar girin ve `Save & Encrypt` butonuna tıklayın. Notunuz şifrelenip kaydedilecektir.
3. **Şifre Çözme:** Şifrelenmiş bir notu çözmek için aynı anahtarı `Enter master key` alanına girin, notu seçin ve `Decrypt` butonuna tıklayın.

## Nasıl Çalışır

1. **Şifreleme (Encode):** Girilen metin, Vigenère şifreleme algoritması ile şifrelenir. Metin, kullanıcı tarafından belirlenen bir anahtara göre harf harf şifrelenir.
2. **Şifre Çözme (Decode):** Şifrelenmiş metin, aynı anahtar kullanılarak çözülür ve orijinal metin elde edilir.

