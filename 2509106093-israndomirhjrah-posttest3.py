from abc import ABC, abstractmethod


class User(ABC):
    """Abstract base class untuk semua pengguna SewaKita."""
    nama_platform = "SewaKita"
    total_user = 0
    status_platform = "Aktif"

    def __init__(self, nama, username, password):
        self._nama = nama                  
        self.username = username
        self.__password = password         
        User.total_user += 1

    @abstractmethod
    def tampilkan_peran(self):
        """Setiap subclass menentukan perannya sendiri."""
        raise NotImplementedError

    @abstractmethod
    def deskripsi_akun(self):
        """Setiap subclass menyediakan deskripsi akun."""
        raise NotImplementedError

    def tampilkan_data(self):
        """Method konkret yang digunakan bersama oleh subclass."""
        print(f"Nama     : {self._nama}")
        print(f"Username : {self.username}")
        print(f"Platform : {self.nama_platform}")
        self.tampilkan_peran()

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

    @classmethod
    def ubah_status_platform(cls, status):
        if not status:
            raise ValueError("Status tidak boleh kosong!")
        cls.status_platform = status

    @classmethod
    def tampilkan_info_platform(cls):
        print("\\n--- INFORMASI PLATFORM ---")
        print("Nama Platform   :", cls.nama_platform)
        print("Total User      :", cls.total_user)
        print("Status Platform :", cls.status_platform)

    @staticmethod
    def validasi_username(username):
        return bool(username) and " " not in username


class Penyewa(User):
    def __init__(self, nama, username, password, alamat):
        super().__init__(nama, username, password)
        self.alamat = alamat

    def tampilkan_peran(self):
        print("Peran    : Penyewa")

    def deskripsi_akun(self):
        return f"Penyewa {self._nama} tinggal di {self.alamat}."


class Pemilik(User):
    def __init__(self, nama, username, password, nama_toko):
        super().__init__(nama, username, password)
        self.nama_toko = nama_toko
        self.daftar_barang = []  # agregasi: daftar menyimpan objek listing

    def tampilkan_peran(self):
        print("Peran    : Pemilik")

    def deskripsi_akun(self):
        return f"Pemilik {self._nama} mengelola toko {self.nama_toko}."

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)


class BarangJasa:
    kategori_platform = "Barang dan Jasa"
    total_listing = 0
    status_listing = "Tersedia"

    def __init__(self, pemilik, nama, kategori, harga):
        self.pemilik = pemilik              # asosiasi ke Pemilik
        self.nama = nama
        self.kategori = kategori
        self.__harga = harga
        BarangJasa.total_listing += 1

    def tampilkan_data(self):
        print("\\n--- DATA BARANG / JASA ---")
        print("Nama      :", self.nama)
        print("Pemilik   :", self.pemilik._nama)
        print("Toko      :", self.pemilik.nama_toko)
        print("Kategori  :", self.kategori)
        print("Harga     :", self.format_harga(self.__harga))
        print("Status    :", BarangJasa.status_listing)

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0!")
        self.__harga = harga

    @classmethod
    def ubah_status_listing(cls, status):
        if not status:
            raise ValueError("Status tidak boleh kosong!")
        cls.status_listing = status

    @classmethod
    def tampilkan_info_listing(cls):
        print("\\n--- INFORMASI LISTING ---")
        print("Kategori       :", cls.kategori_platform)
        print("Total Listing  :", cls.total_listing)
        print("Status Listing :", cls.status_listing)

    @staticmethod
    def format_harga(harga):
        return f"Rp {harga:,.0f}".replace(",", ".")

    def __str__(self):
        return f"{self.nama} ({self.kategori}) - {self.format_harga(self.harga)}"

    def __lt__(self, other):
        if not isinstance(other, BarangJasa):
            return NotImplemented
        return self.harga < other.harga


class DetailSewa:
    """Objek ini dibuat dan dimiliki Penyewaan (komposisi)."""
    def __init__(self, harga_per_hari, durasi):
        self.harga_per_hari = harga_per_hari
        self.durasi = durasi
        self.__total = harga_per_hari * durasi

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        if total < 0:
            raise ValueError("Total tidak boleh negatif!")
        self.__total = total

    def tampilkan_detail(self):
        print("Harga/Hari :", BarangJasa.format_harga(self.harga_per_hari))
        print("Durasi     :", self.durasi, "hari")
        print("Total      :", BarangJasa.format_harga(self.__total))


