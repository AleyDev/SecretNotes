import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox, END
import base64

# Ekranı, başlığı ve ölçüleri tanımlıyorum
root = tk.Tk()
root.title("TUA Secret Notes")
root.geometry("300x550")
root.config(padx=30, pady=30)

# Vigenère şifreleme algoritmasını kullanarak bir mesajı şifreliyorum
def encode(key, clear_message):
    encrypted_message = []  # Şifreli mesajı saklamak için boş bir liste oluşturuyorum
    for i in range(len(clear_message)):
        key_char = key[i % len(key)]  # Anahtardaki karakteri alıyorum
        encoded_char = chr((ord(clear_message[i]) + ord(key_char)) % 256)  # Karakterleri şifreliyorum
        encrypted_message.append(encoded_char)  # Şifrelenmiş karakteri listeye ekliyorum
    return base64.urlsafe_b64encode("".join(encrypted_message).encode()).decode()  # Sonucu base64 ile kodlayarak geri döndürüyorum

# Vigenère şifreleme algoritmasını kullanarak şifrelenmiş bir mesajı çözüyorum - Decryption
def decode(key, encoded_message):
    decrypted_message = []  # Çözülmüş mesajı saklamak için boş bir liste oluşturuyorum
    encoded_message = base64.urlsafe_b64decode(encoded_message).decode()  # Base64 ile kodlanmış mesajı çözüyorum
    for i in range(len(encoded_message)):
        key_char = key[i % len(key)]  # Anahtardaki karakteri alıyorum
        decoded_char = chr((256 + ord(encoded_message[i]) - ord(key_char)) % 256)  # Karakterleri çözüyorum
        decrypted_message.append(decoded_char)  # Çözülmüş karakteri listeye ekliyorum
    return "".join(decrypted_message)  # Sonucu geri döndürüyorum

# Notları kaydedip şifreliyorum
def save_and_encrypt_notes():
    note_title = title_entry.get()  # Kullanıcının girdiği başlığı alıyorum
    note_message = input_text.get("1.0", END)  # Kullanıcının girdiği mesajı alıyorum
    key = master_secret.get()  # Kullanıcının girdiği anahtarı alıyorum

    if len(note_title) == 0 or len(note_message) == 0 or len(key) == 0:  # Kullanıcı herhangi bir alanı boş bıraktıysa
        messagebox.showinfo(title="Error!", message="Please enter all info.")  # Hata mesajı gösteriyorum
    else:
        encrypted_message = encode(key, note_message)  # Mesajı şifreliyorum

        try:
            with open("mysecret.txt", "a") as data_file:  # Dosyaya yazmak için açıyorum
                data_file.write(f'\n{note_title}\n{encrypted_message}')  # Başlık ve şifreli mesajı dosyaya yazıyorum
        except FileNotFoundError:  # Dosya bulunamazsa
            with open("mysecret.txt", "w") as data_file:  # Yeni bir dosya oluşturuyorum
                data_file.write(f'\n{note_title}\n{encrypted_message}')  # Başlık ve şifreli mesajı dosyaya yazıyorum
        finally:
            title_entry.delete(0, END)  # Giriş alanını temizliyorum
            master_secret.delete(0, END)  # Anahtar giriş alanını temizliyorum
            input_text.delete("1.0", END)  # Mesaj alanını temizliyorum

# Notları şifresini çözüyorum
def decrypt_notes():
    encrypted_message = input_text.get("1.0", END)  # Şifrelenmiş mesajı alıyorum
    key = master_secret.get()  # Kullanıcının girdiği anahtarı alıyorum

    if len(encrypted_message) == 0 or len(key) == 0:  # Kullanıcı herhangi bir alanı boş bıraktıysa
        messagebox.showinfo(title="Error!", message="Please enter all info.")  # Hata mesajı gösteriyorum
    else:
        try:
            decrypted_message = decode(key, encrypted_message)  # Mesajın şifresini çözüyorum
            input_text.delete("1.0", END)  # Mevcut mesajı temizliyorum
            input_text.insert("1.0", decrypted_message)  # Çözülmüş mesajı ekrana yazıyorum
        except:
            messagebox.showinfo(title="Error!", message="Please enter all info.")  # Hata mesajı gösteriyorum
      
      
# UI
# Resmi açıyorum ve bir PhotoImage nesnesine dönüştürüyorum
image = Image.open("top-secret.png")
resized_image = image.resize((50,50))
photo = ImageTk.PhotoImage(resized_image)

# Resmi bir etiket içinde gösteriyorum
photo_label = tk.Label(root, image=photo)
photo_label.pack()

# Başlık alanı için
tk.Label(root, text="Enter your title").pack(pady=5)
title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

# Not alanı için
tk.Label(root, text="Enter your secret").pack(pady=5)
input_text = tk.Text(root, width=30, height=10)
input_text.pack(pady=5)

# Master key alanı için
tk.Label(root, text="Enter master key").pack(pady=5)
master_secret = tk.Entry(root, width=40)
master_secret.pack(pady=5)

# Kaydetme butonu için
save_button = tk.Button(root, text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_notes)
decrypt_button.pack(pady=10)

# Tkinter döngüsünü başlatıyorum
root.mainloop()
