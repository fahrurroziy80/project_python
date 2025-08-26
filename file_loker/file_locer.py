from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str):
    # Password -> key
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def lock_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(filename + ".locked", "wb") as file:
        file.write(encrypted_data)

    print(f"🔒 File '{filename}' berhasil dikunci jadi '{filename}.locked'")

def unlock_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = cipher.decrypt(encrypted_data)

        output_file = filename.replace(".locked", "")
        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print(f"🔓 File berhasil dibuka! Hasil disimpan di '{output_file}'")
    except:
        print("❌ Password salah atau file rusak!")

# Main menu
print("=== File Locker ===")
choice = input("1. Lock File\n2. Unlock File\nPilih: ")

if choice == "1":
    file = input("Masukkan nama file: ")
    pw = input("Masukkan password: ")
    lock_file(file, pw)

elif choice == "2":
    file = input("Masukkan nama file .locked: ")
    pw = input("Masukkan password: ")
    unlock_file(file, pw)

else:
    print("❌ Pilihan tidak valid!")
