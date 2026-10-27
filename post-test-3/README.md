# SewaKita — Sistem Penyewaan Online

> Program simulasi marketplace penyewaan barang dan jasa berbasis **Python CLI (Command Line Interface)** yang menerapkan konsep **Object-Oriented Programming (OOP)**.

SewaKita dirancang sebagai marketplace sederhana. Pengguna dapat berperan sebagai **Penyewa** atau **Pemilik**. Pemilik dapat menawarkan barang/jasa beserta kategori dan harga sewa per hari, sedangkan penyewa dapat memilih listing yang tersedia dan menentukan durasi sewa. Program kemudian menampilkan rincian transaksi serta menghitung total biaya berdasarkan harga per hari dikalikan durasi.

README ini menjelaskan struktur kelas, fungsi method, relasi UML, penerapan konsep OOP, alur penggunaan, serta bukti output program.

## Identitas Pembuat

- **Nama:** Isrando Mirhjrah
- **NIM:** 2509106093
- **Kelas:** C'25

---

# 1. Deskripsi Program

SewaKita merupakan aplikasi berbasis terminal yang menyimulasikan proses penyewaan barang atau jasa secara sederhana. Program dimulai dengan registrasi satu penyewa dan satu pemilik. Setelah itu, pengguna dapat menggunakan menu utama dan berpindah dari satu akun ke akun lainnya melalui menu **Ganti User Aktif**.

Program tidak menggunakan database; data disimpan dalam object dan list selama program berjalan. Karena itu, data yang dimasukkan akan hilang ketika program ditutup.

## Tujuan program

1. Mempraktikkan pembuatan class dan object dengan Python.
2. Menunjukkan penggunaan atribut class dan atribut instance.
3. Menerapkan enkapsulasi melalui atribut private dan property.
4. Menerapkan abstraksi melalui abstract class dan abstract method.
5. Mempraktikkan inheritance dan polimorfisme.
6. Menunjukkan asosiasi, agregasi, dan komposisi antarkelas.
7. Menggunakan validasi input agar beberapa nilai yang tidak sesuai ditolak.

# 2. Fitur Utama

Fitur yang tersedia pada program:

- Registrasi penyewa dengan nama, username, password, dan alamat.
- Registrasi pemilik dengan nama, username, password, dan nama toko.
- Validasi username agar tidak kosong dan tidak mengandung spasi.
- Pembatasan fitur upload sehingga hanya pengguna dengan tipe `Pemilik` yang dapat mengunggah listing.
- Penambahan barang/jasa dengan nama, kategori, dan harga sewa per hari.
- Penyimpanan listing pada daftar umum dan pada daftar barang milik pemilik.
- Penampilan daftar barang/jasa.
- Penyewaan listing berdasarkan durasi hari.
- Perhitungan total biaya sewa.
- Penampilan data pengguna dan informasi platform.
- Penggantian pengguna aktif.
- Pengujian abstraksi, polimorfisme, duck typing, dan operator overloading.
- Property getter/setter untuk mengakses atau mengubah data tertentu dengan validasi.

## Menu utama

```text
=======================================================
SEWAKITA - SISTEM PENYEWAAN ONLINE
=======================================================
1. Upload Barang/Jasa
2. Sewa Barang/Jasa
3. Lihat Daftar Barang/Jasa
4. Lihat Data User
5. Informasi Platform
6. Pengujian OOP (ABC, polimorfisme, duck typing)
7. Ganti User Aktif
8. Keluar
```

**Catatan:** menu yang tersedia dapat digunakan setelah registrasi penyewa dan pemilik selesai. Pengguna aktif awalnya adalah penyewa.

# 3. Struktur dan Tanggung Jawab Class

Program menggunakan kelas-kelas berikut.

| Class | Tanggung jawab |
|---|---|
| `User` | Kelas abstrak yang menyediakan data dan perilaku umum pengguna. |
| `Penyewa` | Mewakili pengguna yang menyewa barang/jasa dan memiliki atribut alamat. |
| `Pemilik` | Mewakili pengguna yang menawarkan barang/jasa dan memiliki nama toko serta daftar listing. |
| `BarangJasa` | Menyimpan data listing: pemilik, nama, kategori, harga, dan status listing. |
| `Penyewaan` | Menghubungkan penyewa dengan barang/jasa yang dipilih serta menyimpan detail transaksi. |
| `DetailSewa` | Menyimpan harga per hari, durasi, dan total biaya penyewaan. |
| `RingkasanPlatform` | Contoh kelas yang menampilkan ringkasan melalui method `tampilkan_ringkasan()`. |
| `RingkasanListing` | Contoh kelas lain yang menyediakan method `tampilkan_ringkasan()` untuk sebuah listing. |

