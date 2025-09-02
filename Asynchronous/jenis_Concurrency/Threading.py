import threading
import time

def tugas(nama):
    print(f"Mulasi {tugas}")
    time.sleep()
    print(f"Selesai {tugas}")

t1 = threading.Thread(targer=tugas, args=("Download"))
t2 = threading.Thread(target=tugas, args=("Upload"))

t1.start()
t2.start()
t1.join()
t2.join()

print("Semua tugas selesai...")