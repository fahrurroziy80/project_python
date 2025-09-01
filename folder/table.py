from tabulate import tabulate

data = [
    ["roro", 16, "X TKJ 1"],
    ["rara", 17, "X TKJ 2"],
    ["riri", 16, "X TKJ 1"],

]

print(tabulate(
    data,
    headers=["Nama"
             , "Umur",
             "Kelas"],
            tablefmt="grid"
))