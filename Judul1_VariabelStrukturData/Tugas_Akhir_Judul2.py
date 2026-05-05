def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    tinggi_badan = []

    print("Masukkan tinggi badan siswa (cm):")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Siswa ke-{i+1}: "))
                tinggi_badan.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, masukkan angka!")

    print(f"\nTinggi badan sebelum diurutkan: {tinggi_badan}")

    bubble_sort(tinggi_badan, n)

    print("Tinggi badan setelah diurutkan (terpendek → tertinggi): ", end="")
    for i in range(n):
        print(tinggi_badan[i], end=" ")
    print()

    print(f"\nTinggi badan terpendek: {tinggi_badan[0]} cm")
    print(f"Tinggi badan tertinggi: {tinggi_badan[-1]} cm")


if __name__ == "__main__":
    main()