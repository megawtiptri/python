import sqlite3

# koneksi ke database 
konek = sqlite3.connect('data_siswa.db')
cursor = konek.cursor()

# buat tabel siswa
cursor.execute(''' CREATE TABLE IF NOT EXISTS siswa (id integer primary key autoincrement, nama text, jurusan text, kelas text)''')
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
    cursor.execute("UPDATE siswa SET nama = ?, jurusan = ?, kelas = ? WHERE id=?", (nama, jurusan, kelas, id))
    konek.commit()
    print("Data berhasil diubah")

def hapus_siswa(id):
    cursor.execute("DELETE FROM siswa WHERE id=?", (id))
    konek.commit()
    print("Data berhasil dihapus")

while True:
    print("==== Aplikasi Crud Siswa ====")
    print("================")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa")
    print("3. Ubah Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar Siswa")
    print("================")
    pilihan = input("Masukkan pilihan anda: ")
    print("================")
    if pilihan == "1":
        nama = input("Masukkan nama : ")
        jurusan = input("Masukkan jurusan :")
        kelas = input("Masukkan kelas : ")
        tambah_siswa(nama, jurusan, kelas)
    elif pilihan == "2":
        lihat_siswa()
    elif pilihan == "3":
        id = int(input("Masukkan id yang ingin diubah: "))
        nama = input("Masukkan nama baru: ")
        jurusan = input("Masukkan jurusan baru: ")
        kelas = input('Masukkan kelas baru: ')
        ubah_siswa(id, nama, jurusan, kelas)
    elif pilihan == "4":
        id = int(input("Masukkan id yang ingin dihapus: "))
        hapus_siswa(id)
    elif pilihan == "5":
        break
    else:
        print("Pilihan anda tidak sesuai")

konek.close()