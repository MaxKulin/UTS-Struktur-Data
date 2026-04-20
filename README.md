# UTS-Struktur-Data

I Gusti Ngurah Ketut Puja Bagus Permana - 2501010021 - MaxKulin

Zein Ahmad - 2501010360 - jennnod

Wayan Bayu Kusumadinatha - 2501010359 - uncrownedbay

BAB I

1.1 Rumusan Masalah

Berdasarkan studi kasus sistem antrian pemesanan makanan, maka dapat dirumuskan beberapa permasalahan sebagai berikut:
  1. Bagaimana struktur data queue dapat digunakan untuk mengelola antrian pelanggan secara teratur dan efisien?
  2. Bagaimana cara mengimplementasikan operasi dasar queue seperti enqueue, dequeue, peek, dan display dalam sebuah program Python?
  3. Bagaimana sistem antrian yang dibuat mampu menyelesaikan permasalahan nyata seperti pengelolaan pemesanan makanan agar tidak terjadi kekacauan urutan layanan?
     
1.2 Solusi

Untuk menyelesaikan permasalahan, dibuat sistem antrian sederhana menggunakan struktur data queue berbasis list Python dengan metode FIFO (First In First Out), sehingga pelanggan yang datang lebih dahulu akan dilayani terlebih dahulu.

Fitur utama:

* Enqueue → menambah pelanggan ke antrian
* Dequeue → memanggil pelanggan sesuai urutan
* Peek → melihat antrian terdepan
* Display → menampilkan seluruh antrian

Manfaat:

* Menjaga keteraturan pelayanan
* Menghindari kesalahan urutan
* Meningkatkan efisiensi sistem antrian

BAB II

2.1 Landasan Teori

  Struktur data adalah cara untuk mengatur data dalam memori komputer sehingga dapat dengan mudah diakses dan digunakan oleh program komputer. Setiap struktur data memiliki format khusus untuk mengatur, memproses, mengambil dan menyimpan data, memungkinkan data untuk dimanipulasi dengan berbagai cara oleh pengguna dan sistem computer. https://builtin.com/data-science/python-data-structures
  
  Queue dapat dianalogikan sebagai antrian di bioskop, di mana orang yang pertama kali masuk ke antrian adalah orang pertama yang dilayani. Dengan kata lain, elemen yang pertama kali dimasukkan akan menjadi elemen pertama yang keluar. Stack adalah salah satu struktur data yang paling umum dijumpai dalam pemrograman. Cara kerja stack dapat diibaratkan seperti tumpukan buku. Ketika kita ingin menambah buku ke dalam tumpukan, kita hanya bisa menambahnya di bagian atas. Begitu juga ketika ingin mengambil buku, kita harus mengambil yang paling atas terlebih dahulu.Mengenal Stack dan Queue Serta Perbedaan dan Contohnya - Lawencon
  
  Algoritma FIFO ( First In First Out) adalah metode pengelolaan data atau barang yang mengikuti prinsip “Yang Pertama Masuk, Yang Pertama Keluar.” Dalam konteks algoritma, FIFO digunakan untuk menjadwalkan dan mengelola proses atau data dengan cara memberikan prioritas pada yang pertama kali tiba.https://fikti.umsu.ac.id/algoritma-first-in-first-out-fifo-pengertian-cara-kerja-beserta-contohnya/ . LIFO (Last In First Out) merupakan metode pengelolaan barang yang berkebalikan dengan FIFO. Manajemen persediaan dengan metode ini dilakukan dengan cara barang yang terakhir masuk ke gudang adalah barang pertama yang akan keluar dari gudang untuk dijual. https://www.transcon-indonesia.com/id/blog/metode-fifo-fefo-lifo-dan-average .
  
  Implementasi queue dapat dilakukan menggunakan beberapa cara, salah satunya adalah menggunakan array (list dalam Python). Pada metode ini, data disimpan dalam urutan

indeks, dimana:
    Penambahan data dilakukan di bagian akhir array
    Penghapusan data dilakukan di bagian awal array
  Operasi utama dalam queue meliputi:
      Enqueue: menambahkan elemen ke antrian
      Dequeue: menghapus elemen dari antrian
      Peek: melihat elemen terdepan
      Display: menampilkan seluruh isi antrian
Dengan menggunakan queue, sistem dapat berjalan secara teratur dan adil karena mengikuti urutan kedatangan.