class Penyewaan:
    nama_layanan = "Layanan Penyewaan Online"
    total_penyewaan = 0
    status_sistem = "Berjalan"

    def __init__(self, penyewa, barang_jasa, durasi):
        self.penyewa = penyewa
        self.barang_jasa = barang_jasa
        self.detail = DetailSewa(barang_jasa.harga, durasi)  # komposisi
        Penyewaan.total_penyewaan += 1

    def tampilkan_detail(self):
        print("\\n--- DETAIL PENYEWAAN ---")
        print("Penyewa     :", self.penyewa._nama)
        print("Barang/Jasa :", self.barang_jasa.nama)
        print("Pemilik     :", self.barang_jasa.pemilik._nama)
        print("Toko        :", self.barang_jasa.pemilik.nama_toko)
        self.detail.tampilkan_detail()

    @property
    def total_harga(self):
        return self.detail.total

    @total_harga.setter
    def total_harga(self, total):
        self.detail.total = total

    @classmethod
    def ubah_status_sistem(cls, status):
        if not status:
            raise ValueError("Status tidak boleh kosong!")
        cls.status_sistem = status

    @classmethod
    def tampilkan_info_penyewaan(cls):
        print("\\n--- INFORMASI PENYEWAAN ---")
        print("Layanan         :", cls.nama_layanan)
        print("Total Penyewaan :", cls.total_penyewaan)
        print("Status Sistem   :", cls.status_sistem)

    @staticmethod
    def hitung_total(harga, durasi):
        if harga <= 0 or durasi <= 0:
            return 0
        return harga * durasi


# Kelas ini tidak berhubungan lewat inheritance dengan BarangJasa/DetailSewa.
# Keduanya sama-sama punya method tampilkan_ringkasan (duck typing).
class RingkasanPlatform:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def tampilkan_ringkasan(self):
        print(f"{self.nama}: {self.jumlah}")


def cetak_ringkasan(objek):
    """Duck typing: menerima objek apa pun yang punya method ini."""
    objek.tampilkan_ringkasan()


class RingkasanListing:
    def __init__(self, barang):
        self.barang = barang

    def tampilkan_ringkasan(self):
        print("Listing:", self.barang)


def uji_abstraksi():
    print("\\n=== BUKTI ABSTRACT CLASS ===")
    try:
        User("Tes", "tes", "123")
    except TypeError as error:
        print("User tidak dapat diinstansiasi:", error)


def uji_polimorfisme(pengguna):
    print("\\n=== POLIMORFISME VIA PEWARISAN ===")
    for user in pengguna:
        user.tampilkan_peran()  # method sama, hasil berbeda
        print(user.deskripsi_akun())


def uji_duck_typing(barang):
    print("\\n=== DUCK TYPING ===")
    cetak_ringkasan(RingkasanPlatform("SewaKita", User.total_user))
    cetak_ringkasan(RingkasanListing(barang))


