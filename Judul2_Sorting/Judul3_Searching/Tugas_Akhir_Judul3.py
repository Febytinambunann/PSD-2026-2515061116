# Program Pencarian Nama Siswa Menggunakan Sequential Search
def sequential_search(data, n, target):
    i = 0
    counter = 0

    while i < n:
        if data[i].lower() == target.lower():
            counter += 1
        i += 1

    return counter

def main():
    data = [
        "Kia", "Calis", "Indah",
        "Rara", "Oliv", "Alya",
        "Alya", "Rara", "Bunan"
    ]

    n = len(data)

    print(f"Data siswa: {data}")

    target = input("Masukkan nama yang ingin dicari: ")

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Nama {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Nama {target} tidak ditemukan.")


if __name__ == "__main__":
    main()