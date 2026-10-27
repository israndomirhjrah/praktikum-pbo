# SewaKita - Sistem Penyewaan Online

Program sistem penyewaan online berbasis **CLI (Command Line Interface)** yang dibuat menggunakan bahasa pemrograman Python dan menerapkan konsep **Object-Oriented Programming (OOP)**.

SewaKita memiliki konsep seperti marketplace sederhana, yaitu pengguna dapat menawarkan barang atau jasa untuk disewakan, kemudian pengguna lain dapat menyewa barang atau jasa berdasarkan durasi tertentu.

---

## Identitas Pembuat

- **Nama:** Isrando Mirhjrah
- **NIM:** 2509106093
- **Kelas:** C'25

---

# 1. Deskripsi Program

**SewaKita** merupakan simulasi sistem penyewaan online yang memungkinkan pengguna untuk melakukan aktivitas sebagai penyewa maupun pemilik barang/jasa.

Program memiliki beberapa class utama yang saling berinteraksi, yaitu:

- `User`
- `Penyewa`
- `Pemilik`
- `BarangJasa`
- `DetailSewa`
- `Penyewaan`

Program dimulai dengan proses registrasi penyewa dan pemilik. Setelah registrasi, pengguna dapat memilih berbagai menu seperti:

- Upload barang/jasa
- Menyewa barang/jasa
- Melihat daftar barang/jasa
- Melihat data user
- Melihat informasi platform
- Menguji konsep OOP
- Mengganti user aktif
- Keluar dari program

---

# 2. Fitur Utama

Fitur yang tersedia pada program SewaKita:

- Registrasi penyewa
- Registrasi pemilik
- Validasi username
- Upload barang atau jasa
- Menentukan kategori barang/jasa
- Menentukan harga sewa
- Melihat daftar barang/jasa
- Melakukan penyewaan
- Menentukan durasi penyewaan
- Menghitung total harga secara otomatis
- Menampilkan data user
- Mengganti user aktif
- Informasi platform
- Getter dan setter
- Private attribute
- Class method
- Static method
- Instance method
- Inheritance
- Polymorphism
- Relasi UML
- Validasi input

---

# 3. Struktur Class

## 3.1 Class `User`

`User` merupakan superclass yang menjadi dasar untuk class `Penyewa` dan `Pemilik`.

### Class Attribute

```python
nama_platform = "SewaKita"
total_user = 0
status_platform = "Aktif"
```

### Instance Attribute

- `_nama`
- `username`
- `__password`

Password menggunakan private attribute sehingga tidak dapat diakses secara langsung dari luar class.

### Method

- `__init__()`
- `tampilkan_data()`
- `tampilkan_peran()`
- `password`
- `ubah_status_platform()`
- `tampilkan_info_platform()`
- `validasi_username()`

Class `User` juga menggunakan getter dan setter untuk mengakses password.

---

# 4. Inheritance

Program menerapkan konsep **Inheritance** dengan menjadikan `User` sebagai superclass.

Struktur inheritance:

```text
             User
            /    \
           /      \
      Penyewa    Pemilik
```

## 4.1 Class `Penyewa`

`Penyewa` merupakan subclass dari `User`.

```python
class Penyewa(User):
```

Class ini memiliki atribut tambahan:

```python
alamat
```

Constructor `Penyewa` menggunakan:

```python
super().__init__(nama, username, password)
```

Dengan demikian, atribut dari superclass `User` dapat digunakan kembali oleh `Penyewa`.

Penyewa juga melakukan overriding terhadap:

```python
tampilkan_data()
tampilkan_peran()
```



---

## 4.2 Class `Pemilik`

`Pemilik` juga merupakan subclass dari `User`.

```python
class Pemilik(User):
```

Class ini memiliki atribut tambahan:

```python
nama_toko
daftar_barang
```

Constructor menggunakan:

```python
super().__init__(nama, username, password)
```

Pemilik juga melakukan overriding terhadap:

```python
tampilkan_data()
tampilkan_peran()
```

Selain itu, class `Pemilik` memiliki method:

```python
tambah_barang()
```

yang digunakan untuk memasukkan barang/jasa ke dalam daftar milik pemilik.



---

# 5. Polymorphism

Program menerapkan **Polymorphism** melalui overriding method.

Class `User` memiliki:

