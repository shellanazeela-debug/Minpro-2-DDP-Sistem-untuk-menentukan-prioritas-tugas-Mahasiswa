 /># Minpro-2-DDP-Sistem-untuk-menentukan-prioritas-tugas-Mahasiswa <BR>
Nama : Shella Nazeela Saputra <br>
Nim : 2609116018 <br>


 =========== **LAPORAN MENGENAI MINI PROJECT : SISTEM UNTUK MENENTUKAN PRIORITAS TUGAS MAHASISWA** ===========<br>
Sistem Prioritas Tugas Mahasiswa merupakan program berbasis Python yang digunakan untuk membantu mahasiswa mencatat dan mengatur prioritas tugas berdasarkan sisa waktu pengerjaan dan tingkat kesulitan tugas. Program ini memiliki fitur login dengan dua role, yaitu Admin dan Mahasiswa, yang memiliki hak akses berbeda. Pengguna dapat menambahkan tugas dengan memasukkan nama tugas, sisa hari pengerjaan, dan skala kesulitan dari 1 sampai 5. Berdasarkan data tersebut, program akan menentukan tingkat kesulitan dan prioritas tugas secara otomatis. Program juga menyediakan fitur untuk melihat tugas dalam bentuk list maupun tabel, mengubah tugas, dan menghapus tugas.<br>



**PENJELASAN PROGRAM & OUTPUT SERTA DOKUMENTASI**
*A. MEMBUAT FUNGSI LOGIN* <BR>
1. IMPORT LIBRARY<BR>
<img width="272" height="54" alt="Screenshot 2026-10-06 000030" src="https://github.com/user-attachments/assets/02e000ff-a572-4d48-8f74-6349f95e8fdd" /> <BR>
Code diatas digunakan untuk mengimport library `os`, `pwinput`, dan juga `prettytable`. library `os` berfungsi untuk membersihkan layar terminal,`pwinput` berfungsi untuk membuat password tidak terlihat ketika diketik, dan `prettytable` digunakan untuk membuat tampilan daftar tugas dalam bentuk tabel.<br>
2. FUNGSI TUGAS & AKUN <BR>
<img width="405" height="72" alt="Screenshot 2026-10-06 001020" src="https://github.com/user-attachments/assets/a737db24-18e1-4a1b-92e4-d03acfeb0d7e" /><BR>
Program ini menggunakan dictionary akun untuk menyimpan data login dan role pengguna, serta list Tugas untuk menyimpan daftar tugas mahasiswa. <br>
3. MEMBERSIHKAN TERMINAL <BR>
<img width="322" height="54" alt="Screenshot 2026-10-06 001311" src="https://github.com/user-attachments/assets/1913872f-92c6-4d9e-b9b1-7aeedb615d2a" /><BR>
Adapun beberapa fungsi setiap baris yang ada seperti :
`clear()` → digunakan untuk membersihkan tampilan terminal agar menu atau halaman berikutnya terlihat lebih rapi. Perintah cls digunakan pada Windows.
`jeda()` → digunakan untuk menghentikan program sementara sampai pengguna menekan Enter sebelum melanjutkan ke proses berikutnya.
4. MEMBUAT HALAMAN LOGIN <BR>
<img width="391" height="224" alt="Screenshot 2026-10-06 114633" src="https://github.com/user-attachments/assets/988a6456-c11b-4c6d-9eb6-fcd0a18cb77e" /> <BR>
Fungsi `login()` digunakan untuk **menjalankan proses login pengguna**, mulai dari membersihkan tampilan, menampilkan halaman login, meminta nama, username, dan password. `global Nama` digunakan agar nama yang dimasukkan dapat digunakan kembali di luar fungsi. Disini saya menggunakan code `global` karena agar mempermudah pengerjaan agar bisa membuat input nama dalam code. Selain itu, `pwinput` membuat password tidak terlihat saat diketik.<br>
<img width="484" height="118" alt="Screenshot 2026-10-06 003227" src="https://github.com/user-attachments/assets/f6505633-3df1-40bf-969e-2a5a1f8f9c66" /> <br>
Bagian ini berfungsi untuk memeriksa kebenaran username dan password yang telah diinput oleh pengguna. Jika pengguna menginput nilai huruf ataupun angka yang kurang dari 1 ataupun lebih dari 5, pengguna diminta memasukkan kembali username dan password sampai benar. Setelah login berhasil, program menampilkan pesan selamat datang beserta role pengguna, lalu menunggu pengguna menekan Enter. `return` digunakan untuk mengirim role pengguna (`admin` atau `mahasiswa`) ke bagian program utama. <br>

