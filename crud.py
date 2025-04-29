import sqlite3

# koneksi ke database
konek = sqlite3.connect('data_siswa.db')
cursor = konek.cursor()

# buat tabel siswa
cursor.execute(''' CREATE TABLE IF NOT EXISTS siswa (id integer primary key autoincrement, nama text, jurusan texs, kelas texs) ''')
konek.commit()

# fungsi untuk menambah siswa
def tambah_siswa(nama, jurusan, kelas):
    cursor.execute("INSERT INTO siswa (nama, jurusan, kelas) VALUES (?, ?, ?)", (nama, jurusan, kelas))
    konek.commit()
    print("Data berhasil disimpan")

def lihat_siswa():
    cursor.execute("SELECT * FROM siswa")
    data = cursor.fetchall()
    for row in data:
        print(row)

def ubah_siswa(id, nama, jurusan, kelas):
    cursor.execute("UPDATE siswa SET nama=?, jurusan=?, kelas=? WHERE id=?", (nama,jurusan,kelas,id))
    konek.commit()
    print("Data Berhasil di ubah")

def hapus_siswa(id):
    cursor.execute("DELETE FROM siswa WHERE id=?",(id,))
    konek.commit()
    print("Data Berhasil dihapus")

while True:
    print("==== Aplikasi CRUD Siswa ====")
    print("==========")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa")
    print("3. Ubah Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")
    print("==========")
    pilihan = input("Masukan pilihan Anda : ")
    print("==========")
    if pilihan == "1":
        nama = input("Masukan Nama : ")
        jurusan = input("Masukan Jurusan : ")
        kelas = input("Masukan kelas : ")
        tambah_siswa(nama, jurusan, kelas)
    elif pilihan == "2":
        lihat_siswa()
    elif pilihan == "3":
        id = int(input("Masukan id yang ingin diubah : "))
        nama = input("Masukan Nama Baru : ")
        jurusan = input("Masukan JUrusan Baru ")
        kelas = input("Masukan kelas baru : ")
        ubah_siswa(id, nama, jurusan, kelas)
    elif pilihan == "4":
        id = int(input("Masukan id yang ingin dihapus : "))
        hapus_siswa(id)
    elif pilihan == "5":
        break
    else:
        print("Pilihan Anda tidak sesuai")

konek.close()