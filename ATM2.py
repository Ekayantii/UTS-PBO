saldou = 0
saldot = 0


print('Selamat Datang Di ATM Ekayanti')

print('01. Informasi Saldo')
print('02. Tambah Saldo')
print('03. Ambil Saldo')
print('04. Keluar')
print()

menu = input('Silahkan pilih menu yang anda inginkan : ')
print('=================================================================')

if menu == '1':
    print(f"Saldo umum anda saat ini adalah : {saldou}")
    print(f"Saldo Tabungan anda saat ini adalah : {saldot}")
    print('=================================================================')
elif menu =='2':
    print("Pilih penyimpanan")
    print('1. Umum')
    print('2. Tabungan')
    print('=================================================================')
    menu2=int(input("Pilihan : "))
    if menu2==1:
        setor = int(input("Silahkan Masukan Jumlah Yang Diinginkan : "))
        saldou = setor + saldou
        print()
        print(f"Sisa Saldo Anda : {saldou}")
        print('=================================================================')
    elif menu2==2:
        setor = int(input("Silahkan Masukan Jumlah Yang Diinginkan : "))
        saldot = setor + saldot
        print()
        print(f"Sisa Saldo Anda : {saldot}")
        print('=================================================================')
elif menu =='3':
    print("Pilih penyimpanan")
    print('1. Umum')
    print('2. Tabungan')
    print('=================================================================')
    menu2=int(input("Pilihan : "))
    if menu2==1:
        setor = int(input("Silahkan Masukan Jumlah Yang Diinginkan : "))
        saldou = saldou - setor
        print()
        print(f"Sisa Saldo Anda : {saldou}")
        print('=================================================================')
    elif menu2==2:
        setor = int(input("Silahkan Masukan Jumlah Yang Diinginkan : "))
        saldot = saldot - setor
        print()
        print(f"Sisa Saldo Anda : {saldot}")
        print('=================================================================')
elif menu == '4':
    print("Terimakasih Telah menggunakan jasa Kami")