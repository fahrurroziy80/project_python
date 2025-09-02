from multiprocessing import Process
import os

def hitung(n):
    print(f"Proses {n} dijalankan di PID {os.getpid()}")


if __name__ == "__main__":
    p1 = Process(target=hitung, args=(1,))
    p2 = Process(target=hitung, args=(2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("selesai semua proses")