`RingkasanPlatform` dan `RingkasanListing` digunakan dalam demonstrasi duck typing. Keduanya tidak diturunkan dari `User` atau `BarangJasa`; keduanya dapat diproses oleh fungsi yang membutuhkan method `tampilkan_ringkasan()`.

# 4. Class Diagram

![Class Diagram SewaKita](class_diagram_sewakita.png)

Diagram di atas menggambarkan kelas-kelas utama, pewarisan `User`, serta hubungan asosiasi, agregasi, dan komposisi.

## 4.1 Inheritance (Pewarisan)

Pewarisan terjadi ketika suatu kelas turunan mewarisi atribut atau perilaku dari kelas induk. Dalam SewaKita, `User` menjadi kelas induk, sedangkan `Penyewa` dan `Pemilik` menjadi kelas turunan.

```text
              User (abstract)
                /       \
               /         \
          Penyewa       Pemilik
```

Deklarasi kelasnya:

```python
class Penyewa(User):
    ...

class Pemilik(User):
    ...
```

Kedua kelas turunan memanggil constructor kelas induk melalui `super().__init__(nama, username, password)`. Dengan demikian, data umum pengguna tidak perlu ditulis ulang seluruhnya pada masing-masing kelas.

Keduanya juga menyediakan implementasi untuk abstract method `tampilkan_peran()` dan `deskripsi_akun()` yang diwajibkan oleh kelas `User`.

## 4.2 Asosiasi

**Asosiasi** menunjukkan bahwa objek dari satu kelas berhubungan dengan objek kelas lain. Pada program ini, relasi tersebut terlihat pada kelas `Penyewaan`.

```python
self.penyewa = penyewa
self.barang_jasa = barang_jasa
```

Atribut `penyewa` menyimpan objek `Penyewa` yang melakukan transaksi, sedangkan `barang_jasa` menyimpan objek `BarangJasa` yang dipilih. Ketika detail transaksi ditampilkan, program menggunakan kedua referensi tersebut untuk menampilkan nama penyewa, nama listing, dan pemilik listing.

`BarangJasa` juga menyimpan referensi ke pemiliknya:

```python
self.pemilik = pemilik
```

Artinya, sebuah listing dapat menampilkan informasi pemilik dan nama toko yang menawarkan listing tersebut.

Secara ringkas:

```text
Penyewa ───── Penyewaan ───── BarangJasa
                                  |
                                  | referensi pemilik
                                  v
                                Pemilik
```

## 4.3 Agregasi

**Agregasi** adalah hubungan keseluruhan dan bagian yang relatif longgar. Pada SewaKita, kelas `Pemilik` menyimpan beberapa listing melalui atribut `daftar_barang`.

```python
self.daftar_barang = []

def tambah_barang(self, barang):
    self.daftar_barang.append(barang)
```

Ketika pemilik mengunggah barang/jasa, program membuat objek `BarangJasa`, lalu menambahkannya ke daftar barang umum dan daftar milik pemilik. Objek listing tersebut tetap merupakan objek tersendiri, bukan dibuat di dalam constructor `Pemilik`.

Representasi sederhananya:

```text
Pemilik ◇──────── BarangJasa
       daftar_barang
```

Simbol wajik kosong `◇` digunakan untuk menandai agregasi. Maknanya, pemilik mengelompokkan listing yang ditawarkannya.

## 4.4 Komposisi

**Komposisi** adalah hubungan keseluruhan dan bagian yang lebih kuat. Pada program ini, `Penyewaan` membuat objek `DetailSewa` di dalam constructor-nya.

```python
self.detail = DetailSewa(barang_jasa.harga, durasi)
```

Objek `DetailSewa` menyimpan `harga_per_hari`, `durasi`, dan `__total`. Kelas `Penyewaan` menggunakan objek detail tersebut untuk menampilkan rincian transaksi dan menyediakan property `total_harga`.

```text
Penyewaan ◆──────── DetailSewa
```

Simbol wajik terisi `◆` digunakan untuk menandai komposisi. Dalam desain program ini, detail dibuat sebagai bagian dari proses pembuatan transaksi penyewaan.

# 5. Penjelasan Setiap Class

## 5.1 Class `User`

`User` merupakan kelas abstrak yang menjadi dasar bagi semua pengguna SewaKita. Kelas ini mengumpulkan atribut dan perilaku umum agar dapat digunakan kembali oleh `Penyewa` dan `Pemilik`.

### Atribut class

```python
nama_platform = "SewaKita"
total_user = 0
status_platform = "Aktif"
```

- `nama_platform`: nama platform yang ditampilkan dalam informasi akun.
- `total_user`: penghitung jumlah object pengguna yang dibuat melalui constructor `User`.
- `status_platform`: status umum platform.

### Atribut instance

