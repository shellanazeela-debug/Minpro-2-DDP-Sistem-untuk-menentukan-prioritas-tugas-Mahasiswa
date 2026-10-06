Nama : Shella Nazeela Saputra <br>
Nim 2609116018 <br>

**FLOWCHART UNTUK SISTEM UNTUK MENENTUKAN PRIORITAS TUGAS MAHASISWA**<br>
**1. FLOWCHART UNTUK MENJELASKAN SISTEM HALAMAN LOGIN** <BR>
<img width="692" height="942" alt="MINNPRO2 2-LOGIN drawio" src="https://github.com/user-attachments/assets/ba6bc1eb-9e40-458e-bb21-840ee20ece11" /> <br>
Flowchart diatas digunakan untuk menjalankan sistem yang memproses halaman login. Yang dimana, dibagian ini user diminta untuk memasukkan nama panggilan, role, dan juga password. Nantinya pengguna akan diarahkan ke dua role yaitu admin dan mahasiswa berdasarkan username dan password pengguna. Didalam flowchart, dijelaskan ketika nama kosong,dan username/password salah, flowchart menggambarkan decission yang artinya pilihan arah lain. ketika hal tersebut terjadi, sistem akan memberikan pesan teguran jika nama kosonh atau username/password salah. <br>
**2. FLOWCHART UNTUK MENAMPILKAN MENU LOGIN** <BR>
<img width="1432" height="1442" alt="MINNPRO2 2-TAMPILANMENU drawio" src="https://github.com/user-attachments/assets/5e0527ab-63fa-4345-809b-571b9087fbd1" /> <br>
Menampilkan menu login yang dimana flowchart menggambarkan deccision yang mengartikan dua pilihan kemungkinan, yaitu role mahasiswa dan juga admin. Diflowchart juga tergambar bagaimana role admin dan juga mahasiswa memmiliki jumlah menu yang berbeda. Untuk admin memiliki opsi yang jauh lebih lengkap dibanding mahasiswa yang dimana telah terlihat alurnya diflowchart atas. Dan juga, didalam flowchart diatas menggunakan sistem deccision ketika pengguna menginput angka,sistem akan melakukan percabangan dari menu ke 1-5. Ketika pengguna memilih menu 5, sistem akan menyelesaikan proses yang ada. Dan jika pengguna memilih menu selain 1-5,akan masuk kebagian else yang artinya tidak ada pilihan di sistem. Sistem akan memberikan pesan "tidak valid". <br>
**3. FLOWCHART UNTUK MENAMBAH TUGAS** <BR>
<img width="652" height="1532" alt="MINNPRO2 2-MENAMBAHKAN TUGAS drawio" src="https://github.com/user-attachments/assets/10df8b38-5be7-4a83-a6ad-95401bf94a6c" /> <BR>
Menjelaskan proses menambahkan tugas baru, dimulai dari memasukkan nama tugas dan sisa hari pengerjaan, kemudian sistem memvalidasi apakah sisa hari berupa angka. Setelah itu, pengguna memasukkan skala kesulitan 1–5 yang juga divalidasi oleh sistem. Jika data sudah benar, sistem menentukan tingkat kesulitan dan prioritas tugas berdasarkan tingkat kesulitan serta sisa hari, kemudian menyimpan data tugas ke dalam list. Terakhir, sistem menampilkan pesan bahwa tugas berhasil disimpan dan proses dilanjutkan ke tahap berikutnya. <br>
**4. FLOWCHART UNTUK MELIHAT TUGAS** <BR>
<img width="1270" height="1412" alt="MINNPRO2 2-MELIHAT DAFTAR TUGAS drawio" src="https://github.com/user-attachments/assets/2b9ce063-6192-4a95-846c-66dc5cca59aa" /> <br>
Menjelaskan proses melihat daftar tugas, dimulai dengan mengecek apakah terdapat tugas di dalam list `data_tugas`. Jika tidak ada, sistem menampilkan pesan bahwa belum ada tugas dan proses selesai. Jika ada, sistem menampilkan menu pilihan untuk melihat tugas dalam bentuk list, melihat tugas dalam bentuk tabel, atau kembali ke menu utama. Pengguna kemudian memilih pilihan 1–3, jika memilih 1 maka tugas ditampilkan dalam bentuk list, jika memilih 2 ditampilkan dalam bentuk tabel, sedangkan pilihan 3 akan kembali ke menu utama. Jika pengguna memasukkan pilihan selain 1–3, sistem menampilkan pesan “Pilihan tidak valid!” dan kembali ke menu untuk memilih kembali.<br>
**5. FLOWCHART UNTUK HAPUS TUGAS** <BR>
<img width="1197" height="1402" alt="MINNPRO2 2-HAPUS TUGAS drawio" src="https://github.com/user-attachments/assets/b10841db-d999-44ce-8e83-3bcb0b56b20e" /> <BR>
Menjelaskan proses menghapus tugas, dimulai dengan mengecek apakah terdapat data tugas dalam list. Jika tidak ada, sistem menampilkan pesan “Nomor tugas tidak ada!” dan proses kembali ke menu utama. Jika ada, sistem menampilkan daftar tugas, kemudian pengguna memasukkan nomor tugas yang ingin dihapus. Sistem mengecek apakah nomor tersebut tersedia dalam index; jika tidak, muncul pesan “Belum ada tugas yang dapat diubah” dan pengguna diminta memasukkan nomor kembali. Jika nomor valid, tugas yang dipilih akan dihapus menggunakan Tugas.pop(index), kemudian sistem menampilkan pesan bahwa tugas berhasil dihapus dan pengguna menekan Enter untuk melanjutkan ke menu utama. <br>
**6. FLOWCHART UNTUK MENGUBAH TUGAS** <BR>
<img width="712" height="1462" alt="MINNPRO2 2-MENGUBAH TUGAS drawio" src="https://github.com/user-attachments/assets/cb1579a1-24e7-4c7c-be07-33508c01ddf8" /> <BR>
Menjelaskan proses mengubah data tugas, dimulai dengan mengecek apakah terdapat tugas yang dapat diubah. Jika tidak ada, sistem menampilkan pesan bahwa belum ada tugas yang dapat diubah. Jika ada, sistem menampilkan daftar tugas dan pengguna memasukkan nomor tugas yang ingin diubah. Sistem kemudian memeriksa apakah nomor tersebut valid; jika tidak, pengguna diminta memasukkan kembali nomor tugas. Jika valid, pengguna dapat memasukkan data tugas baru untuk menggantikan data lama pada index yang dipilih. Setelah data berhasil diubah, sistem menampilkan pesan “Tugas berhasil diubah!”, kemudian pengguna menekan Enter untuk kembali ke menu utama.<br>