```python
tampilkan_data()
tampilkan_peran()
```

Kemudian method tersebut diimplementasikan kembali pada:

- `Penyewa`
- `Pemilik`

Contohnya:

```text
User
 ├── tampilkan_data()
 └── tampilkan_peran()

Penyewa
 ├── tampilkan_data()
 └── tampilkan_peran()

Pemilik
 ├── tampilkan_data()
 └── tampilkan_peran()
```

Walaupun nama method sama, hasil yang ditampilkan berbeda sesuai jenis object.

Contohnya:

```text
Peran : Penyewa
```

sedangkan object `Pemilik` menampilkan:

```text
Peran : Pemilik
```

---

# 6. Class `BarangJasa`

Class `BarangJasa` digunakan untuk merepresentasikan barang atau jasa yang ditawarkan oleh pemilik.

### Class Attribute

```python
kategori_platform = "Barang dan Jasa"
total_listing = 0
status_listing = "Tersedia"
```

### Instance Attribute

- `pemilik`
- `nama`
- `kategori`
- `__harga`

Harga dibuat sebagai private attribute:

```python
self.__harga
```

### Method

- `tampilkan_data()`
- `harga` sebagai property
- `ubah_status_listing()`
- `tampilkan_info_listing()`
- `format_harga()`



---

# 7. Class `DetailSewa`

Class `DetailSewa` digunakan untuk menyimpan detail dari proses penyewaan.

### Attribute

```python
harga_per_hari
durasi
__total
```

Total harga dihitung berdasarkan:

```text
Total = Harga per Hari × Durasi
```

Contoh:

```text
Harga per hari = Rp150.000
Durasi = 3 hari

Total = Rp150.000 × 3
      = Rp450.000
```

Class ini juga memiliki property `total` yang menggunakan getter dan setter.



---

# 8. Class `Penyewaan`

Class `Penyewaan` digunakan untuk merepresentasikan transaksi penyewaan.

### Class Attribute

```python
nama_layanan = "Layanan Penyewaan Online"
total_penyewaan = 0
status_sistem = "Berjalan"
```

### Instance Attribute

- `penyewa`
- `barang_jasa`
- `detail`

Class `Penyewaan` membuat object `DetailSewa` di dalam constructor:

```python
self.detail = DetailSewa(
    barang_jasa.harga,
    durasi
)
```

Class ini juga menyediakan:

- `tampilkan_detail()`
- `total_harga`
- `ubah_status_sistem()`
- `tampilkan_info_penyewaan()`
- `hitung_total()`



---

# 9. Konsep OOP yang Digunakan

## 9.1 Class

Program menggunakan beberapa class:

```text
User
Penyewa
Pemilik
BarangJasa
DetailSewa
Penyewaan
```

---

## 9.2 Object

Object dibuat berdasarkan class yang tersedia.

Contohnya:

```python
user1 = Penyewa(...)
user2 = Pemilik(...)
barang = BarangJasa(...)
sewa = Penyewaan(...)
```

---

## 9.3 Constructor

Constructor menggunakan:

```python
__init__()
```

Constructor digunakan untuk memberikan nilai awal kepada object.

---

## 9.4 Class Attribute

Class attribute digunakan untuk menyimpan data yang bersifat umum dan digunakan oleh seluruh object dalam class.

Contoh:

```python
User.total_user
BarangJasa.total_listing
Penyewaan.total_penyewaan
```

---

## 9.5 Instance Attribute

Instance attribute merupakan atribut yang dimiliki oleh masing-masing object.

Contoh:

```python
self.username
self.alamat
self.nama_toko
self.nama
self.kategori
self.durasi
```

---

## 9.6 Encapsulation

Program menerapkan **Encapsulation** dengan menggunakan private attribute.

Contoh:

```python
self.__password
self.__harga
self.__total
```

Data tersebut tidak diakses secara langsung, tetapi melalui property getter dan setter.

---

## 9.7 Getter

Getter digunakan untuk mengambil nilai private attribute.

Contoh:

```python
@property
def password(self):
    return self.__password
```

Getter juga digunakan pada:

```text
password
harga
total
total_harga
```

---

## 9.8 Setter

Setter digunakan untuk mengubah nilai private attribute sekaligus melakukan validasi.

Contoh:

