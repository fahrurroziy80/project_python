# print("-"*20)
# print("list angka")
# print("-"*20)
# list_angka = [1,2,1,1,1,1,1,4,4,5,6,3,7,7,7,5,5,6,6,7,8,9,]
#
# print(f"list angka = {list_angka}")
#
# jumlah_angka_4 = list_angka.count(4)
# jumlah_angka_1 = list_angka.count(1)
#
# print(f"jumlah angka 4 = {jumlah_angka_4}")
# print(f"jumlah angka 1 = {jumlah_angka_1}")
#
# print("-"*20)
# print("urutakan list ")
# print("-"*20)
# print(f"list angak sebelum di sort = \n {list_angka}")
# list_angka.sort()
# print(f"list angka sesudah di sort = \n {list_angka}")
#
#
# print("-"*20)
# print("ambil posisi karakter ")
# print("-"*20)
# list_index = ["jamal","gloo","ter","fak"]
# print(f"list indek = {list_index}")
#
# list_ter = list_index.index("ter")
# list_gloo = list_index.index("gloo")
# list_fak = list_index.index("fak")
#
# print(f"ter berada di urutan ke = {list_ter}")
# print(f"gloo berada di urutan ke = {list_gloo}")
# print(f"fak berada di urutan ke = {list_fak}")
#
from tokenize import endpats

print("="*10)
print("="*10)

angka = [2, 3, 4, 2, 6, 2, 8, 9, 2, 5, 3, 2]

print(f"angka = {angka}")

angka_2 = angka.count(2)
angka_3 = angka.count(3)

print(f"angka 2 muncul = {angka_2}")
print(f"angka 3 muncul = {angka_3}")

print("="*10)
print("urutkan data")
print("="*10)

nilai = [70, 85, 60, 90, 75, 60, 100, 85]

print(f"nilai sebelum di urutkan =\n {nilai}")

nilai.sort()
print(f"niali sesudah di urutkan = \n {nilai}")

print("="*10)
print("cari posisi elmen")
print("="*10)
buah = ["apel", "jeruk", "mangga", "pisang", "apel", "anggur"]
print(f"list nama buah =\n{buah}")

posisi_apel = buah.index("apel")
posisi_mangga = buah.index("mangga")

print(f"posisi apel = {posisi_apel}")
print(f"posisi mangga = {posisi_mangga}")

if "durian" in buah:
    print("Posisi durian = ", buah.index("durian"))
else:
    print("durian tidak ada dalam daftar buah ")


# untuk memeberikan karakter/spasi
print("belajar", "python", end="!!!")












































