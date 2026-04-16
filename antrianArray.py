# Sistem Antrian Pemesanan Makanan (Queue - FIFO)

antrian = []   # array
nomor = 1      # nomor antrian


# ENQUEUE (tambah antrian)
def enqueue():
    global nomor
    nama = input("Masukkan nama: ")
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