```python
@password.setter
def password(self, password):
    if password == "":
        raise ValueError("Password tidak boleh kosong!")

    if len(password) < 3:
        raise ValueError("Password minimal 3 karakter!")

    self.__password = password
```

---

# 10. Instance Method

Instance method merupakan method yang menggunakan parameter `self`.

Contoh:

```python
def tampilkan_data(self):
```

Instance method digunakan untuk mengakses data dari object tertentu.

Contoh lainnya:

```python
tampilkan_peran()
tambah_barang()
tampilkan_detail()
```

---

# 11. Class Method

Class method menggunakan decorator:

```python
@classmethod
```

dan parameter:

```python
cls
```

Contohnya:

```python
@classmethod
def tampilkan_info_platform(cls):
```

Class method digunakan untuk mengakses atau mengubah data yang dimiliki oleh class.

Class method yang digunakan antara lain:

```text
User.ubah_status_platform()
User.tampilkan_info_platform()

BarangJasa.ubah_status_listing()
BarangJasa.tampilkan_info_listing()

Penyewaan.ubah_status_sistem()
Penyewaan.tampilkan_info_penyewaan()
```

---

# 12. Static Method

Static method menggunakan:

```python
@staticmethod
```

Static method tidak membutuhkan `self` maupun `cls`.

Contohnya:

```python
@staticmethod
def validasi_username(username):
    return username != "" and " " not in username
```

Static method lainnya:

```python
BarangJasa.format_harga()
Penyewaan.hitung_total()
```

---

# 13. Validasi Data

Program memiliki beberapa validasi.

### Username

Username:

- Tidak boleh kosong
- Tidak boleh mengandung spasi

### Password

Password:

- Tidak boleh kosong
- Minimal 3 karakter

### Harga

Harga harus lebih dari:

```text
0
```

### Durasi

Durasi harus lebih dari:

```text
0
```

### Total Harga

Total harga tidak boleh negatif.

### Nomor Barang

Nomor barang harus sesuai dengan daftar barang/jasa.

---

# 14. Relasi UML

Program menerapkan tiga jenis relasi UML yang digunakan dalam tugas.

## 14.1 Asosiasi

Asosiasi terjadi antara class `Penyewaan` dengan `Penyewa` dan `BarangJasa`.

Pada class `Penyewaan` terdapat:

```python
self.penyewa = penyewa
self.barang_jasa = barang_jasa
```

Artinya transaksi penyewaan berhubungan dengan:

```text
Penyewa
   |
   | melakukan
   v
Penyewaan
   |
   | terhadap
   v
BarangJasa
```

Relasi ini disebut **Asosiasi** karena object `Penyewaan` berhubungan dengan object `Penyewa` dan `BarangJasa`.

Kode pengujian program juga secara langsung menjelaskan bahwa `Penyewaan` berhubungan dengan `Penyewa` dan `BarangJasa`.

---

## 14.2 Agregasi

Agregasi terjadi antara `Pemilik` dan `BarangJasa`.

Class `Pemilik` memiliki:

```python
self.daftar_barang = []
```

Kemudian barang ditambahkan menggunakan:

```python
self.daftar_barang.append(barang)
```

Artinya:

```text
Pemilik
   ◇
   |
   +── BarangJasa
   +── BarangJasa
   +── BarangJasa
```

`Pemilik` memiliki kumpulan `BarangJasa`, tetapi object `BarangJasa` tetap dapat dianggap sebagai object tersendiri.

Program juga mendemonstrasikan relasi ini melalui bagian pengujian UML.

---

## 14.3 Komposisi

Komposisi terjadi antara `Penyewaan` dan `DetailSewa`.

Di dalam constructor `Penyewaan` terdapat:

```python
self.detail = DetailSewa(
    barang_jasa.harga,
    durasi
)
```

Artinya object `DetailSewa` dibuat sebagai bagian dari object `Penyewaan`.

Strukturnya:

```text
Penyewaan
    ◆
    |
    v
DetailSewa
```

Relasi ini digunakan karena `DetailSewa` menjadi bagian dari informasi transaksi penyewaan.

Kode program juga secara eksplisit menguji relasi tersebut sebagai **Komposisi**.

---

# 15. Diagram Hubungan Class

Secara sederhana hubungan antar-class dapat digambarkan:

