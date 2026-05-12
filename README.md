Deskripsi Singkat

Program ini dirancang untuk mencari data nama siswa dengan menggunakan algoritma Sequential Search, yaitu metode pencarian sederhana yang menelusuri data secara berurutan dari elemen pertama hingga terakhir hingga data yang dicari ditemukan. Dalam implementasinya, daftar nama siswa disimpan dalam sebuah list. Pengguna diminta memasukkan nama target, lalu program akan membandingkan nama tersebut dengan setiap elemen dalam list secara beruntun. Apabila nama yang dicari cocok dengan salah satu data, program akan menghitung jumlah kemunculannya menggunakan variabel counter.

<img width="1326" height="1622" alt="baruu" src="https://github.com/user-attachments/assets/1dd04287-4c33-446b-ad58-bf5a6c6a4c11" />

1. def sequential_search(data, n, target): untuk melakukan pencarian data.
2. i = 0 Membuat variabel i sebagai indeks awal pencarian.
3. counter = 0 untuk menghitung jumlah data yang ditemukan.
4. while i < n: Melakukan perulangan selama indeks i masih lebih kecil dari jumlah data.
5. if data[i].lower() == target.lower(): untuk mengecek data pada indeks ke-i sama dengan data yang dicari. lower() digunakan agar huruf besar dan kecil dianggap sama.
6. counter += 1 Jika data ditemukan, maka counter ditambah 1.
7. i += 1 berpindah ke data berikutnya.
8. return counter untuk mengembalikan jumlah data yang ditemukan ke program utama.
9. def main(): fungsi utama program.
10. data = "Kia", "Calis", "Indah", "Rara", "Oliv", "Alya", "Alya", "Rara", "Bunan" untuk membuat list yang berisi data nama siswa.
11. n = len(data) untuk menghitung jumlah data dalam list menggunakan fungsi len().
12. print(f"Data siswa: {data}") untuk menampilkan seluruh data siswa ke layar.
13. target = input("Masukkan nama yang ingin dicari: ") untuk meminta pengguna memasukkan nama yang ingin dicari.
14. counter = sequential_search(data, n, target) untuk melakukan pencarian data.
15. if counter > 0: untuk mengecek apakah data ditemukan.
16. print(f"Nama {target} ditemukan sebanyak {counter} kali.") untuk menampilkan jumlah nama yang ditemukan.
17. else: Dijalankan jika data tidak ditemukan.
18. print(f"Nama {target} tidak ditemukan.") untuk menampilkan pesan bahwa data tidak ditemukan.
19. if __name__ == "__main__": untuk mengecek apakah program dijalankan langsung.
20. main() untuk menjalankan fungsi utama program.