BAB III

3.1 Desain Sistem dan Implementasi

Dalam sistem ini digunakan metode Queue (FIFO) untuk mengatur antrian pemesananmakanan. Berikut adalah pseudocode dari sistem yang dibuat:
```
Mulai
Buat array antrian
Set nomor = 1

Ulangi:
    Tampilkan menu:
        1. Enqueue (Tambah Antrian)
        2. Dequeue (Panggil Antrian)
        3. Peek (Lihat Antrian Depan)
        4. Display (Tampilkan Semua)
        5. Keluar

    Input pilihan

    Jika pilihan = 1:
        Input nama
        Input pesanan
        Tambahkan ke array antrian
        Tambah nomor

    Jika pilihan = 2:
        Jika antrian kosong:
            Tampilkan "Antrian kosong"
        Jika tidak:
            Hapus data paling depan

    Jika pilihan = 3:
        Tampilkan data paling depan

    Jika pilihan = 4:
        Tampilkan semua isi antrian

    Jika pilihan = 5:
        Selesai
```
### **3.2 Alur Sistem (Input → Proses → Output)**

#### **🔹 Input**

* Nama pelanggan
* Pesanan makanan
* Pilihan menu

#### **🔹 Proses**

* **Enqueue** → Menambahkan data pelanggan ke dalam antrian
* **Dequeue** → Menghapus data pelanggan dari bagian depan antrian
* **Peek** → Melihat data pelanggan yang berada di posisi terdepan
* **Display** → Menampilkan seluruh data antrian

#### **🔹 Output**

* Nomor antrian (contoh: A001, A002, ...)
* Informasi pelanggan (nama dan pesanan)
* Daftar seluruh antrian

#### **🔄 Alur Singkat Sistem**

```id="ipo123"
Input data pelanggan → 
Diproses menggunakan operasi queue (FIFO) → 
Output ditampilkan → 
Kembali ke menu sampai pengguna memilih keluar
```
    
3.3 Sistem Antrian Pemesanan Makanan (Queue - FIFO)
```
antrian = []  # array
nomor = 1     # nomor antrian

# ENQUEUE (tambah antrian)
def enqueue():
    global nomor
    nama = input("Masukkan nama pelanggan: ")
    pesanan = input("Masukkan pesanan: ")
    nomor_antrian = f"A{nomor:03}"  # format A001, A002
    data = [nomor_antrian, nama, pesanan]
    antrian.append(data)
    print(f"Nomor antrian kamu: {nomor_antrian}")
    nomor += 1

# DEQUEUE (layani antrian)
def dequeue():
    if len(antrian) == 0:
        print("Antrian kosong")
    else:
        data = antrian.pop(0)
        print(f"Memanggil {data[0]} - {data[1]} ({data[2]})")

# PEEK (lihat depan)
def peek():
    if len(antrian) == 0:
        print("Antrian kosong")
    else:
        data = antrian[0]
        print(f"Antrian terdepan: {data[0]} - {data[1]} ({data[2]})")

# DISPLAY (tampilkan semua)
def display():
    if len(antrian) == 0:
        print("Antrian kosong")
    else:
        print("\nDaftar Antrian:")
        for data in antrian:
            print(f"{data[0]} - {data[1]} ({data[2]})")

# MENU UTAMA
while True:
    print("\n=== SISTEM ANTRIAN MAKANAN ===")
    print("1. Pesan makanan (Enqueue)")
    print("2. Panggil antrian (Dequeue)")
    print("3. Lihat antrian terdepan (Peek)")
    print("4. Tampilkan semua antrian (Display)")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        enqueue()
    elif pilihan == "2":
        dequeue()
    elif pilihan == "3":
        peek()
    elif pilihan == "4":
        display()
    elif pilihan == "5":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")

```
BAB IV
4.1 Kesimpulan

• Rumusan masalah telah berhasil diselesaikan dengan menggunakan konsep queue untuk mengatur antrian pelanggan.

• Sistem yang dibuat telah berjalan sesuai dengan teori, yaitu menggunakan prinsip FIFO di mana pelanggan yang datang lebih dulu akan dilayani terlebih dahulu.

• Penggunaan queue sangat bermanfaat dalam kasus pemesanan makanan karena dapat menjaga keteraturan, menghindari kesalahan urutan, serta meningkatkan efisiensi pelayanan.