**OUTPUT:**<br>
<img width="296" height="151" alt="image" src="https://github.com/user-attachments/assets/1b6e72f9-fc5f-469e-9a86-5967dfa74f6a" /> < <BR>
Output diatas berisikan halaman pengguna ketika telah memasukkan nama panggilan dan juga memilih role antara admin/mahasiswa yang dimana akan membedakan tampilan menu yang ada. <br>




*B.MEMBUAT FUNGSI UNTUK MENU UTAMA PENGGUNA* <br>
1. MEMBUAT TAMPILAN MENU UNTUK ADMIN DAN UNTUK MAHASISWA<br>
<img width="371" height="233" alt="Screenshot 2026-10-06 004205" src="https://github.com/user-attachments/assets/e586f58a-badc-4788-aa92-caffbca17d3c" /> <br>
Bagian ini berfungsi untuk menampilkan menu utama sesuai dengan role pengguna. while True membuat menu terus ditampilkan sampai pengguna memilih keluar.Ketika role adalah admin, akan muncul menu dengan akses tambah, lihat, hapus, ubah tugas,dan keluar. Jika bukan admin, akan muncul menu mahasiswa dengan akses tambah,lihat tugasdan keluar. pilihan digunakan untuk menyimpan menu yang dipilih pengguna.<BR>
2. FUNGSI YANG DIGUNAKAN UNTUK MENJALANKAN MENU UTAMAC<BR>
<img width="418" height="363" alt="Screenshot 2026-10-06 004229" src="https://github.com/user-attachments/assets/49d271a4-2629-4808-8135-6223496426ad" /> <BR>
Bagian ini berfungsi untuk menjalankan perintah sesuai role dan menu yang dipilih pengguna. Adapun beberapa fungsi terkait yang digunakan dalam percabangan if-elif-else digunakan untuk menggunakan fungsi yang dipilih agar menjalankan perintah yang sesuai. setiap fungsinya memiliki isi tersendiri didalamnya, berikut akan dijelaskan permenu bagaimana fungsinya berjalan. <br>
**note:** saya menulis fungsi tugas karena ketika code dirun, menu akan muncul terlebih dahulu. Akan tetapi, jika sesuai urutan divscode, untuk fungsi yang berguna untuk membuat menu utama pengguna berada dibagian akhir code.<br>
**OUTPUT** <BR>
KETIKA MENGGUNAKAN ROLE ADMIN <BR>
<img width="197" height="115" alt="Screenshot 2026-10-06 010238" src="https://github.com/user-attachments/assets/cfd860f4-02df-4fb5-a57f-b4cb12d6a9e1" /> <BR>
Admin menggunakan username dan password yang berbeda sehingga ketika login dengan role admin, akan menampilkan sepenuhnya menu seperti akses tambah, lihat, hapus, ubah tugas,dan keluar.<br>
<img width="191" height="74" alt="Screenshot 2026-10-06 010320" src="https://github.com/user-attachments/assets/68dcb584-fe67-45f6-81a9-bef662009f4c" /> <br>
Role mahasiswa menggunakan username dan password yang berbeda sehingga ketika login dengan role mahasiswa, akan menampilkan beberapa menu yang cukup terbatas tidak seperti admin, yaitu akses tambah, lihat dan keluar.<br>





