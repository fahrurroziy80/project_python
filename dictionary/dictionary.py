# tamplat dict mahasiswa
import datetime

mahasiswa_tamplat = {
    'nama': 'nama',
    'NIM': '00000000',
    'SKS': 0,
    'lahir': datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

print(f"{'selamat datang':^20}")
print(f"{'data mahasiswa':^20}")
print("-"*10)

mahasiswa = dict.fromkeys(mahasiswa_tamplat.keys())
print(mahasiswa)
mahasiswa['nama'] = input("masukan nama : ")
mahasiswa['NIM'] = input("masukan NIM : ")
mahasiswa['SKS'] = int(input("masukan SKS : "))
TAHUN_LAHIR = int(input("Tahun lahir"))
print(mahasiswa)