def main():
    users = []
    barang_jasa = []
    penyewaan = []

    print("=" * 55)
    print("SEWAKITA - SISTEM PENYEWAAN ONLINE")
    print("=" * 55)

    print("\\n=== REGISTRASI PENYEWA ===")
    nama = input("Nama     : ")
    username = input("Username : ")
    while not User.validasi_username(username):
        print("Username tidak boleh kosong atau mengandung spasi!")
        username = input("Username : ")
    password = input("Password : ")
    alamat = input("Alamat   : ")
    penyewa = Penyewa(nama, username, password, alamat)
    users.append(penyewa)

    print("\\n=== REGISTRASI PEMILIK ===")
    nama = input("Nama      : ")
    username = input("Username  : ")
    while not User.validasi_username(username):
        print("Username tidak boleh kosong atau mengandung spasi!")
        username = input("Username : ")
    password = input("Password  : ")
    nama_toko = input("Nama Toko : ")
    pemilik = Pemilik(nama, username, password, nama_toko)
    users.append(pemilik)
    user_aktif = penyewa

    while True:
        print("\\n" + "=" * 55)
        print("MENU UTAMA | User aktif:", user_aktif._nama)
        print("1. Upload Barang/Jasa")
        print("2. Sewa Barang/Jasa")
        print("3. Lihat Daftar Barang/Jasa")
        print("4. Lihat Data User")
        print("5. Informasi Platform")
        print("6. Pengujian OOP (ABC, polimorfisme, duck typing)")
        print("7. Ganti User Aktif")
        print("8. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if not isinstance(user_aktif, Pemilik):
                print("Hanya Pemilik yang dapat meng-upload barang/jasa!")
                continue
            nama_barang = input("Nama barang/jasa : ")
            kategori = input("Kategori         : ")
            try:
                harga = int(input("Harga sewa/hari  : Rp "))
                if harga <= 0:
                    print("Harga harus lebih dari 0!")
                    continue
            except ValueError:
                print("Harga harus berupa angka!")
                continue
            barang = BarangJasa(user_aktif, nama_barang, kategori, harga)
            barang_jasa.append(barang)
            user_aktif.tambah_barang(barang)
            print("Berhasil di-upload:", barang)

        elif pilihan == "2":
            if not barang_jasa:
                print("Belum ada barang/jasa tersedia.")
                continue
            for i, barang in enumerate(barang_jasa, 1):
                print(f"{i}. {barang}")
            try:
                nomor = int(input("Pilih nomor barang/jasa: "))
                if not 1 <= nomor <= len(barang_jasa):
                    print("Nomor tidak tersedia!")
                    continue
                durasi = int(input("Durasi sewa (hari): "))
                if durasi <= 0:
                    print("Durasi harus lebih dari 0!")
                    continue
            except ValueError:
                print("Masukkan angka yang benar!")
                continue
            sewa = Penyewaan(user_aktif, barang_jasa[nomor - 1], durasi)
            penyewaan.append(sewa)
            print("Penyewaan berhasil.")
            sewa.tampilkan_detail()

        elif pilihan == "3":
            if not barang_jasa:
                print("Belum ada barang/jasa yang di-upload.")
            else:
                for i, barang in enumerate(barang_jasa, 1):
                    print(f"\\n[{i}] {barang}")
                    barang.tampilkan_data()

        elif pilihan == "4":
            for user in users:
                user.tampilkan_data()
                print(user.deskripsi_akun())

        elif pilihan == "5":
            User.tampilkan_info_platform()
            BarangJasa.tampilkan_info_listing()
            Penyewaan.tampilkan_info_penyewaan()

        elif pilihan == "6":
            uji_abstraksi()
            uji_polimorfisme(users)
            if barang_jasa:
                uji_duck_typing(barang_jasa[0])
            else:
                contoh = BarangJasa(pemilik, "Kamera contoh", "Barang", 150000)
                # Listing uji juga ditambahkan ke daftar pemilik agar agregasi tampak nyata.
                pemilik.tambah_barang(contoh)
                barang_jasa.append(contoh)
                uji_duck_typing(contoh)
            print("\\n=== OPERATOR OVERLOADING ===")
            print("Representasi string:", barang_jasa[0])
            if len(barang_jasa) >= 2:
                lebih_murah = barang_jasa[0] < barang_jasa[1]
                print("Listing pertama lebih murah dari kedua:", lebih_murah)
            else:
                print("Perbandingan harga dengan dirinya sendiri:",
                      barang_jasa[0] < barang_jasa[0])

        elif pilihan == "7":
            for i, user in enumerate(users, 1):
                print(f"{i}. {user._nama} - {user.username}")
            try:
                nomor = int(input("Pilih user: "))
                if not 1 <= nomor <= len(users):
                    print("Nomor user tidak tersedia!")
                    continue
                user_aktif = users[nomor - 1]
            except ValueError:
                print("Masukkan nomor yang benar!")

        elif pilihan == "8":
            print("Terima kasih telah menggunakan SewaKita.")
            break
        else:
            print("Pilihan tidak tersedia!")


if __name__ == "__main__":
    main()