*C.MEMBUAT TAMBAH TUGAS UNTUK MENU PENGGUNA* <br>
1.FUNGSI UNTUK INPUT NAMA TUGAS <BR>
<img width="365" height="79" alt="Screenshot 2026-10-06 011241" src="https://github.com/user-attachments/assets/0414a7c0-ba67-4468-8bce-2c60fa28f9d9" /> <br>
Bagian ini berfungsi untuk meminta nama tugas dari pengguna dan melakukan validasi agar nama tugas tidak boleh kosong. Jika pengguna tidak memasukkan nama, `while` akan terus meminta nama kembali sampai pengguna mengisi nama tugas dengan benar.<br>
2. FUNGSI UNTUK INPUT SISA HARI <BR>
<img width="356" height="87" alt="Screenshot 2026-10-06 011247" src="https://github.com/user-attachments/assets/5a83e8c6-a185-4004-8da6-c62dda449b4c" /><BR>
Bagian ini berfungsi untuk **meminta dan memvalidasi jumlah sisa hari tugas**. Program memastikan input berupa angka dan lebih dari 0. Jika input salah, pengguna diminta memasukkan kembali. Setelah valid, `int(hari)` mengubah input dari teks menjadi **angka** agar bisa digunakan dalam perhitungan prioritas.<br>
3. FUNGSI UNTUK INPUT SKALA KESULITAN. <BR>
<img width="500" height="167" alt="Screenshot 2026-10-06 011300" src="https://github.com/user-attachments/assets/e48e39a4-0042-40a0-bdb6-552ca0a6f5f2" /> <BR>
Bagian ini berfungsi untuk menampilkan pilihan tingkat kesulitan tugas dan memvalidasi input pengguna. Pengguna harus memasukkan angka 1–5. Jika input bukan angka atau di luar dari angka 1-5, program akan meminta pengguna memasukkannya kembali. Setelah valid, `int(kesulitan)` mengubah input menjadi angka agar dapat digunakan untuk menentukan tingkat dan prioritas tugas. <br>
4.PROSES MENENTUKAN SKALA KESULITAN <br>
<img width="347" height="148" alt="Screenshot 2026-10-06 011321" src="https://github.com/user-attachments/assets/d1d841dd-68a3-4350-a7b1-3d8af7413e04" /> <br>
Bagian ini merupakan proses logika berdasar skala kesulitan yang telah diinput pengguna. Sistem akan menjalankan logika untuk menentukan bagaimana skala kesulitan yang ada. <br>
5. PROSES LOGIKA MENENTUKAN PRIORITAS <BR>
<img width="321" height="167" alt="Screenshot 2026-10-06 011208" src="https://github.com/user-attachments/assets/26358305-8143-4ed2-a6d2-cf59b0f4a38a" /> <BR>
Bagian ini digunakan untuk menentukan tingkat prioritas tugas berdasarkan sisa hari dan tingkat kesulitannya. Semakin dekat deadline dan semakin sulit tugasnya, maka prioritasnya semakin tinggi. Fungsi `return` digunakan untuk mengembalikan hasil berupa Sangat Tinggi, Tinggi, Sedang, atau Rendah. <br>

6. MENGGUNAKAN DICTIONARY UNTUK MEMASUKKAN DATA TUGAS <BR>
<img width="404" height="136" alt="Screenshot 2026-10-06 011406" src="https://github.com/user-attachments/assets/a795a3b8-75cc-433d-b809-29f69ebd8334" /> <BR>
Bagian ini berfungsi untuk menggabungkan semua data tugas ke dalam sebuah dictionary `data_tugas`, seperti nama, sisa hari, tingkat kesulitan, tingkat kesulitan dalam teks, dan prioritas. `return data_tugas` kemudian **mengembalikan data tugas tersebut** agar bisa disimpan ke dalam daftar `Tugas`.<BR>

7. MENAMBAH TUGAS KEDALAM DATA
<img width="414" height="205" alt="Screenshot 2026-10-06 011431" src="https://github.com/user-attachments/assets/88d3cb96-6377-4c4b-ba8f-cc6beee71b6a" /> <BR>
Fungsi ini digunakan untuk menambahkan tugas baru ke dalam daftar tugas. Program memanggil `tambah_tugas()` untuk memasukkan data, kemudian menyimpannya ke `Tugas` menggunakan `append()`. Setelah itu, program menampilkan kembali detail tugas dan prioritasnya, lalu `jeda()` menunggu pengguna menekan Enter. <BR>

**OUTPUT** <br>
<img width="246" height="262" alt="Screenshot 2026-10-06 013719" src="https://github.com/user-attachments/assets/6d910a3d-23b2-4f2a-a866-4fa2e8bf2e3b" /> <br>
Output diatas merupakan hasil dari menu tambah yang menampilkan nama tugas yang diinput, sisa hari, dan skala kesulitan. Dengan sistem logika diatas, akhirnya sistem menentukan seberapa prioritasnya suatu tugas dan langsung ditampilkan setelah selesai menambahkan semuanya. <br>





