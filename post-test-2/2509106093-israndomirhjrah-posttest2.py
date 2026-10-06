class User:

    nama_platform = "SewaKita"
    total_user = 0
    status_platform = "Aktif"

    def __init__(self, nama, username, password):
        self._nama = nama
        self.username = username
        self.__password = password
        User.total_user += 1

    def tampilkan_data(self):
        print("\n--- DATA USER ---")
        print("Nama     :", self._nama)
        print("Username :", self.username)
        print("Platform :", User.nama_platform)

    def tampilkan_peran(self):
        print("Peran    : User")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password == "":
            raise ValueError("Password tidak boleh kosong!")

        if len(password) < 3:
            raise ValueError("Password minimal 3 karakter!")

        self.__password = password

    @classmethod
    def ubah_status_platform(cls, status):
        if status == "":
            raise ValueError("Status tidak boleh kosong!")

        cls.status_platform = status

    @classmethod
    def tampilkan_info_platform(cls):
        print("\n--- INFORMASI PLATFORM ---")
        print("Nama Platform   :", cls.nama_platform)
        print("Total User      :", cls.total_user)
        print("Status Platform :", cls.status_platform)

    @staticmethod
    def validasi_username(username):
        return username != "" and " " not in username


class Penyewa(User):

    def __init__(self, nama, username, password, alamat):
        super().__init__(nama, username, password)
        self.alamat = alamat

    def tampilkan_data(self):
        print("\n--- DATA PENYEWA ---")
        print("Nama     :", self._nama)
        print("Username :", self.username)
        print("Alamat   :", self.alamat)
        print("Platform :", User.nama_platform)

    def tampilkan_peran(self):
        print("Peran    : Penyewa")


class Pemilik(User):

    def __init__(self, nama, username, password, nama_toko):
        super().__init__(nama, username, password)
        self.nama_toko = nama_toko
        self.daftar_barang = []

    def tampilkan_data(self):
        print("\n--- DATA PEMILIK ---")
        print("Nama          :", self._nama)
        print("Username      :", self.username)
        print("Nama Toko     :", self.nama_toko)
        print("Jumlah Listing:", len(self.daftar_barang))
        print("Platform      :", User.nama_platform)

    def tampilkan_peran(self):
        print("Peran    : Pemilik")

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)


class BarangJasa:

    kategori_platform = "Barang dan Jasa"
    total_listing = 0
    status_listing = "Tersedia"

    def __init__(self, pemilik, nama, kategori, harga):
        self.pemilik = pemilik
        self.nama = nama
        self.kategori = kategori
        self.__harga = harga
        BarangJasa.total_listing += 1

    def tampilkan_data(self):
        print("\n--- DATA BARANG / JASA ---")
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
        if status == "":
            raise ValueError("Status tidak boleh kosong!")

        cls.status_listing = status

    @classmethod
    def tampilkan_info_listing(cls):
        print("\n--- INFORMASI LISTING ---")
        print("Kategori       :", cls.kategori_platform)
        print("Total Listing  :", cls.total_listing)
        print("Status Listing :", cls.status_listing)

    @staticmethod
    def format_harga(harga):
        return f"Rp {harga:,.0f}".replace(",", ".")


class DetailSewa:

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
        print(
            "Harga/Hari :",
            BarangJasa.format_harga(self.harga_per_hari)
        )
        print("Durasi     :", self.durasi, "hari")
        print(
            "Total      :",
            BarangJasa.format_harga(self.__total)
        )


class Penyewaan:

    nama_layanan = "Layanan Penyewaan Online"
    total_penyewaan = 0
    status_sistem = "Berjalan"

    def __init__(self, penyewa, barang_jasa, durasi):
        self.penyewa = penyewa
        self.barang_jasa = barang_jasa

        self.detail = DetailSewa(
            barang_jasa.harga,
            durasi
        )

        Penyewaan.total_penyewaan += 1

    def tampilkan_detail(self):
        print("\n--- DETAIL PENYEWAAN ---")
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
        if total < 0:
            raise ValueError(
                "Total harga tidak boleh negatif!"
            )

        self.detail.total = total

    @classmethod
    def ubah_status_sistem(cls, status):
        if status == "":
            raise ValueError("Status tidak boleh kosong!")

        cls.status_sistem = status

    @classmethod
    def tampilkan_info_penyewaan(cls):
        print("\n--- INFORMASI PENYEWAAN ---")
        print("Layanan         :", cls.nama_layanan)
        print("Total Penyewaan :", cls.total_penyewaan)
        print("Status Sistem   :", cls.status_sistem)

    @staticmethod
    def hitung_total(harga, durasi):
        if harga <= 0 or durasi <= 0:
            return 0

        return harga * durasi


users = []
barang_jasa = []
penyewaan = []

objek_uji_dibuat = False

print("=" * 60)
print("                    SEWAKITA")
print("             SISTEM PENYEWAAN ONLINE")
print("=" * 60)

print("\n=== REGISTRASI PENYEWA ===")

nama1 = input("Nama     : ")
username1 = input("Username : ")
password1 = input("Password : ")
alamat1 = input("Alamat   : ")