- `_nama`: nama pengguna; menggunakan satu garis bawah sebagai penanda bahwa atribut ditujukan untuk penggunaan internal.
- `username`: username pengguna.
- `__password`: password yang menggunakan name mangling Python untuk membatasi akses langsung dari luar kelas.

### Method penting

- `__init__(nama, username, password)`: menginisialisasi data pengguna dan menambah `User.total_user`.
- `tampilkan_data()`: menampilkan nama, username, nama platform, dan memanggil `tampilkan_peran()`.
- `tampilkan_peran()`: abstract method yang harus diimplementasikan oleh kelas turunan.
- `deskripsi_akun()`: abstract method yang harus diimplementasikan oleh kelas turunan.
- `password`: property getter untuk membaca password melalui antarmuka property.
- `password` setter: menolak password kosong dan password yang panjangnya kurang dari tiga karakter.
- `ubah_status_platform(status)`: class method untuk mengubah status platform setelah memastikan status tidak kosong.
- `tampilkan_info_platform()`: class method untuk menampilkan nama platform, jumlah user, dan status.
- `validasi_username(username)`: static method yang memeriksa username tidak kosong dan tidak mengandung spasi.

## 5.2 Class `Penyewa`

`Penyewa` adalah kelas turunan `User` yang mewakili pengguna yang melakukan penyewaan.

### Atribut tambahan

- `alamat`: alamat penyewa.

### Method

- `__init__(nama, username, password, alamat)`: memanggil constructor `User` melalui `super()` dan menyimpan alamat.
- `tampilkan_peran()`: menampilkan teks `Peran : Penyewa`.
- `deskripsi_akun()`: mengembalikan kalimat yang menyebut nama penyewa dan alamatnya.

Contoh hasil `deskripsi_akun()`:

```text
Penyewa Andi tinggal di Samarinda.
```

Nama dan alamat pada contoh tersebut merupakan data ilustrasi yang dimasukkan saat program berjalan.

## 5.3 Class `Pemilik`

`Pemilik` merupakan kelas turunan `User` yang mewakili pengguna yang menawarkan barang/jasa.

### Atribut tambahan

- `nama_toko`: nama toko milik pengguna.
- `daftar_barang`: list yang menyimpan referensi objek `BarangJasa` milik pemilik tersebut.

### Method

- `__init__(nama, username, password, nama_toko)`: memanggil constructor `User`, menyimpan nama toko, dan membuat list `daftar_barang`.
- `tampilkan_peran()`: menampilkan teks `Peran : Pemilik`.
- `deskripsi_akun()`: mengembalikan deskripsi nama pemilik dan toko.
- `tambah_barang(barang)`: menambahkan objek listing ke `daftar_barang`.

Fitur upload memeriksa jenis pengguna aktif dengan `isinstance(user_aktif, Pemilik)`. Jika pengguna aktif bukan objek `Pemilik`, program menolak proses upload dan menampilkan pesan peringatan.

## 5.4 Class `BarangJasa`

`BarangJasa` mewakili sebuah barang atau jasa yang ditawarkan untuk disewa.

### Atribut class

```python
kategori_platform = "Barang dan Jasa"
total_listing = 0
status_listing = "Tersedia"
```

- `kategori_platform`: label kategori umum platform.
- `total_listing`: penghitung jumlah listing yang dibuat.
- `status_listing`: status listing yang ditampilkan program.

### Atribut instance

