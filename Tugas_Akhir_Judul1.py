def menu():
    print("\n=== SISTEM MENU MBG ===")
    print("1. Tampilkan semua menu")
    print("2. Tampilkan menu per hari")
    print("3. Ubah menu")
    print("4. Keluar")


def main():
    # 5 hari x 3 menu 
    menu_mbg = [
        ["Nasi Ayam", "Sayur", "Buah"],
        ["Nasi Ikan", "Sup", "Jeruk"],
        ["Nasi Telur", "Tumis", "Pisang"],
        ["Nasi Tempe", "Sayur Asem", "Apel"],
        ["Nasi Daging", "Sop", "Melon"]
    ]

    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        # 1. Tampilkan semua menu
        if choice == 1:
            print("\n=== MENU MBG MINGGUAN ===")
            for i in range(5):
                print(f"{hari[i]}: {menu_mbg[i]}")

        # 2. Tampilkan menu per hari
        elif choice == 2:
            try:
                h = int(input("Pilih hari (0=Senin ... 4=Jumat): "))
                print(f"{hari[h]}: {menu_mbg[h]}")
            except:
                print("Input tidak valid!")

        # 3. Ubah menu
        elif choice == 3:
            try:
                h = int(input("Pilih hari (0-4): "))
                for j in range(3):
                    menu_mbg[h][j] = input(f"Menu ke-{j+1}: ")
                print("Menu berhasil diubah!")
            except:
                print("Input tidak valid!")

        # 4. Keluar
        elif choice == 4:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()