class User:

    nama_platform = "SewaKita"
    total_user = 0
    status_platform = "Aktif"

    def __init__(self, nama, username, password):
        self.nama = nama
        self.username = username
        self.__password = password
        User.total_user += 1

    def tampilkan_data(self):
        print("\n--- DATA USER ---")
        print("Nama     :", self.nama)
        print("Username :", self.username)
        print("Platform :", User.nama_platform)

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
        print("\nNama      :", self.nama)
        print("Pemilik   :", self.pemilik.nama)
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


class Penyewaan:

    nama_layanan = "Layanan Penyewaan Online"
    total_penyewaan = 0
    status_sistem = "Berjalan"

    def __init__(self, penyewa, barang_jasa, durasi):
        self.penyewa = penyewa
        self.barang_jasa = barang_jasa
        self.durasi = durasi
        self.__total_harga = barang_jasa.harga * durasi
        Penyewaan.total_penyewaan += 1

    def tampilkan_detail(self):
        print("\n--- DETAIL PENYEWAAN ---")
        print("Penyewa      :", self.penyewa.nama)
        print("Barang/Jasa  :", self.barang_jasa.nama)
        print(
            "Harga/Hari   :",
            BarangJasa.format_harga(self.barang_jasa.harga)
        )
        print("Durasi       :", self.durasi, "hari")
        print(
            "Total Harga  :",
            BarangJasa.format_harga(self.__total_harga)
        )

    @property
    def total_harga(self):
        return self.__total_harga

    @total_harga.setter
    def total_harga(self, total):
        if total < 0:
            raise ValueError("Total harga tidak boleh negatif!")

        self.__total_harga = total

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
print("              SEWAKITA")
print("        SISTEM PENYEWAAN ONLINE")
print("=" * 60)

print("\n=== REGISTRASI USER 1 ===")

nama1 = input("Nama     : ")
username1 = input("Username : ")
password1 = input("Password : ")

while not User.validasi_username(username1):
    print("Username tidak boleh kosong atau mengandung spasi!")
    username1 = input("Username : ")

user1 = User(nama1, username1, password1)
users.append(user1)

print("\n=== REGISTRASI USER 2 ===")

nama2 = input("Nama     : ")
username2 = input("Username : ")
password2 = input("Password : ")

while not User.validasi_username(username2):
    print("Username tidak boleh kosong atau mengandung spasi!")
    username2 = input("Username : ")

user2 = User(nama2, username2, password2)
users.append(user2)

user_aktif = user1