- `pemilik`: referensi ke objek `Pemilik.
- `nama`: nama barang/jasa.
- `kategori`: kategori listing.
- `__harga`: harga sewa per hari yang disimpan sebagai atribut private.

### Method

- `__init__(pemilik, nama, kategori, harga)`: menyimpan informasi listing dan menambah penghitung `total_listing`.
- `tampilkan_data()`: menampilkan nama, pemilik, toko, kategori, harga, dan status.
- `harga`: property getter untuk mengambil nilai harga.
- `harga` setter: menolak harga yang kurang dari atau sama dengan nol.
- `ubah_status_listing(status)`: class method untuk mengubah status listing.
- `tampilkan_info_listing()`: class method untuk menampilkan kategori, jumlah listing, dan status.
- `format_harga(harga)`: static method untuk mengubah angka menjadi format rupiah, misalnya `150000` menjadi `Rp 150.000`.
- `__str__()`: menghasilkan representasi teks objek ketika objek dicetak.
- `__lt__(other)`: memungkinkan dua listing dibandingkan dengan operator `<` berdasarkan harga.

## 5.5 Class `DetailSewa`

`DetailSewa` menyimpan rincian biaya untuk suatu transaksi penyewaan.

### Atribut

- `harga_per_hari`: harga sewa untuk satu hari.
- `durasi`: jumlah hari penyewaan.
- `__total`: total biaya yang dihitung dari harga per hari dikalikan durasi.

### Method

- `__init__(harga_per_hari, durasi)`: menyimpan harga dan durasi serta menghitung total awal.
- `total`: property getter untuk mengambil total biaya.
- `total` setter: mengubah total biaya dan menolak nilai negatif.
- `tampilkan_detail()`: menampilkan harga per hari, durasi, dan total dalam format rupiah.

Rumus yang digunakan:

```text
Total biaya = Harga sewa per hari × Durasi sewa
```

Contoh:

```text
Harga sewa per hari : Rp150.000
Durasi              : 3 hari
Total biaya         : Rp450.000
```

## 5.6 Class `Penyewaan`

`Penyewaan` merepresentasikan transaksi penyewaan antara pengguna dan listing yang dipilih.

### Atribut class

```python
nama_layanan = "Layanan Penyewaan Online"
total_penyewaan = 0
status_sistem = "Berjalan"
```

- `nama_layanan`: nama layanan yang digunakan pada informasi transaksi.
- `total_penyewaan`: penghitung transaksi yang dibuat.
- `status_sistem`: status sistem penyewaan.

### Atribut instance

- `penyewa`: objek penyewa yang melakukan transaksi.
- `barang_jasa`: objek listing yang dipilih.
- `detail`: objek `DetailSewa` yang dibuat ketika transaksi diinisialisasi.

### Method dan property

- `__init__(penyewa, barang_jasa, durasi)`: menyimpan objek penyewa dan listing, membuat `DetailSewa`, lalu menambah `total_penyewaan`.
- `tampilkan_detail()`: menampilkan penyewa, listing, pemilik, toko, dan rincian biaya.
- `total_harga`: property yang mengambil nilai dari `self.detail.total`.
- `total_harga` setter: meneruskan perubahan total ke property `DetailSewa.total`.
- `ubah_status_sistem(status)`: class method untuk mengubah status sistem setelah validasi.
- `tampilkan_info_penyewaan()`: class method untuk menampilkan nama layanan, jumlah transaksi, dan status.
- `hitung_total(harga, durasi)`: static method yang mengembalikan hasil perkalian jika harga dan durasi positif; jika tidak, mengembalikan `0`.

## 5.7 Class `RingkasanPlatform` dan `RingkasanListing`

Kedua kelas ini dipakai untuk demonstrasi duck typing.

`RingkasanPlatform` menyimpan `nama` dan `jumlah`, lalu method `tampilkan_ringkasan()` mencetak keduanya.

`RingkasanListing` menyimpan objek listing pada atribut `barang`, lalu method `tampilkan_ringkasan()` menampilkan listing tersebut.

Kedua kelas tidak perlu memiliki superclass yang sama. Yang penting, keduanya menyediakan method bernama `tampilkan_ringkasan()` yang dipanggil oleh fungsi `cetak_ringkasan(objek)`.

# 6. Penerapan Abstraksi

Abstraksi diterapkan dengan menjadikan `User` sebagai abstract class menggunakan `ABC` dan menandai method tertentu dengan `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def tampilkan_peran(self):
        raise NotImplementedError

    @abstractmethod
    def deskripsi_akun(self):
        raise NotImplementedError
```

`User` mendefinisikan perilaku yang wajib tersedia pada semua jenis pengguna, tetapi tidak menentukan isi detail kedua method tersebut. Isi perilaku disediakan oleh kelas turunannya.

### Method abstrak yang digunakan

1. `tampilkan_peran()`: setiap jenis pengguna harus dapat menampilkan perannya.
2. `deskripsi_akun()`: setiap jenis pengguna harus dapat menghasilkan deskripsi akunnya.

`Penyewa` dan `Pemilik` menyediakan implementasi masing-masing untuk kedua method tersebut. Karena itu, objek dari kedua kelas turunan dapat dibuat, sedangkan kelas `User` tidak dapat dibuat secara langsung selama abstract method-nya belum diimplementasikan.

## Bukti abstract class tidak bisa diinstansiasi

Fungsi `uji_abstraksi()` mencoba membuat objek langsung dari `User`:

```python
def uji_abstraksi():
    print("\\n=== BUKTI ABSTRACT CLASS ===")
    try:
        User("Tes", "tes", "123")
    except TypeError as error:
        print("User tidak dapat diinstansiasi:", error)
