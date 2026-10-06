import os
import pwinput
from prettytable import PrettyTable

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "mahasiswa": {"password": "user123", "role": "user"}
}
Tugas = []

def clear():
    os.system("cls")
def jeda():
    input("klik enter kalau mau lanjut...")

def login():
    global Nama
    clear()
    print("===================================")
    print(" SISTEM PRIORITAS TUGAS MAHASISWA ")
    print("===================================")
    print("=== HALAMAN LOGIN ===")
    Nama = input("MAU DIPANGGIL SIAPA?: ")
    while Nama == "":
        print("Nama tidak boleh kosong!")
        Nama = input("MAU DIPANGGIL SIAPA?: ")

    print("Pilih role anda! yang tersedia:admin/mahasiswa")
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    while username not in akun or akun[username]["password"] != password:
        print("username atau password anda salah silahkan coba lagi ya!")
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")

    print(f"Selamat datang {Nama} dengan role {akun[username]['role']}!")
    input("ayo lanjut dengan Tekan Enter ^^...")
    return akun[username]["role"], Nama

def tentukan_prioritas(hari, kesulitan):
    if hari <= 2 :
        return "Sangat Tinggi"
    elif hari <= 5 and kesulitan >=4:
        return "Tinggi"
    elif hari <= 5:
        return "Sedang"
    else:
        return "Rendah"

def tambah_tugas():
    nama = input ("masukkan nama tugas:")
    while nama == "":
        print("Nama tugas tidak boleh kosong!")
        nama = input("Masukkan nama tugas: ")
    
    hari = input("masukkan sisa hari tugas:")
    while not hari.isdigit() or int(hari) <= 0:
        print("masukkan sisa hari yang benar!")
        hari = input("masukkan sisa hari tugas:")
    hari = int(hari)

    print("skala kesulitan :")
    print("1. Sangat Mudah")
    print("2. Mudah")
    print("3. sedang")
    print("4. Sulit")
    print("5. sangat sulit")
    kesulitan = input("masukkan skala kesulitan (1-5):")
    while not kesulitan.isdigit() or int(kesulitan) < 1 or int(kesulitan) > 5:
        print("Skala Kesulitan harus berupa angka 1 sampai 5!")
        kesulitan = input("Masukkan skala kesulitan (1-5): ")
    kesulitan = int(kesulitan)

    if kesulitan == 1:
        tingkat = "sangat mudah"
    elif kesulitan == 2:
        tingkat = "Mudah"
    elif kesulitan == 3:
        tingkat = "sedang"
    elif kesulitan == 4:
        tingkat = "sulit"
    else:
        tingkat = "sangat sulit"

    data_tugas = {
            "nama": nama,
            "hari": hari,
            "kesulitan": kesulitan,
            "tingkat": tingkat,
            "prioritas": tentukan_prioritas(hari, kesulitan)
    }

    return data_tugas
def input_tugas():
    clear()
    print("=== TAMBAHKAN TUGAS ===")
    data_tugas = tambah_tugas()
    Tugas.append(data_tugas)
    print("Tugas berhasil ditambahkan!")
    print("---------------------------")
    print("Nama tugas      :", data_tugas["nama"])
    print("Sisa Hari       :", data_tugas["hari"])
    print("Skala kesulitan :", data_tugas["kesulitan"])
    print("Tingkat         :", data_tugas["tingkat"])
    print("Prioritas       :", data_tugas["prioritas"])
    print("---------------------------")
    jeda()

def tampilkan_tugas():
    for i in range(len(Tugas)):
        print("Tugas", i + 1)
        print("Nama Tugas     :", Tugas[i]["nama"])
        print("Sisa Hari      :", Tugas[i]["hari"])
        print("Skala Kesulitan:", Tugas[i]["kesulitan"])
        print("Tingkat        :", Tugas[i]["tingkat"])
        print("Prioritas      :", Tugas[i]["prioritas"])

def lihat_tabel():
    table = PrettyTable()
    table.field_names = [
        "No", 
        "Nama Tugas",
        "Sisa Hari", 
        "Skala Kesulitan", 
        "Tingkat", 
        "Prioritas"
    ]

    for i in range(len(Tugas)):
        table.add_row([
            i + 1,
            Tugas[i]["nama"],
            Tugas[i]["hari"],
            Tugas[i]["kesulitan"],
            Tugas[i]["tingkat"],
            Tugas[i]["prioritas"]
        ])

    print(table)

def lihat_tugas():
    clear()
    if len(Tugas) == 0:
        print("Belum ada tugas yang kamu simpan. ayo mulai tambahin!")
        jeda()
        return

    while True:
        clear()
        print("=== LIHAT DAFTAR TUGAS ===")
        print("1. Lihat tugas dalam bentuk list")
        print("2. Lihat tugas dalam bentuk tabel")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == "1":
            clear()
            tampilkan_tugas()
            jeda()
        elif pilihan == "2":
            clear()
            lihat_tabel()
            jeda()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")
            jeda()

def pilih_tugas():
    if len(Tugas) == 0:
        print("Belum ada tugas yang dapat diubah.")
        return -1
    lihat_tabel()
    nomor = input("Pilih nomor tugas : ")

    while not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(Tugas):
        print("Nomor tugas tidak ada!")
        nomor = input("Pilih nomor tugas : ")
    return int(nomor) - 1

def hapus_tugas():
    clear()
    print ("===== HAPUS TUGAS =====")
    index = pilih_tugas()
    if index != -1:
        nama_dihapus = Tugas[index]["nama"]
        Tugas.pop(index)
        print("Tugas", nama_dihapus, "berhasil dihapus!")
    jeda()

def ubah_tugas():
    clear()
    print("===== UBAH TUGAS =====")
    index = pilih_tugas()
    if index != -1:
        print("Masukkan data tugas yang baru:")
        Tugas[index] = tambah_tugas()
        print("Tugas berhasil diubah!")
        print("Tugas Berhasil diubah! ^^")
        print("===================================")
        print("Nama Tugas      :", Tugas[index]["nama"])
        print("Sisa hari       :", Tugas[index]["hari"])
        print("Skala kesulitan :", Tugas[index]["kesulitan"])
        print("Tingkat         :", Tugas[index]["tingkat"])
        print("Prioritas       :", Tugas[index]["prioritas"])
    jeda()

role = login()

while True:
    clear()
    if role == "admin":
        print("==== MENU UTAMA ADMIN ====")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Ubah Tugas")
        print("5. Keluar")
    else:
        print("==== MENU UTAMA MAHASISWA ====")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Keluar")
    
    pilihan = input("Pilih menu: ") 

    if role == "admin":
        if pilihan == "1":
            input_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            hapus_tugas()
        elif pilihan == "4":
            ubah_tugas()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")
            jeda()

    else:
        if pilihan == "1":
            input_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")
            jeda()

clear()
print(f"Terima kasih telah menggunakan sistem ini, {Nama}!")
print("=================================================")
print("Terima kasih", Nama, "telah menggunakan program ini!")
print("semoga semua tugas dapat diselesaikan tepat waktu")
print("dan mendapat nilai terbaik", Nama, "ya!")
print("=================================================")
