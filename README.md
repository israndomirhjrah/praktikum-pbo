# SewaKita - Sistem Penyewaan Online (Python OOP)

Program sistem penyewaan online berbasis CLI (Command Line Interface) yang
dibangun menggunakan konsep **Object-Oriented Programming (OOP)** di Python.

Sistem ini memiliki konsep seperti marketplace, di mana pengguna dapat
meng-upload barang atau jasa yang ingin disewakan, kemudian pengguna lain
dapat melihat dan menyewa barang atau jasa tersebut berdasarkan durasi
penyewaan.

---

## Identitas Pembuat

- Nama : [ISRANDO MIRHJRAH]
- NIM : [2509106093]
- Kelas : [C"25]

---

## 1. Deskripsi Program

**SewaKita** merupakan program simulasi sistem penyewaan online yang
memungkinkan pengguna untuk menawarkan barang atau jasa dan melakukan
penyewaan melalui menu yang tersedia.

Program menggunakan konsep **Object-Oriented Programming (OOP)** dengan
3 class utama yang saling berinteraksi, yaitu:

- `User`
- `BarangJasa`
- `Penyewaan`

Pengguna terlebih dahulu melakukan registrasi. Setelah itu pengguna dapat
memilih berbagai menu seperti meng-upload barang atau jasa, menyewa barang
atau jasa, melihat daftar barang, melihat data user, melihat informasi
platform, serta melakukan pengujian konsep OOP.

### Fitur Utama

- Registrasi dua user melalui input.
- Validasi username.
- Upload barang atau jasa.
- Menentukan kategori dan harga sewa.
- Melihat daftar barang atau jasa yang tersedia.
- Melakukan penyewaan berdasarkan durasi.
- Menghitung total harga penyewaan secara otomatis.
- Menampilkan data user.
- Menampilkan informasi platform.
- Private attribute untuk data penting.
- Getter dan setter menggunakan `@property`.
- Validasi data pada setter.
- Class method untuk informasi dan status class.
- Static method untuk fungsi utility.
- Pengujian instance method, class method, dan static method.
- Pengujian setter dengan data valid dan tidak valid.

---

# 2. Struktur Class

## 2.1 `User`

Class `User` digunakan untuk merepresentasikan pengguna yang terdaftar
di dalam sistem SewaKita.

### Atribut

| Atribut | Tipe | Keterangan |
|---|---|---|
| `nama` | str | Nama pengguna |
| `username` | str | Username pengguna |
| `__password` | str (private) | Password pengguna |
| `nama_platform` | str | Nama platform |
| `total_user` | int | Jumlah user yang dibuat |
| `status_platform` | str | Status platform |

### Property

- `password` (getter) — mengambil nilai password.
- `password` (setter) — mengubah password sekaligus melakukan validasi.

Validasi password:

- Tidak boleh kosong.
- Minimal memiliki 3 karakter.

### Method

| Method | Tipe | Fungsi |
|---|---|---|
| `tampilkan_data()` | instance | Menampilkan data user |
| `ubah_status_platform()` | `@classmethod` | Mengubah status platform |
| `tampilkan_info_platform()` | `@classmethod` | Menampilkan informasi platform |
| `validasi_username()` | `@staticmethod` | Memvalidasi username |

---

## 2.2 `BarangJasa`

Class `BarangJasa` digunakan untuk merepresentasikan barang atau jasa yang
ditawarkan oleh pengguna untuk disewakan.

### Atribut

| Atribut | Tipe | Keterangan |
|---|---|---|
| `pemilik` | User | Pemilik barang atau jasa |
| `nama` | str | Nama barang atau jasa |
| `kategori` | str | Kategori barang atau jasa |
| `__harga` | int | Harga sewa (private) |
| `kategori_platform` | str | Kategori yang tersedia di platform |
| `total_listing` | int | Jumlah listing |
| `status_listing` | str | Status listing |

### Property

- `harga` (getter) — mengambil harga barang atau jasa.
- `harga` (setter) — mengubah harga dengan validasi.

Validasi harga:

- Harga harus lebih dari `0`.

### Method

| Method | Tipe | Fungsi |
|---|---|---|
| `tampilkan_data()` | instance | Menampilkan data barang/jasa |
| `ubah_status_listing()` | `@classmethod` | Mengubah status listing |
| `tampilkan_info_listing()` | `@classmethod` | Menampilkan informasi listing |
| `format_harga()` | `@staticmethod` | Mengubah angka menjadi format Rupiah |

---

## 2.3 `Penyewaan`

Class `Penyewaan` digunakan untuk merepresentasikan transaksi penyewaan
antara pengguna dan barang atau jasa.

### Atribut

| Atribut | Tipe | Keterangan |
|---|---|---|
| `penyewa` | User | User yang melakukan penyewaan |
| `barang_jasa` | BarangJasa | Barang atau jasa yang disewa |
| `durasi` | int | Lama penyewaan dalam hari |
| `__total_harga` | int | Total harga penyewaan (private) |
| `nama_layanan` | str | Nama layanan penyewaan |
| `total_penyewaan` | int | Jumlah transaksi penyewaan |
| `status_sistem` | str | Status sistem |

### Property

- `total_harga` (getter) — mengambil total harga penyewaan.
- `total_harga` (setter) — mengubah total harga dengan validasi.

Validasi total harga:

- Total harga tidak boleh bernilai negatif.

### Method

| Method | Tipe | Fungsi |
|---|---|---|
| `tampilkan_detail()` | instance | Menampilkan detail penyewaan |
| `ubah_status_sistem()` | `@classmethod` | Mengubah status sistem |
| `tampilkan_info_penyewaan()` | `@classmethod` | Menampilkan informasi penyewaan |
| `hitung_total()` | `@staticmethod` | Menghitung total harga penyewaan |

---

# 3. Konsep OOP yang Digunakan

Program SewaKita menerapkan beberapa konsep utama dalam
**Object-Oriented Programming**.

## 3.1 Class dan Object

Program memiliki 3 class utama:

```text
User
BarangJasa
Penyewaan

Setiap class dapat digunakan untuk membuat object sesuai kebutuhan sistem.

Contohnya:

user1 = User(nama1, username1, password1)
barang = BarangJasa(
    user_aktif,
    nama_barang,
    kategori,
    harga
)
sewa = Penyewaan(
    user_aktif,
    barang_dipilih,
    durasi
)
3.2 Class Attribute

Setiap class memiliki class attribute yang digunakan untuk menyimpan data
yang bersifat umum atau digunakan bersama oleh object.

Contoh pada class User:

nama_platform = "SewaKita"
total_user = 0
status_platform = "Aktif"

Contoh pada class BarangJasa:

kategori_platform = "Barang dan Jasa"
total_listing = 0
status_listing = "Tersedia"

Contoh pada class Penyewaan:

nama_layanan = "Layanan Penyewaan Online"
total_penyewaan = 0
status_sistem = "Berjalan"
3.3 Instance Attribute

Instance attribute dibuat di dalam __init__() menggunakan self.

Contoh:

self.nama
self.username
self.__password

Setiap object dapat memiliki nilai yang berbeda.

3.4 Encapsulation

Program menggunakan konsep encapsulation dengan membuat beberapa
attribute sebagai private attribute.

Private attribute ditandai dengan awalan __.

Contoh:

self.__password
self.__harga
self.__total_harga

Data tersebut kemudian diakses melalui getter dan setter.

3.5 Instance Method

Instance method merupakan method yang menggunakan parameter self.

Contoh:

def tampilkan_data(self):

Method ini digunakan untuk menampilkan data dari object tertentu.

3.6 Class Method

Class method menggunakan parameter cls.

Contoh:

@classmethod
def tampilkan_info_platform(cls):

Class method digunakan untuk mengakses atau mengubah data yang dimiliki
oleh class.

3.7 Static Method

Static method tidak menggunakan self maupun cls.

Contoh:

@staticmethod
def validasi_username(username):

Static method digunakan untuk fungsi yang tidak bergantung pada object
tertentu.

4. Getter dan Setter

Program menggunakan @property untuk menerapkan getter dan setter pada
private attribute.

Getter

Getter digunakan untuk mengambil nilai private attribute.

Contoh:

@property
def password(self):
    return self.__password
Setter

Setter digunakan untuk mengubah nilai private attribute sekaligus
melakukan validasi.

Contoh:

@password.setter
def password(self, password):
    if password == "":
        raise ValueError("Password tidak boleh kosong!")

    if len(password) < 3:
        raise ValueError("Password minimal 3 karakter!")

    self.__password = password

Konsep yang sama diterapkan pada:

password
harga
total_harga
5. Validasi Data

Program memiliki beberapa validasi untuk memastikan data yang dimasukkan
oleh pengguna sesuai dengan aturan sistem.

Data	Validasi
Username	Tidak boleh kosong
Username	Tidak boleh mengandung spasi
Password	Tidak boleh kosong
Password	Minimal 3 karakter
Harga	Harus lebih dari 0
Durasi	Harus lebih dari 0
Total Harga	Tidak boleh negatif
Nomor Barang	Harus sesuai dengan daftar

Jika pengguna memasukkan data yang tidak valid, program akan memberikan
pesan kesalahan dan meminta input kembali.

6. Alur Program

Alur utama program adalah sebagai berikut:

Program Dimulai
      |
      v
Registrasi User 1
      |
      v
Registrasi User 2
      |
      v
    Menu Utama
      |
      +-------------------------+
      |                         |
      v                         v
Upload Barang/Jasa        Sewa Barang/Jasa
      |                         |
      |                         v
      |                  Pilih Barang/Jasa
      |                         |
      |                         v
      |                    Input Durasi
      |                         |
      |                         v
      |                  Hitung Total Harga
      |                         |
      +------------+------------+
                   |
                   v
          Menu Informasi
                   |
                   v
            Pengujian OOP
                   |
                   v
                Keluar
7. Menu Program

Program menyediakan menu utama sebagai berikut:

============================================================
                    MENU UTAMA
============================================================
1. Upload Barang / Jasa
2. Sewa Barang / Jasa
3. Lihat Daftar Barang / Jasa
4. Lihat Data User
5. Informasi Platform
6. Pengujian OOP
7. Keluar
============================================================
8. Fitur Program
8.1 Registrasi User

Pada awal program, pengguna diminta memasukkan data user.

=== REGISTRASI USER 1 ===

Nama     : Rando
Username : rando
Password : 093

Program kemudian membuat object User.

8.2 Upload Barang / Jasa

Pengguna memilih menu:

1. Upload Barang / Jasa

Kemudian memasukkan:

Nama barang/jasa
Kategori
Harga sewa

Contoh:

Nama barang/jasa : Kamera
Kategori         : Barang
Harga sewa       : Rp 150000

Data tersebut akan dibuat menjadi object BarangJasa.

8.3 Sewa Barang / Jasa

Pengguna dapat memilih barang atau jasa yang tersedia.

Contoh:

Pilih nomor yang ingin disewa : 1
Durasi sewa (hari) : 3

Sistem akan membuat object Penyewaan.

Total harga dihitung menggunakan rumus:

Total Harga = Harga Sewa × Durasi

Contoh:

Rp150.000 × 3 hari
= Rp450.000
8.4 Lihat Daftar Barang / Jasa

Menu ini digunakan untuk menampilkan seluruh barang atau jasa yang telah
di-upload.

Informasi yang ditampilkan:

Nama
Pemilik
Kategori
Harga
Status
8.5 Lihat Data User

Menampilkan data user yang telah terdaftar dalam sistem.

8.6 Informasi Platform

Menu ini menampilkan informasi dari masing-masing class.

Informasi yang ditampilkan meliputi:

Nama Platform
Total User
Total Listing
Total Penyewaan
Status Platform
Status Listing
Status Sistem
9. Pengujian OOP

Menu 6. Pengujian OOP digunakan untuk menunjukkan penerapan konsep
OOP pada program.

Pengujian meliputi:

1. Instance Method
2. Class Method
3. Static Method
4. Getter
5. Setter Data Valid
6. Setter Data Tidak Valid
7. Jumlah Object
8. Status Class

Program membuat object pengujian dari class BarangJasa dan Penyewaan
untuk mendemonstrasikan interaksi antar-object.

10. Panduan Pengujian
10.1 Pengujian Upload Barang / Jasa

Pilih:

1

Masukkan data barang atau jasa.

Ekspektasi:

Barang atau jasa berhasil ditambahkan dan ditampilkan pada daftar.

10.2 Pengujian Sewa Barang / Jasa

Pilih:

2

Pilih barang yang tersedia kemudian masukkan durasi.

Ekspektasi:

Sistem membuat transaksi penyewaan dan menghitung total harga secara
otomatis.

10.3 Pengujian Harga Tidak Valid

Saat upload barang, masukkan harga:

-50000

Ekspektasi:

Program menampilkan pesan:

Harga harus lebih dari 0!
10.4 Pengujian Durasi Tidak Valid

Saat melakukan penyewaan, masukkan:

0

atau angka negatif.

Ekspektasi:

Program menampilkan:

Durasi harus lebih dari 0!
10.5 Pengujian Setter Password Valid

Pada pengujian OOP, password diubah menjadi:

user1.password = "999"

Ekspektasi:

Password berhasil diubah karena memenuhi minimal 3 karakter.

10.6 Pengujian Setter Password Tidak Valid

Password diubah menjadi:

user1.password = ""

Ekspektasi:

Program menolak perubahan dan menghasilkan ValueError.

10.7 Pengujian Setter Harga Tidak Valid

Harga diubah menjadi:

barang1.harga = -50000

Ekspektasi:

Program menolak harga tersebut karena harga harus lebih dari 0.

10.8 Pengujian Setter Total Harga Tidak Valid

Total harga diubah menjadi:

sewa1.total_harga = -100000

Ekspektasi:

Program menolak perubahan karena total harga tidak boleh negatif.

11. Cara Menjalankan Program

Pastikan Python telah terinstall pada komputer.

Kemudian jalankan file program menggunakan:

python nama_file.py

Contoh:

python main.py

Setelah program dijalankan, pengguna akan diminta melakukan registrasi
dan memilih menu yang tersedia.

12. Contoh Output

Contoh tampilan awal program:

============================================================
              SEWAKITA
        SISTEM PENYEWAAN ONLINE
============================================================

=== REGISTRASI USER 1 ===
Nama     : Rando
Username : rando
Password : 093

=== REGISTRASI USER 2 ===
Nama     : User Kedua
Username : user2
Password : 123

Registrasi berhasil.
User aktif : Rando

============================================================
                    MENU UTAMA
============================================================
1. Upload Barang / Jasa
2. Sewa Barang / Jasa
3. Lihat Daftar Barang / Jasa
4. Lihat Data User
5. Informasi Platform
6. Pengujian OOP
7. Keluar
============================================================

Pilih menu : 1

Contoh ketika melakukan upload:

=== UPLOAD BARANG / JASA ===

Nama barang/jasa : Kamera
Kategori         : Barang
Harga sewa       : Rp 150000

Barang/jasa berhasil di-upload!

Nama      : Kamera
Pemilik   : Rando
Kategori  : Barang
Harga     : Rp 150.000
Status    : Tersedia

Contoh penyewaan:

=== DAFTAR BARANG / JASA ===

1 . Kamera - Rp 150.000 /hari

Pilih nomor yang ingin disewa : 1

Barang/Jasa : Kamera
Pemilik     : Rando
Harga       : Rp 150.000

Durasi sewa (hari) : 3

Penyewaan berhasil!

--- DETAIL PENYEWAAN ---
Penyewa      : User Kedua
Barang/Jasa  : Kamera
Harga/Hari   : Rp 150.000
Durasi       : 3 hari
Total Harga  : Rp 450.000
13. Struktur Project
SEWAKITA/
│
├── main.py
│
└── README.md
main.py

Berisi seluruh kode program Sistem Penyewaan Online, termasuk class:

User
BarangJasa
Penyewaan

serta menu utama dan proses input pengguna.

README.md

Berisi dokumentasi mengenai project, struktur class, fitur, konsep OOP,
alur program, dan cara menjalankan program.

14. Ringkasan Konsep
Konsep	Implementasi
Class	User, BarangJasa, Penyewaan
Object	user1, user2, barang1, barang2, sewa1, sewa2
Constructor	__init__()
Class Attribute	total_user, total_listing, total_penyewaan
Instance Attribute	nama, username, kategori, durasi
Private Attribute	__password, __harga, __total_harga
Instance Method	tampilkan_data()
Class Method	tampilkan_info_platform()
Static Method	validasi_username()
Getter	@property
Setter	@property.setter
Validation	ValueError dan validasi input
Object Interaction	User berinteraksi dengan BarangJasa dan Penyewaan
15. Kesimpulan

SewaKita merupakan implementasi sistem penyewaan online sederhana
menggunakan bahasa pemrograman Python dan konsep Object-Oriented
Programming.

Program ini memungkinkan pengguna untuk meng-upload barang atau jasa,
melihat daftar yang tersedia, melakukan penyewaan berdasarkan durasi,
serta menghitung total harga secara otomatis.

Selain fungsi utama sistem penyewaan, program juga menerapkan berbagai
konsep OOP seperti:

Class
Object
Constructor
Class Attribute
Instance Attribute
Private Attribute
Encapsulation
Instance Method
Class Method
Static Method
Getter
Setter
Validation
Object Interaction

Dengan demikian, SewaKita tidak hanya berfungsi sebagai simulasi sistem
penyewaan online, tetapi juga sebagai penerapan konsep OOP Python dalam
sebuah studi kasus yang terstruktur.
