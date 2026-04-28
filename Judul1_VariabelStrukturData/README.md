Deskripsi Singkat

  Program ini adalah Sistem Menu MBG yang sederhana dengan menggunakan Python, di mana berfungsi untuk menunjukkan, melihat, dan mengubah daftar hidangan selama 5 hari, dari Senin hingga Jumat. Setiap harinya terdapat 3 pilihan menu, contohnya nasi, lauk/sayur, dan buah.

  Data disimpan dalam struktur list dua dimensi. List menu_mbg menyimpan informasi menu dalam format baris dan kolom, yaitu 5 hari dengan 3 menu. Program ini juga menerapkan kontrol seperti perulangan while, percabangan if-elif-else, serta penanganan kesalahan menggunakan try-except untuk mengatasi input yang tidak valid.

Source Code
<img width="1356" height="2724" alt="code" src="https://github.com/user-attachments/assets/79540245-435a-44a1-8d6d-b2ff39c4dc3e" />

1. 'def menu():' mendefinisikan fungsi yang menampilkan pilihan dari menu utama.
2. Beberapa perintah 'print()' digunakan untuk menunjukkan opsi: tampilkan semua menu, tampilkan per hari, ubah menu, dan keluar dari program.
3. 'def main():' merupakan fungsi inti tempat program dioperasikan.
4. 'menu_mbg' adalah list dua dimensi yang menyimpan menu selama 5 hari, dengan 3 menu masing-masing dalam sehari.
5. 'hari' adalah list yang menyimpan nama hari dari Senin hingga Jumat.
6. 'running = True' berfungsi sebagai penanda untuk menjaga agar program tetap berjalan.
7. 'while running:' memastikan program terus berulang hingga pengguna memilih untuk keluar.
8. 'menu()' memanggil fungsi yang menampilkan menu utama.
9. 'choice = int(input("Pilihan: "))' meminta pengguna untuk memberikan input terkait pilihan.
10. 'try-except' diterapkan agar program tidak mengalami kesalahan ketika pengguna memasukkan input yang bukan angka.
11. Jika 'choice == 1', program akan menampilkan semua menu mingguan dengan menggunakan perulangan 'for'.
12. Jika 'choice == 2', pengguna diminta untuk memilih indeks hari dari 0 hingga 4, kemudian program akan menampilkan menu untuk hari tersebut.
13. Jika 'choice == 3', pengguna memilih hari, kemudian mengganti 3 menu pada hari itu menggunakan perulangan 'for'.
14. Jika 'choice == 4', nilai 'running' diatur menjadi 'False', artinya program akan berhenti.
15. Jika pilihan yang diberikan tidak sesuai, program akan menunjukkan pesan “Pilihan tidak valid! ”.
16. Bagian 'if __name__ == "__main__": main()' memastikan bahwa fungsi 'main()' aktif ketika file Python dijalankan secara langsung.