while not User.validasi_username(username1):
    print(
        "Username tidak boleh kosong "
        "atau mengandung spasi!"
    )
    username1 = input("Username : ")

user1 = Penyewa(
    nama1,
    username1,
    password1,
    alamat1
)

users.append(user1)

print("\n=== REGISTRASI PEMILIK ===")

nama2 = input("Nama      : ")
username2 = input("Username  : ")
password2 = input("Password  : ")
nama_toko2 = input("Nama Toko : ")

while not User.validasi_username(username2):
    print(
        "Username tidak boleh kosong "
        "atau mengandung spasi!"
    )
    username2 = input("Username : ")

user2 = Pemilik(
    nama2,
    username2,
    password2,
    nama_toko2
)

users.append(user2)

user_aktif = user1

print("\nRegistrasi berhasil.")
print("User aktif :", user_aktif._nama)

while True:

    print("\n" + "=" * 60)
    print("                    MENU UTAMA")
    print("=" * 60)

    print("1. Upload Barang / Jasa")
    print("2. Sewa Barang / Jasa")
    print("3. Lihat Daftar Barang / Jasa")
    print("4. Lihat Data User")
    print("5. Informasi Platform")
    print("6. Pengujian OOP")
    print("7. Ganti User Aktif")
    print("8. Keluar")

    print("=" * 60)

    pilihan = input("Pilih menu : ")

    if pilihan == "1":

        print("\n=== UPLOAD BARANG / JASA ===")

        if not isinstance(user_aktif, Pemilik):
            print(
                "\nHanya Pemilik yang dapat "
                "meng-upload barang/jasa!"
            )
            continue

        nama_barang = input(
            "Nama barang/jasa : "
        )

        kategori = input(
            "Kategori         : "
        )

        while True:

            try:
                harga = int(
                    input("Harga sewa       : Rp ")
                )

                if harga <= 0:
                    print(
                        "Harga harus lebih dari 0!"
                    )
                    continue

                break

            except ValueError:
                print(
                    "Harga harus berupa angka!"
                )

        barang = BarangJasa(
            user_aktif,
            nama_barang,
            kategori,
            harga
        )

        barang_jasa.append(barang)
        user_aktif.tambah_barang(barang)

        print(
            "\nBarang/jasa berhasil di-upload!"
        )

        barang.tampilkan_data()

    elif pilihan == "2":

        if len(barang_jasa) == 0:
            print(
                "\nBelum ada barang atau jasa "
                "yang tersedia."
            )
            continue

        print("\n=== DAFTAR BARANG / JASA ===")

        for i, barang in enumerate(
            barang_jasa,
            start=1
        ):
            print(
                i,
                ".",
                barang.nama,
                "-",
                BarangJasa.format_harga(
                    barang.harga
                ),
                "/hari"
            )

        while True:

            try:
                nomor = int(
                    input(
                        "\nPilih nomor yang ingin disewa : "
                    )
                )

                if nomor < 1 or nomor > len(
                    barang_jasa
                ):
                    print(
                        "Nomor tidak tersedia!"
                    )
                    continue

                break

            except ValueError:
                print(
                    "Masukkan nomor yang benar!"
                )

        barang_dipilih = barang_jasa[
            nomor - 1
        ]

        print(
            "\nBarang/Jasa :",
            barang_dipilih.nama
        )

        print(
            "Pemilik     :",
            barang_dipilih.pemilik._nama
        )

        print(
            "Harga       :",
            BarangJasa.format_harga(
                barang_dipilih.harga
            )
        )

        while True:

            try:
                durasi = int(
                    input(
                        "Durasi sewa (hari) : "
                    )
                )

                if durasi <= 0:
                    print(
                        "Durasi harus lebih dari 0!"
                    )
                    continue

                break

            except ValueError:
                print(
                    "Durasi harus berupa angka!"
                )

        sewa = Penyewaan(
            user_aktif,
            barang_dipilih,
            durasi
        )

        penyewaan.append(sewa)

        print("\nPenyewaan berhasil!")

        sewa.tampilkan_detail()

    elif pilihan == "3":

        print(
            "\n=== DAFTAR BARANG / JASA ==="
        )

        if len(barang_jasa) == 0:
            print(
                "Belum ada barang atau jasa "
                "yang di-upload."
            )

        else:

            for i, barang in enumerate(
                barang_jasa,
                start=1
            ):
                print("\n[" + str(i) + "]")
                barang.tampilkan_data()

    elif pilihan == "4":

        print("\n=== DATA USER ===")

        for user in users:
            user.tampilkan_data()
            user.tampilkan_peran()

    elif pilihan == "5":

        User.tampilkan_info_platform()
        BarangJasa.tampilkan_info_listing()
        Penyewaan.tampilkan_info_penyewaan()

    elif pilihan == "6":

        print("\n" + "=" * 60)
        print("                 PENGUJIAN OOP")
        print("=" * 60)

        if not objek_uji_dibuat:

            barang1 = BarangJasa(
                user2,
                "Kamera Uji",
                "Barang",
                150000
            )

            barang2 = BarangJasa(
                user2,
                "Jasa Fotografi Uji",
                "Jasa",
                300000
            )

            user2.tambah_barang(barang1)
            user2.tambah_barang(barang2)

            sewa1 = Penyewaan(
                user1,
                barang1,
                2
            )

            sewa2 = Penyewaan(
                user1,
                barang2,
                3
            )

            objek_uji_dibuat = True

        print("\n1. INSTANCE METHOD")

        user1.tampilkan_data()
        user2.tampilkan_data()

        barang1.tampilkan_data()
        barang2.tampilkan_data()

        sewa1.tampilkan_detail()
        sewa2.tampilkan_detail()

        print("\n2. CLASS METHOD")

        User.ubah_status_platform(
            "Aktif"
        )

        BarangJasa.ubah_status_listing(
            "Tersedia"
        )

        Penyewaan.ubah_status_sistem(
            "Berjalan"
        )

        User.tampilkan_info_platform()
        BarangJasa.tampilkan_info_listing()
        Penyewaan.tampilkan_info_penyewaan()

        print("\n3. STATIC METHOD")

        print(
            "Username user 1 valid :",
            User.validasi_username(
                user1.username
            )
        )

        print(
            "Username user 2 valid :",
            User.validasi_username(
                user2.username
            )
        )

        print(
            "Format harga barang 1 :",
            BarangJasa.format_harga(
                barang1.harga
            )
        )

        print(
            "Total sewa barang 1 :",
            Penyewaan.hitung_total(
                barang1.harga,
                sewa1.detail.durasi
            )
        )

        print("\n4. GETTER")

        print(
            "Password user 1 :",
            user1.password
        )

        print(
            "Harga barang 1  :",
            barang1.harga
        )

        print(
            "Total sewa 1    :",
            sewa1.total_harga
        )

        print("\n5. SETTER DATA VALID")

        try:

            user1.password = "999"

            print(
                "Password baru :",
                user1.password
            )

        except ValueError as e:

            print("Error :", e)

        try:

            barang1.harga = 200000

            print(
                "Harga baru :",
                barang1.harga
            )

        except ValueError as e:

            print("Error :", e)

        try:

            sewa1.total_harga = 400000

            print(
                "Total harga baru :",
                sewa1.total_harga
            )

        except ValueError as e:

            print("Error :", e)

        print(
            "\n6. SETTER DATA TIDAK VALID"
        )

        try:

            user1.password = ""

        except ValueError as e:

            print(
                "Password :",
                e
            )

        try:

            barang1.harga = -50000

        except ValueError as e:

            print(
                "Harga :",
                e
            )

        try:

            sewa1.total_harga = -100000

        except ValueError as e:

            print(
                "Total harga :",
                e
            )

        print("\n7. INHERITANCE")

        print("Superclass : User")
        print("Subclass 1 : Penyewa")
        print("Subclass 2 : Pemilik")

        print("\nPenyewa menggunakan super():")

        print(
            "Nama :",
            user1._nama
        )

        print(
            "Alamat :",
            user1.alamat
        )

        print("\nPemilik menggunakan super():")

        print(
            "Nama :",
            user2._nama
        )

        print(
            "Nama Toko :",
            user2.nama_toko
        )

        print("\n8. RELASI UML")

        print(
            "Asosiasi  : Penyewaan berhubungan "
            "dengan Penyewa dan BarangJasa."
        )

        print(
            "Agregasi  : Pemilik memiliki "
            "daftar BarangJasa."
        )

        print(
            "Komposisi : Penyewaan memiliki "
            "objek DetailSewa."
        )

        print("\n9. JUMLAH OBJEK")

        print(
            "Jumlah User        :",
            User.total_user
        )

        print(
            "Jumlah Barang/Jasa :",
            BarangJasa.total_listing
        )

        print(
            "Jumlah Penyewaan   :",
            Penyewaan.total_penyewaan
        )

        print("\n10. STATUS CLASS")

        print(
            "Status Platform :",
            User.status_platform
        )

        print(
            "Status Listing  :",
            BarangJasa.status_listing
        )

        print(
            "Status Sistem   :",
            Penyewaan.status_sistem
        )

    elif pilihan == "7":

        print("\n=== GANTI USER AKTIF ===")

        for i, user in enumerate(
            users,
            start=1
        ):
            print(
                i,
                ".",
                user._nama,
                "-",
                type(user).__name__
            )

        try:

            nomor_user = int(
                input("Pilih user : ")
            )

            if nomor_user < 1 or nomor_user > len(users):
                print(
                    "Nomor user tidak tersedia!"
                )
                continue

            user_aktif = users[
                nomor_user - 1
            ]

            print(
                "\nUser aktif sekarang :",
                user_aktif._nama
            )

            print(
                "Tipe user           :",
                type(user_aktif).__name__
            )

        except ValueError:

            print(
                "Masukkan nomor yang benar!"
            )

    elif pilihan == "8":

        print(
            "\nTerima kasih telah "
            "menggunakan SewaKita."
        )

        break

    else:

        print(
            "\nPilihan tidak tersedia!"
        )