*D.MEMBUAT SISTEM MENAMPILKAN TUGAS DALAM MENU PENGGUNA* <br>
1.MENAMPILKAN TUGAS DALAM BENTUK LIST<BR>
<img width="404" height="119" alt="Screenshot 2026-10-06 011441" src="https://github.com/user-attachments/assets/05717ab5-34ee-4b6c-8230-2a0302b0d13f" /> <br>
Bagian ini digunakan untuk menampilkan seluruh daftar tugas yang sudah tersimpan. for digunakan untuk mengulang setiap tugas dalam Tugas, kemudian menampilkan nama, sisa hari, tingkat kesulitan, tingkat, dan prioritas dari masing-masing tugas. <br>
2. MENAMPILKAN TUGAS DALAM BENTUK TABEL <BR>
<img width="269" height="145" alt="Screenshot 2026-10-06 011450" src="https://github.com/user-attachments/assets/fb5c81a6-7919-48dc-a7ba-da8f6bd38ea6" /> <br>
Bagian ini digunakan untuk membuat tampilan tabel daftar tugas menggunakan library `PrettyTable`. `table.field_names` digunakan untuk menentukan judul kolom, seperti nomor, nama tugas, sisa hari, tingkat kesulitan, tingkat, dan prioritas. <br>
<img width="329" height="159" alt="Screenshot 2026-10-06 011501" src="https://github.com/user-attachments/assets/86b914d3-e50c-4e42-a64d-1310f52199eb" /> <br>
Bagian ini berfungsi untuk memasukkan setiap data tugas ke dalam tabel menggunakan `table.add_row()`. `for` digunakan untuk mengambil semua tugas daro data `Tugas` satu per satu, sedangkan `print(table)` digunakan untuk menampilkan tabel yang sudah dibuat . <br>
3. KETIKA TIDAK ADA TUGAS YANG MAU DITAMPILKAN <BR>
<img width="467" height="92" alt="Screenshot 2026-10-06 011514" src="https://github.com/user-attachments/assets/45e82f43-0236-49ae-91e6-bd0819fa2de5" /> <BR>
Bagian ini berfungsi untuk mengecek apakah sudah ada tugas yang tersimpan. Jika `Tugas` masih kosong, program menampilkan pesan bahwa belum ada tugas, lalu `jeda()` menunggu pengguna menekan Enter. `return` digunakan untuk menghentikan fungsi agar tidak melanjutkan ke proses berikutnya.<BR>
4. MENAMPILKAN MENU UNTUK MENAMPILKAN TUGAS SERTA LOGIKANYA <BR>.
<img width="413" height="302" alt="Screenshot 2026-10-06 011531" src="https://github.com/user-attachments/assets/1833cb0a-a217-4bb8-a928-0ad8170b0229" /> <br>
Bagian ini berfungsi untuk menampilkan pilihan cara melihat daftar tugas. Pengguna dapat memilih melihat tugas dalam bentuk list, tabel, atau kembali ke menu utama. Jika pilihan 1 atau 2 dipilih, fungsi yang sesuai akan dijalankan. Terdapat percabangan if elif dan else untuk menentukan kondisi sesuai dengan nomor yang diinput dengan pengguna. Setelah itu terdapat `break` digunakan untuk kembali ke menu utama dan `else`diakhir digunakan untuk menangani pilihan yang tidak valid. <br>

**OUTPUT**
<img width="221" height="74" alt="Screenshot 2026-10-06 015906" src="https://github.com/user-attachments/assets/96f97c35-ab06-497c-9c6e-cc455b7f009e" /> <br>
Merupakan hasil input pada menu utama ketika pengguna ingin melihat semua list tugas. pengguna bisa memilih untuk melihat tugas dalam bentuk list ataupun tugas.<br>

<img width="229" height="350" alt="Screenshot 2026-10-06 015857" src="https://github.com/user-attachments/assets/fba21530-d135-44c3-8dc2-d8b4bf4ed6fa" /> <br>
ketika pengguna memilih untuk melihat daftar tugas dalam bentuk list, diatas merupakan hasil output daftar tugas dalam bentuk list.<br>
<img width="473" height="132" alt="Screenshot 2026-10-06 015921" src="https://github.com/user-attachments/assets/09a1c20b-3642-4726-b96c-1cb15c732327" /> <br> 
Ketika pengguna memilih untuk melihat daftar tugas dalam bentuk table, diatas merupakan hasil output dari daftar tugas dalam bentuk table. <Br>