print("\nRegistrasi berhasil.")
print("User aktif :", user_aktif.nama)

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
    print("7. Keluar")
    print("=" * 60)

    pilihan = input("Pilih menu : ")

    if pilihan == "1":

        print("\n=== UPLOAD BARANG / JASA ===")

        nama_barang = input("Nama barang/jasa : ")
        kategori = input("Kategori         : ")

        while True:
            try:
                harga = int(input("Harga sewa       : Rp "))

                if harga <= 0:
                    print("Harga harus lebih dari 0!")
                    continue

                break

            except ValueError:
                print("Harga harus berupa angka!")

        barang = BarangJasa(
            user_aktif,
            nama_barang,
            kategori,
            harga
        )

        barang_jasa.append(barang)

        print("\nBarang/jasa berhasil di-upload!")
        barang.tampilkan_data()

    elif pilihan == "2":

        if len(barang_jasa) == 0:
            print("\nBelum ada barang atau jasa yang tersedia.")
            continue

        print("\n=== DAFTAR BARANG / JASA ===")

        for i, barang in enumerate(barang_jasa, start=1):
            print(
                i,
                ".",
                barang.nama,
                "-",
                BarangJasa.format_harga(barang.harga),
                "/hari"
            )

        while True:
            try:
                nomor = int(
                    input("\nPilih nomor yang ingin disewa : ")
                )

                if nomor < 1 or nomor > len(barang_jasa):
                    print("Nomor tidak tersedia!")
                    continue

                break

            except ValueError:
                print("Masukkan nomor yang benar!")

        barang_dipilih = barang_jasa[nomor - 1]

        print("\nBarang/Jasa :", barang_dipilih.nama)
        print("Pemilik     :", barang_dipilih.pemilik.nama)
        print(
            "Harga       :",
            BarangJasa.format_harga(barang_dipilih.harga)
        )

        while True:
            try:
                durasi = int(
                    input("Durasi sewa (hari) : ")
                )

                if durasi <= 0:
                    print("Durasi harus lebih dari 0!")
                    continue

                break

            except ValueError:
                print("Durasi harus berupa angka!")

        sewa = Penyewaan(
            user_aktif,
            barang_dipilih,
            durasi
        )

        penyewaan.append(sewa)

        print("\nPenyewaan berhasil!")
        sewa.tampilkan_detail()

    elif pilihan == "3":

        print("\n=== DAFTAR BARANG / JASA ===")

        if len(barang_jasa) == 0:
            print("Belum ada barang atau jasa yang di-upload.")

        else:
            for i, barang in enumerate(barang_jasa, start=1):
                print("\n[" + str(i) + "]")
                barang.tampilkan_data()

    elif pilihan == "4":

        print("\n=== DATA USER ===")

        for user in users:
            user.tampilkan_data()

    elif pilihan == "5":

        User.tampilkan_info_platform()
        BarangJasa.tampilkan_info_listing()
        Penyewaan.tampilkan_info_penyewaan()

    elif pilihan == "6":

        print("\n" + "=" * 60)
        print("              PENGUJIAN OOP")
        print("=" * 60)

        if not objek_uji_dibuat:

            barang1 = BarangJasa(
                user1,
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

            sewa1 = Penyewaan(
                user1,
                barang1,
                2
            )

            sewa2 = Penyewaan(
                user2,
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

        User.ubah_status_platform("Aktif")
        BarangJasa.ubah_status_listing("Tersedia")
        Penyewaan.ubah_status_sistem("Berjalan")

        User.tampilkan_info_platform()
        BarangJasa.tampilkan_info_listing()
        Penyewaan.tampilkan_info_penyewaan()

        print("\n3. STATIC METHOD")

        print(
            "Username user 1 valid :",
            User.validasi_username(user1.username)
        )

        print(
            "Username user 2 valid :",
            User.validasi_username(user2.username)
        )

        print(
            "Format harga barang 1 :",
            BarangJasa.format_harga(barang1.harga)
        )

        print(
            "Total sewa barang 1 :",
            Penyewaan.hitung_total(
                barang1.harga,
                sewa1.durasi
            )
        )

        print("\n4. GETTER")

        print("Password user 1 :", user1.password)
        print("Harga barang 1  :", barang1.harga)
        print("Total sewa 1    :", sewa1.total_harga)

        print("\n5. SETTER DATA VALID")

        try:
            user1.password = "999"
            print("Password baru :", user1.password)
        except ValueError as e:
            print("Error :", e)

        try:
            barang1.harga = 200000
            print("Harga baru :", barang1.harga)
        except ValueError as e:
            print("Error :", e)

        try:
            sewa1.total_harga = 400000
            print("Total harga baru :", sewa1.total_harga)
        except ValueError as e:
            print("Error :", e)

        print("\n6. SETTER DATA TIDAK VALID")

        try:
            user1.password = ""
        except ValueError as e:
            print("Password :", e)

        try:
            barang1.harga = -50000
        except ValueError as e:
            print("Harga :", e)

        try:
            sewa1.total_harga = -100000
        except ValueError as e:
            print("Total harga :", e)

        print("\n7. JUMLAH OBJEK")

        print("Jumlah User        :", len(users))
        print(
            "Jumlah Barang/Jasa :",
            BarangJasa.total_listing
        )
        print(
            "Jumlah Penyewaan   :",
            Penyewaan.total_penyewaan
        )

        print("\n8. STATUS CLASS")

        print("Status Platform :", User.status_platform)
        print("Status Listing  :", BarangJasa.status_listing)
        print("Status Sistem   :", Penyewaan.status_sistem)

    elif pilihan == "7":

        print("\nTerima kasih telah menggunakan SewaKita.")
        break

    else:

        print("\nPilihan tidak tersedia!")