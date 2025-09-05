## teknik menduplikat list

a = ["ayam", "tukus", "kambing"]
print(f"Nama hewan = {a}" )

b = a
print(f"Nama hewan 2 = {b}")

a[0] = "paus"
b.sort()
print(f"ayam di ubah jadi = {a}")
print(f"{b}")


## addres dari a dan b
print(f"addres dari a = {hex(id(a))}")
print(f"addres dari b = {hex(id(b))}")

## menduplikat list dengan copy
print("menduplikat list c dengan a.copy")
c = a.copy()

print(f"addres dari a = {hex(id(a))}")
print(f"addres dari b = {hex(id(b))}")
print(f"addres dari c = {hex(id(c))}")

print(f"c = {c}")
print(f"a = {a}")
print(f"b = {b}")

print("kita ubah data 0")
c[0] = "blod"

print(f"c = {c}")
print(f"a = {a}")
print(f"b = {b}")