```text
                    User
                   /    \
                  /      \
                 v        v
             Penyewa    Pemilik
                           |
                           |
                           ◇
                           |
                           v
                       BarangJasa
                           ^
                           |
                           |
                       Asosiasi
                           |
                           |
                       Penyewaan
                           |
                           ◆
                           |
                           v
                       DetailSewa
```

Keterangan:

```text
Inheritance  : User → Penyewa
               User → Pemilik

Asosiasi     : Penyewaan → Penyewa
               Penyewaan → BarangJasa

Agregasi     : Pemilik ◇→ BarangJasa

Komposisi    : Penyewaan ◆→ DetailSewa
```

---

# 16. Alur Program

Alur utama program:

```text
Program Dimulai
       |
       v
Registrasi Penyewa
       |
       v
Registrasi Pemilik
       |
       v
User Aktif
       |
       v
Menu Utama
       |
       +-----------------------------+
       |                             |
       v                             v
Upload Barang/Jasa             Sewa Barang/Jasa
       |                             |
       v                             v
Pemilik memasukkan data        Pilih Barang/Jasa
       |                             |
       v                             v
Barang dibuat                  Input Durasi
       |                             |
       v                             v
Masuk daftar barang            Hitung Total Harga
                                     |
                                     v
                               Buat Penyewaan
                                     |
                                     v
                              Tampilkan Detail
```

Selain itu pengguna dapat:

```text
Menu Utama
   |
   +-- Lihat Daftar Barang/Jasa
   |
   +-- Lihat Data User
   |
   +-- Informasi Platform
   |
   +-- Pengujian OOP
   |
   +-- Ganti User Aktif
   |
   +-- Keluar
```

---

# 17. Menu Program

Program memiliki menu:

```text
============================================================
                    MENU UTAMA
============================================================
1. Upload Barang / Jasa
2. Sewa Barang / Jasa
3. Lihat Daftar Barang / Jasa
4. Lihat Data User
5. Informasi Platform
6. Pengujian OOP
7. Ganti User Aktif
8. Keluar
============================================================
```

Menu tersebut terdapat langsung pada program utama.

---

# 18. Proses Upload Barang/Jasa

Menu:

```text
1. Upload Barang / Jasa
```

Hanya object dengan tipe `Pemilik` yang dapat melakukan upload.

Program melakukan pengecekan:

```python
if not isinstance(user_aktif, Pemilik):
```

Jika user aktif bukan pemilik, program akan menampilkan pesan bahwa hanya pemilik yang dapat melakukan upload.

Setelah itu pemilik memasukkan:

```text
Nama barang/jasa
Kategori
Harga sewa
```

Kemudian dibuat object:

```python
barang = BarangJasa(
    user_aktif,
    nama_barang,
    kategori,
    harga
)
```

Barang kemudian dimasukkan ke daftar barang dan daftar barang milik pemilik.

---

# 19. Proses Penyewaan

Menu:

```text
2. Sewa Barang / Jasa
```

Pengguna memilih barang/jasa dari daftar yang tersedia.

Kemudian memasukkan:

```text
Durasi sewa
```

Program membuat object:

```python
sewa = Penyewaan(
    user_aktif,
    barang_dipilih,
    durasi
)
```

Object `Penyewaan` kemudian membuat object `DetailSewa` dan menghitung total harga.

Rumus:

```text
Total Harga = Harga per Hari × Durasi
```

Contoh:

```text
Harga       : Rp150.000
Durasi      : 3 hari

Total Harga : Rp450.000
```

---

# 20. Pengujian OOP

Menu **Pengujian OOP** digunakan untuk menunjukkan bahwa konsep OOP pada program benar-benar digunakan.

Pengujian meliputi:

1. Instance Method
2. Class Method
3. Static Method
4. Getter
5. Setter Data Valid
6. Setter Data Tidak Valid
7. Inheritance
8. Relasi UML
9. Jumlah Object
10. Status Class

Program membuat beberapa object pengujian:

```text
barang1
barang2
sewa1
sewa2
```

Kemudian object tersebut digunakan untuk menguji berbagai konsep OOP.

---

# 21. Pengujian Setter

## Setter Valid

Contoh:

```python
user1.password = "999"
barang1.harga = 200000
sewa1.total_harga = 400000
```

Data diterima karena memenuhi aturan validasi.

## Setter Tidak Valid

Contoh:

```python
user1.password = ""
barang1.harga = -50000
sewa1.total_harga = -100000
```

Program akan menolak data tersebut dan menghasilkan `ValueError`.

---

# 22. Pengujian Inheritance

Program menampilkan hubungan:

```text
Superclass : User
Subclass 1 : Penyewa
Subclass 2 : Pemilik
```

Kemudian menunjukkan penggunaan:

```python
super().__init__()
```

pada class `Penyewa` dan `Pemilik`.

Dengan demikian, atribut dan constructor dari `User` dapat digunakan kembali oleh subclass.

---

# 23. Pengujian Relasi UML

Program menampilkan:

```text
Asosiasi  : Penyewaan berhubungan dengan Penyewa dan BarangJasa.

Agregasi  : Pemilik memiliki daftar BarangJasa.

Komposisi : Penyewaan memiliki objek DetailSewa.
```

Pengujian tersebut menunjukkan penerapan ketiga relasi UML dalam program.

---

# 24. Struktur Project

Struktur project:

```text
SEWAKITA/
│
├── main.py
│
└── README.md
```

### `main.py`

Berisi seluruh kode program SewaKita, termasuk:

- Class `User`
- Class `Penyewa`
- Class `Pemilik`
- Class `BarangJasa`
- Class `DetailSewa`
- Class `Penyewaan`
- Menu utama
- Input pengguna
- Proses upload
- Proses penyewaan
- Pengujian OOP

### `README.md`

Berisi dokumentasi project, penjelasan class, konsep OOP, inheritance, polymorphism, relasi UML, alur program, pengujian, dan cara menjalankan program.

---

# 25. Cara Menjalankan Program

Pastikan Python sudah terinstall.

Buka terminal pada folder project kemudian jalankan:

```bash
python main.py
```

Setelah program dijalankan, pengguna akan diminta melakukan registrasi dan kemudian masuk ke menu utama.

---

# 26. Ringkasan Konsep OOP

| Konsep | Implementasi |
|---|---|
| Class | User, Penyewa, Pemilik, BarangJasa, DetailSewa, Penyewaan |
| Object | user1, user2, barang1, barang2, sewa1, sewa2 |
| Constructor | `__init__()` |
| Class Attribute | `total_user`, `total_listing`, `total_penyewaan` |
| Instance Attribute | `username`, `alamat`, `nama_toko`, `nama`, `kategori`, `durasi` |
| Private Attribute | `__password`, `__harga`, `__total` |
| Encapsulation | Private attribute + property |
| Inheritance | `Penyewa(User)`, `Pemilik(User)` |
| Polymorphism | Overriding `tampilkan_data()` dan `tampilkan_peran()` |
| Instance Method | `tampilkan_data()` |
| Class Method | `tampilkan_info_platform()` |
| Static Method | `validasi_username()` |
| Getter | `@property` |
| Setter | `@property.setter` |
| Validation | `ValueError` dan validasi input |
| Asosiasi | `Penyewaan` dengan `Penyewa` dan `BarangJasa` |
| Agregasi | `Pemilik` dengan `BarangJasa` |
| Komposisi | `Penyewaan` dengan `DetailSewa` |

---

# 27. Kesimpulan

SewaKita merupakan program simulasi sistem penyewaan online berbasis Python yang menerapkan konsep **Object-Oriented Programming** secara terstruktur.

Program memiliki beberapa class yang saling berinteraksi, yaitu `User`, `Penyewa`, `Pemilik`, `BarangJasa`, `DetailSewa`, dan `Penyewaan`.

Konsep OOP yang diterapkan meliputi:

- Class
- Object
- Constructor
- Class Attribute
- Instance Attribute
- Private Attribute
- Encapsulation
- Getter
- Setter
- Instance Method
- Class Method
- Static Method
- Inheritance
- Polymorphism
- Validation

Selain itu, program juga menerapkan tiga relasi UML yang menjadi bagian dari tugas, yaitu:

```text
Asosiasi
Agregasi
Komposisi
```

Dengan adanya konsep tersebut, SewaKita tidak hanya berfungsi sebagai simulasi sistem penyewaan online, tetapi juga menjadi contoh penerapan OOP Python yang mencakup hubungan antar-object, inheritance, encapsulation, polymorphism, serta relasi UML dalam sebuah studi kasus.