```

Python akan menghasilkan `TypeError` karena `tampilkan_peran()` dan `deskripsi_akun()` masih merupakan abstract method yang belum diimplementasikan pada `User`. Program menangkap error tersebut menggunakan `try/except`, sehingga bukti kegagalan tampil dengan rapi dan program dapat melanjutkan pengujian.

![Screenshot bukti abstract class tidak dapat diinstansiasi](screenshot_abstraksi.png)

Untuk melihat pengujian ini secara langsung, jalankan program dan pilih **menu 6 — Pengujian OOP**.

# 7. Penerapan Polimorfisme

Polimorfisme berarti satu antarmuka atau nama method dapat menghasilkan perilaku berbeda berdasarkan objek yang menggunakannya.

## 7.1 Polimorfisme melalui pewarisan

Polimorfisme melalui pewarisan terlihat pada method `tampilkan_peran()` dan `deskripsi_akun()`.

- `Penyewa.tampilkan_peran()` menampilkan peran penyewa.
- `Pemilik.tampilkan_peran()` menampilkan peran pemilik.
- `Penyewa.deskripsi_akun()` menjelaskan nama dan alamat penyewa.
- `Pemilik.deskripsi_akun()` menjelaskan nama pemilik dan nama tokonya.

Fungsi `uji_polimorfisme(pengguna)` memanggil method yang sama pada objek-objek dalam list:

```python
def uji_polimorfisme(pengguna):
    print("\\n=== POLIMORFISME VIA PEWARISAN ===")
    for user in pengguna:
        user.tampilkan_peran()
        print(user.deskripsi_akun())
```

Fungsi tidak perlu memeriksa satu per satu apakah objek adalah `Penyewa` atau `Pemilik` sebelum memanggil method tersebut. Setiap objek menjalankan implementasi yang sesuai dengan kelasnya.

## 7.2 Polimorfisme dengan duck typing

Duck typing ditunjukkan oleh fungsi berikut:

```python
def cetak_ringkasan(objek):
    objek.tampilkan_ringkasan()
```

Fungsi ini menerima objek apa pun yang menyediakan method `tampilkan_ringkasan()`. Pada program, fungsi tersebut dipanggil dengan objek `RingkasanPlatform` dan `RingkasanListing`.

- `RingkasanPlatform.tampilkan_ringkasan()` menampilkan nama platform dan jumlah pengguna.
- `RingkasanListing.tampilkan_ringkasan()` menampilkan data listing.

Kedua kelas tidak harus memiliki hubungan inheritance. Kesamaan method yang tersedia sudah cukup untuk digunakan oleh `cetak_ringkasan()`.

![Screenshot output polimorfisme dan duck typing](screenshot_polimorfisme.png)

# 8. Enkapsulasi, Getter, dan Setter

Enkapsulasi menggabungkan data dan perilaku yang mengelola data tersebut dalam kelas. Program menggunakan atribut private dan property untuk mengatur cara beberapa nilai diakses atau diubah.

| Atribut | Kelas | Pengaturan |
|---|---|---|
| `__password` | `User` | Diakses melalui property `password`; setter menolak string kosong dan panjang kurang dari tiga karakter. |
| `__harga` | `BarangJasa` | Diakses melalui property `harga`; setter menolak nilai kurang dari atau sama dengan nol. |
| `__total` | `DetailSewa` | Diakses melalui property `total`; setter menolak nilai negatif. |

### Contoh getter dan setter password

```python
@property
def password(self):
    return self.__password

@password.setter
def password(self, password):
    if not password:
        raise ValueError("Password tidak boleh kosong!")
    if len(password) < 3:
        raise ValueError("Password minimal 3 karakter!")
    self.__password = password
```

Getter digunakan untuk membaca nilai melalui property, sedangkan setter digunakan untuk mengubah nilai setelah memeriksa aturan validasi. Atribut yang menggunakan awalan dua garis bawah mengalami *name mangling* di Python; ini membantu menghindari akses tidak sengaja, tetapi bukan mekanisme keamanan password untuk aplikasi produksi.

Property `Penyewaan.total_harga` meneruskan akses ke `self.detail.total`, sehingga total transaksi dikelola melalui objek `DetailSewa`.

# 9. Instance Method, Class Method, dan Static Method

## 9.1 Instance method

Instance method menggunakan parameter `self` dan biasanya bekerja dengan data dari object tertentu.

Contoh:

- `User.tampilkan_data()`
- `Penyewa.tampilkan_peran()`
- `Pemilik.tambah_barang(barang)`
- `BarangJasa.tampilkan_data()`
- `DetailSewa.tampilkan_detail()`
- `Penyewaan.tampilkan_detail()`

Misalnya, `Penyewaan.tampilkan_detail()` membaca data dari objek transaksi tertentu, termasuk penyewa, listing, dan detail biayanya.

## 9.2 Class method

Class method menggunakan decorator `@classmethod` dan parameter `cls`. Method ini mengakses atau mengubah atribut yang berada pada tingkat kelas.

Contoh implementasi:

- `User.ubah_status_platform(status)`
- `User.tampilkan_info_platform()`
- `BarangJasa.ubah_status_listing(status)`
- `BarangJasa.tampilkan_info_listing()`
- `Penyewaan.ubah_status_sistem(status)`
- `Penyewaan.tampilkan_info_penyewaan()`

Method informasi menampilkan nilai seperti total pengguna, total listing, dan total penyewaan. Method pengubah status menolak nilai status yang kosong.

## 9.3 Static method

Static method menggunakan decorator `@staticmethod`. Method ini tidak menerima `self` maupun `cls` secara otomatis.

Contoh:

- `User.validasi_username(username)` memeriksa username.
- `BarangJasa.format_harga(harga)` memformat angka menjadi rupiah.
- `Penyewaan.hitung_total(harga, durasi)` menghitung total berdasarkan harga dan durasi jika keduanya positif.

Static method cocok untuk fungsi pendukung yang berkaitan dengan kelas, tetapi tidak perlu membaca atau mengubah keadaan suatu objek atau kelas.

# 10. Operator Overloading

Program mengimplementasikan dua special method pada kelas `BarangJasa`.

### `__str__()`

Method `__str__()` menentukan bentuk teks ketika objek dicetak.

```python
def __str__(self):
    return f"{self.nama} ({self.kategori}) - {self.format_harga(self.harga)}"