*E.MEMBUAT SISTEM MENGHAPUS TUGAS YANG ADA DALAM MENU PENGGUNA* <br>
1.MEMBUAT SISTEM PILIH TUGAS TERLEBIH DAHULU <BR>
<img width="494" height="165" alt="Screenshot 2026-10-06 011545" src="https://github.com/user-attachments/assets/ef3ee35d-52d2-4001-9755-eca6315daaf9" /> <BR>
Bagian ini digunakan untuk memilih tugas yang ingin diubah atau dihapus. Program mengecek apakah ada tugas, lalu meminta nomor tugas dan memastikan nomor yang dimasukkan benar.Benar disini adalah ketika nomor yang dimasukkan adalah sebuah angka, dan dan nomor terdapat dalam data `Tugas`. Jika tidak sesuai, sistem akan mengulang hingga akhirnya benar. Setelah itu,`return int(nomor) - 1` mengembalikan nomor tugas yang dipilih. <br>

2.MEMBUAT SISTEM MENGHAPUS TUGAS<BR>
<img width="397" height="120" alt="Screenshot 2026-10-06 011555" src="https://github.com/user-attachments/assets/b480eaea-9ff3-473d-be43-4be59268b9c1" /><BR>
Bagian diatas berguna untuk menghapus tugas yang dipilih. Yang dimana program akan meminta nomor tugas melalui pilih_tugas(), kemudian pop() menghapus tugas tersebut dari daftar. Setelah berhasil, nama tugas yang dihapus ditampilkan. <br>

**OUTPUT**
<img width="448" height="143" alt="Screenshot 2026-10-06 104344" src="https://github.com/user-attachments/assets/604487ac-09ce-47e5-9ba0-33289ccdcfe3" /> <br>
Merupakan hasil dari sistem menghapus tugas yang dimana pertama sistem akan menampilkan tugas yang tersedia, lalu ketika pengguna menginput nomor tugas yang akan dihapus, sistem akan menghapus tugas yang telah dipilih pengguna. <br>


*F.MEMBUAT SISTEM MENGUBAH TUGAS YANG ADA DALAM MENU PENGGUNA* <br>
<img width="434" height="230" alt="Screenshot 2026-10-06 111108" src="https://github.com/user-attachments/assets/24ffe525-a94a-45d8-94f2-5a1f60ac2b23" /> <br>
Bagian ini digunakan untuk mengubah data tugas yang sudah ada. Program meminta pengguna memilih tugas melalui pilih_tugas()(variable yang telah dibuat saat ingin menghapus tugas), kemudian memasukkan data tugas yang baru melalui tambah_tugas()(variabel yang dibuat ketika ingin menambah tugas). Data lama akan diganti dengan data baru menggunakan Tugas[index]. Setelah berhasil, program menampilkan pesan bahwa tugas telah diubah. <br>

**OUTPUT**<br>
<img width="468" height="356" alt="Screenshot 2026-10-06 111053" src="https://github.com/user-attachments/assets/ef2c08ae-62d3-4a85-a5bb-10ca215cb069" /> <br>
Output diatas merupakan hasil dari sistem mengubah tugas yang telah diinput oleh admin. Setelah selesai mengubah, sistem akan menampilkan hasil perubahan tugas yang telah dilakukan oleh user. <br>

**ROLE LOGIN**<br>
<img width="179" height="23" alt="image" src="https://github.com/user-attachments/assets/524d9b7d-1ade-48a4-8291-72a537a2b830" /> <BR>
Bagian ini berfungsi untuk menjalankan fungsi login() dan menyimpan role pengguna yang berhasil login ke dalam variabel role. Role ini nantinya digunakan untuk menentukan menu yang bisa diakses, seperti menu admin atau mahasiswa.<br>




*F.MEMBUAT SISTEM KELUAR* <br>
<img width="405" height="101" alt="Screenshot 2026-10-06 111508" src="https://github.com/user-attachments/assets/1f8f9ee4-6981-4cc4-8f57-e1921149c5a8" /> <BR>
Bagian ini berfungsi Ketika pengguna memilih menu keluar, sistem akan menampilkan penutup program. `clear()` membersihkan layar, kemudian program menampilkan ucapan terima kasih kepada pengguna berdasarkan nama yang dimasukkan saat login, serta memberikan pesan agar tugas dapat diselesaikan tepat waktu dan mendapat nilai yang baik.<br>

**OUTPUT**<br>
<img width="402" height="104" alt="image" src="https://github.com/user-attachments/assets/cc385898-432c-4c3d-b554-b46587866cb2" /><BR>




