```

Contoh tampilan:

```text
Kamera (Elektronik) - Rp 150.000
```

### `__lt__(other)`

Method `__lt__()` membuat operator `<` membandingkan harga dua objek `BarangJasa`.

```python
def __lt__(self, other):
    if not isinstance(other, BarangJasa):
        return NotImplemented
    return self.harga < other.harga
```

Dengan demikian, ekspresi `barang1 < barang2` menghasilkan `True` jika harga `barang1` lebih rendah daripada harga `barang2`. Jika objek pembanding bukan `BarangJasa`, method mengembalikan `NotImplemented`.

# 11. Validasi Input dan Data

Program menggunakan beberapa validasi untuk mengurangi kesalahan saat input.

## 11.1 Username

Method `User.validasi_username(username)` mengembalikan nilai benar jika username tidak kosong dan tidak mengandung spasi. Pada registrasi, program akan meminta username kembali sampai input memenuhi aturan tersebut.

## 11.2 Password

Setter property `User.password` menolak password yang kosong atau kurang dari tiga karakter. Pemeriksaan setter berlaku saat nilai diubah melalui property tersebut.

## 11.3 Harga listing

Saat upload, input harga dikonversi menjadi integer. Program menolak input nonangka dan harga yang kurang dari atau sama dengan nol. Property setter `BarangJasa.harga` juga menolak harga yang tidak positif.

## 11.4 Durasi penyewaan

Durasi dikonversi menjadi integer dan harus lebih dari nol. Jika input bukan angka atau durasi tidak valid, program menampilkan pesan dan kembali ke menu.

## 11.5 Nomor listing

Saat penyewa memilih barang/jasa, nomor yang dimasukkan harus berada dalam rentang nomor listing yang ditampilkan. Nomor di luar rentang ditolak.

## 11.6 Total biaya

Setter `DetailSewa.total` menolak total negatif. Static method `Penyewaan.hitung_total(harga, durasi)` mengembalikan `0` jika harga atau durasi tidak positif.

# 12. Alur Penggunaan Program

Secara garis besar, program berjalan dengan urutan berikut:

```text
Program dimulai
      |
      v
Registrasi Penyewa
      |
      v
Registrasi Pemilik
      |
      v
Menu utama (pengguna aktif)
      |
      +---- Upload Barang/Jasa
      |          |
      |          v
      |    Buat objek BarangJasa
      |          |
      |          v
      |    Simpan listing ke daftar
      |
      +---- Sewa Barang/Jasa
      |          |
      |          v
      |    Pilih listing dan durasi
      |          |
      |          v
      |    Buat objek Penyewaan
      |          |
      |          v
      |    Buat DetailSewa dan hitung total
      |
      +---- Lihat data / informasi
      |
      +---- Pengujian OOP
      |
      +---- Ganti pengguna aktif
      |
      v
Keluar
```

## 12.1 Proses upload barang/jasa

1. Pengguna memilih menu 1.
2. Program memeriksa apakah pengguna aktif merupakan objek `Pemilik`.
3. Pemilik memasukkan nama barang/jasa, kategori, dan harga sewa per hari.
4. Program memvalidasi harga.
5. Program membuat objek `BarangJasa`.
6. Objek dimasukkan ke list barang umum dan ditambahkan ke `daftar_barang` milik pemilik.

## 12.2 Proses penyewaan

1. Pengguna memilih menu 2.
2. Program menampilkan listing yang tersedia pada list program.
3. Pengguna memilih nomor listing dan memasukkan durasi.
4. Program memvalidasi nomor listing serta durasi.
5. Program membuat objek `Penyewaan` menggunakan penyewa aktif, listing terpilih, dan durasi.
6. Constructor `Penyewaan` membuat objek `DetailSewa`.
7. Program menampilkan rincian transaksi dan total biaya.

![Screenshot contoh transaksi penyewaan](screenshot_penyewaan.png)

Contoh pada screenshot menggunakan harga Rp150.000 per hari dan durasi tiga hari, sehingga total biaya adalah Rp450.000.

# 13. Screenshot Output Program

Screenshot berikut dibuat dari eksekusi program dengan data contoh. Screenshot disediakan sebagai bukti tampilan terminal dan pengujian, bukan sebagai gambar ilustrasi.

## 13.1 Tampilan awal dan menu

![Screenshot tampilan awal SewaKita](screenshot_menu.png)

## 13.2 Bukti abstract class tidak bisa diinstansiasi

Ketika menu pengujian OOP dipilih, fungsi `uji_abstraksi()` mencoba membuat objek `User` secara langsung. Python menolak pembuatan objek karena abstract method `tampilkan_peran()` dan `deskripsi_akun()` belum diimplementasikan pada kelas `User`. Error ditangkap dan pesannya dicetak.

![Screenshot pengujian abstraksi](screenshot_abstraksi.png)

## 13.3 Bukti polimorfisme dan duck typing

Output menunjukkan bahwa objek `Penyewa` dan `Pemilik` menghasilkan peran dan deskripsi akun yang berbeda ketika method yang sama dipanggil. Output duck typing menunjukkan bahwa `RingkasanPlatform` dan `RingkasanListing` dapat diproses melalui `cetak_ringkasan()`.

![Screenshot pengujian polimorfisme dan duck typing](screenshot_polimorfisme.png)

## 13.4 Bukti perhitungan transaksi

Screenshot transaksi menunjukkan informasi penyewa, listing, pemilik, toko, harga per hari, durasi, dan total biaya yang dihitung oleh program.

![Screenshot detail penyewaan](screenshot_penyewaan.png)

# 14. Cara Menjalankan Program

Pastikan Python 3 sudah terpasang di komputer.

1. Simpan file `sewakita.py` di folder proyek.
2. Buka terminal atau Command Prompt di folder tersebut.
3. Jalankan perintah berikut:

```bash
python sewakita.py
```

4. Masukkan data registrasi penyewa.
5. Masukkan data registrasi pemilik.
6. Pilih menu sesuai kebutuhan.
7. Untuk melihat pengujian abstraksi, polimorfisme, duck typing, dan operator overloading, pilih menu **6**.
8. Untuk mengakhiri program, pilih menu **8**.

Di beberapa sistem, perintah menjalankan Python dapat berupa `python3 sewakita.py`.

# 15. Struktur Folder Proyek

Letakkan semua file berikut di dalam satu folder agar gambar dapat ditampilkan saat README dibuka di GitHub.

```text
SewaKita/
├── sewakita.py
├── README.md
├── class_diagram_sewakita.png
├── screenshot_menu.png
├── screenshot_abstraksi.png
├── screenshot_polimorfisme.png
└── screenshot_penyewaan.png
```

Nama file gambar di dalam README harus sama persis dengan nama file yang diunggah. Jika gambar tidak ikut diunggah atau nama filenya berbeda, GitHub tidak dapat menampilkan gambar tersebut.


## 14. Screenshot Output Program dari Pengujian Pengguna

Bagian ini berisi **screenshot asli yang dikirim dari hasil menjalankan program SewaKita**. Data yang terlihat pada screenshot merupakan input contoh saat program dijalankan. Screenshot ini melengkapi screenshot pengujian abstraksi dan polimorfisme di bagian sebelumnya.

### 14.1 Registrasi Penyewa dan Pemilik

Pada awal program, pengguna diminta mengisi data penyewa dan pemilik. Data yang dimasukkan kemudian ditampilkan pada menu dan digunakan selama sesi program berjalan.

![Screenshot registrasi penyewa dan pemilik](ss_registrasi.png)

### 14.2 Upload Barang/Jasa

Pemilik memilih menu **1 — Upload Barang/Jasa**, lalu memasukkan nama barang, kategori, dan harga sewa per hari. Program menampilkan pesan berhasil setelah listing dibuat.

![Screenshot proses upload barang dan jasa](ss_upload_barang.png)

### 14.3 Proses Penyewaan dan Perhitungan Total

Penyewa memilih menu **2 — Sewa Barang/Jasa**, memilih listing, lalu memasukkan durasi sewa. Pada contoh screenshot, harga adalah Rp100 per hari dan durasi dua hari, sehingga total yang ditampilkan adalah Rp200.

![Screenshot proses penyewaan](ss_sewa_barang.png)

### 14.4 Melihat Daftar Barang/Jasa

Menu **3 — Lihat Daftar Barang/Jasa** menampilkan listing yang tersedia, nama pemilik, nama toko, kategori, harga, dan status listing.

![Screenshot daftar barang dan jasa](ss_daftar_barang.png)

### 14.5 Melihat Data User

Menu **4 — Lihat Data User** menampilkan informasi pengguna yang sudah diregistrasi, termasuk username, platform, peran, dan deskripsi akun.

![Screenshot data pengguna](ss_data_user.png)

### 14.6 Informasi Platform

Menu **5 — Informasi Platform** menampilkan informasi platform, jumlah pengguna, status listing, jumlah listing, serta jumlah penyewaan.

![Screenshot informasi platform](ss_informasi_platform.png)

### 14.7 Pengujian Abstraksi dan Polimorfisme

Menu **6 — Pengujian OOP** menampilkan bukti bahwa kelas abstrak `User` tidak bisa diinstansiasi langsung. Output juga memperlihatkan polimorfisme melalui method `tampilkan_peran()` dan `deskripsi_akun()`, duck typing melalui `cetak_ringkasan()`, serta operator overloading pada objek `BarangJasa`.

![Screenshot pengujian OOP](ss_pengujian_oop.png)

### 14.8 Mengganti User Aktif

Menu **7 — Ganti User Aktif** menampilkan daftar pengguna dan memungkinkan pengguna memilih akun yang akan menjadi user aktif.

![Screenshot ganti user aktif](ss_ganti_user.png)

# 16. Ringkasan Penerapan OOP

| Konsep | Implementasi di SewaKita |
|---|---|
| Class | `User`, `Penyewa`, `Pemilik`, `BarangJasa`, `Penyewaan`, `DetailSewa` |
| Object | Object penyewa, pemilik, listing, transaksi, dan detail transaksi |
| Constructor | `__init__()` pada masing-masing kelas |
| Class attribute | `User.total_user`, `BarangJasa.total_listing`, `Penyewaan.total_penyewaan` |
| Instance attribute | `username`, `alamat`, `nama_toko`, `nama`, `kategori`, `durasi` |
| Encapsulation | `__password`, `__harga`, `__total` beserta property |
| Abstraction | `User(ABC)`, `@abstractmethod` |
| Abstract method | `tampilkan_peran()`, `deskripsi_akun()` |
| Inheritance | `Penyewa(User)`, `Pemilik(User)` |
| Polymorphism | Pemanggilan `tampilkan_peran()` dan `deskripsi_akun()` pada objek berbeda |
| Duck typing | `cetak_ringkasan()` dan `tampilkan_ringkasan()` |
| Instance method | `tampilkan_data()`, `tambah_barang()`, `tampilkan_detail()` |
| Class method | `tampilkan_info_platform()`, `ubah_status_platform()` dan method informasi/status lainnya |
| Static method | `validasi_username()`, `format_harga()`, `hitung_total()` |
| Getter/setter | Property `password`, `harga`, `total`, `total_harga` |
| Operator overloading | `BarangJasa.__str__()` dan `BarangJasa.__lt__()` |
| Asosiasi | `Penyewaan` mengacu pada `Penyewa` dan `BarangJasa` |
| Agregasi | `Pemilik` menyimpan daftar objek `BarangJasa` |
| Komposisi | `Penyewaan` membuat objek `DetailSewa` |

# 17. Kesimpulan

SewaKita merupakan simulasi marketplace penyewaan barang dan jasa berbasis Python CLI. Program mengorganisasikan data pengguna, listing, dan transaksi ke dalam kelas yang memiliki tanggung jawab masing-masing.

Abstraksi diterapkan melalui kelas `User` yang menggunakan `ABC` dan abstract method. Inheritance diterapkan melalui kelas `Penyewa` dan `Pemilik`. Polimorfisme terlihat ketika method yang sama menghasilkan perilaku berbeda berdasarkan jenis objek, sedangkan duck typing ditunjukkan oleh dua kelas ringkasan yang memiliki method `tampilkan_ringkasan()`.

Program juga memperlihatkan relasi UML berupa asosiasi antara `Penyewaan` dengan `Penyewa` dan `BarangJasa`, agregasi antara `Pemilik` dengan daftar `BarangJasa`, serta komposisi antara `Penyewaan` dan `DetailSewa`. Konsep enkapsulasi, property, validasi input, class method, static method, dan operator overloading melengkapi penerapan OOP pada studi kasus ini.

Dengan struktur tersebut, SewaKita dapat digunakan sebagai contoh pembelajaran OOP Python yang menunjukkan hubungan antarkelas sekaligus perilaku program yang dapat diuji langsung melalui menu terminal.
