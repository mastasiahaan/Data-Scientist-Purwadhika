#DATA KARYAWAN UNIVERSITAS PURWADHIKA
#MASTA SIAHAAN (JCDSOL-012 C)

dataKaryawan = [
    {
        'NIKP' : '123001',
        'Nama' : 'Ilman',
        'Jabatan' : 'Dekan',
        'Fakultas' : 'Ilmu Hukum'
    },
    {
        'NIKP' : '123002',
        'Nama' : 'Abidin',
        'Jabatan' : 'Dosen',
        'Fakultas' : 'Ilmu Hukum'
    },
    {
        'NIKP' : '123003',
        'Nama' : 'Muhammad',
        'Jabatan' : 'Tendik',
        'Fakultas' : 'Ilmu Hukum'
    }
]   

# FITUR READ
def showData():#untuk menampilkan seluruh data
    print('========= Data Seluruh Karyawan Universitas Purwadhika =========\n')
    print('.===============================================================.')
    print('|NIKP    \t| Nama     \t| Jabatan\t| Fakultas\t|')
    print('.===============================================================.')
    for karyawan in dataKaryawan:
        print('|{}  \t| {}    \t| {}   \t| {}\t|'.format(karyawan['NIKP'], karyawan['Nama'], karyawan['Jabatan'], karyawan['Fakultas']))
        print('.---------------------------------------------------------------.')
    print('\n')

def cariData():#untuk mencari data
    print('''
 ===================== CARI DATA KARYAWAN =======================         
.================================================================.
| Pilih kategori pencarian berdasarkan:                          |
| [1] NIKP                                                       |
| [2] Nama                                                       |
| [3] Jabatan                                                    |
| [4] Fakultas                                                   |
.================================================================.          
          ''')
    kategori = input('Masukkan kategori pencarian ([1] / [2] / [3] / [4]): ')
    while True:
        if kategori == '1':
            keyword = input('Masukkan NIKP karyawan: ')
            if keyword.isdigit():
                hasil_pencarian = [karyawan for karyawan in dataKaryawan if keyword in karyawan['NIKP']]
                break
            else:
                print("'Masukkan NIKP dengan menggunakan angka(0-9)'")
        elif kategori == '2':
            keyword = input('Masukkan nama karyawan: ')
            if keyword.isalpha():
                hasil_pencarian = [karyawan for karyawan in dataKaryawan if keyword.lower() in karyawan['Nama'].lower()]
                break
            else:
                print("'Masukkan nama dengan menggunakan huruf saja'")    
        elif kategori == '3':
            keyword = input('Masukkan jabatan karyawan: ')
            if keyword.isalpha():
                hasil_pencarian = [karyawan for karyawan in dataKaryawan if keyword.lower() in karyawan['Jabatan'].lower()]
                break
            else:
                print("'Masukkan jabatann karyawan dengan menggunakan huruf saja'")
        elif kategori == '4':
            keyword = input('Masukkan fakultas karyawan: ')
            if keyword.isalpha():
                hasil_pencarian = [karyawan for karyawan in dataKaryawan if keyword.lower() in karyawan['Fakultas'].lower()]
                break
            else:
                print("'Masukkan nama Fakultas dengan menggunakan huruf saja'") 
        else:
            print('Kategori tidak valid!')
            break
    
    if len(hasil_pencarian) > 0:
        print(f"Hasil pencarian untuk '{keyword}':")
        print('.===============================================================.')
        print('|NIKP    \t| Nama     \t| Jabatan\t| Fakultas\t|')
        print('.===============================================================.')
        for karyawan in hasil_pencarian:
            print('|{}  \t| {}    \t| {}   \t| {}\t|'.format(karyawan['NIKP'], karyawan['Nama'], karyawan['Jabatan'], karyawan['Fakultas']))
        print('.---------------------------------------------------------------.\n')
    else:
        print(f"Tidak ada karyawan dengan pencarian '{keyword}'")
        verifikasi = input("Apakah anda ingin mencari data karyawan lain? ([Y]/[N]): ")
        if verifikasi.upper() == 'Y':
            cariData()
        elif verifikasi.upper() == 'N':
            return
        else:
            print('Pilihan tidak valid. Silahkan coba lagi. ([Y]/[N])')

#FITUR CREATE
def inputData():
    while True:
        print('''
 ================= TAMBAH DATA KARYAWAN BARU ====================
|1. Tambahkan Data Karyawan Baru Universitas Purwadhika          |
|2. Kembali ke Menu Utama                                        |
 ================================================================
              ''')
        pilihan = input('Ketik submenu yang ingin anda pilih ([1]/[2]): ')
        if pilihan == '1':
            print(' ================= TAMBAH DATA KARYAWAN BARU =====================')
            while True:
                nikp = input("Masukkan NIKP karyawan baru: ")
                if nikp.isdigit():
                    for karyawan in dataKaryawan:
                        if karyawan['NIKP'] == nikp:
                            print("NIKP sudah ada, silakan masukkan NIKP yang berbeda")
                            break
                    else:
                        break
                else:
                    print("'Masukkan NIKP dengan menggunakan angka(0-9)'")

            while True:
                nama = input("Masukkan nama karyawan baru: ")
                if nama.isalpha():
                    break
                else:
                    print("'Masukkan nama dengan menggunakan huruf saja'")
                    
            while True:    
                jabatan = input("Masukkan jabatan karyawan baru: ")
                if jabatan.isalpha():
                    break         
                else:
                    print("'Masukkan jabatann karyawan dengan menggunakan huruf saja'")
            while True:    
                fakultas = input("Masukkan fakultas karyawan baru: ")
                if fakultas.isalpha():
                    break
                else:
                    print("'Masukkan nama Fakultas dengan menggunakan huruf saja'")

            karyawanBaru = {
                'NIKP' : nikp,
                'Nama' : nama.capitalize(),
                'Jabatan' : jabatan.capitalize(),
                'Fakultas' : fakultas.capitalize()
                        }
            print('====[Data yang anda masukkan valid!]====')
            print('Data Karyawan yang ingin anda tambahkan adalah:')
            print(f"NIKP\t\t: {karyawanBaru['NIKP']}")
            print(f"Nama\t\t: {karyawanBaru['Nama']}")
            print(f"Jabatan\t\t: {karyawanBaru['Jabatan']}")
            print(f"Fakultas\t: {karyawanBaru['Fakultas']}\n")

            while True:
                cekDataBaru = input('Apakah anda ingin menambahkan Data Karyawan Ini?([Y]/[N]): ').upper()
                if cekDataBaru.upper() == 'Y':
                    dataKaryawan.append(karyawanBaru)
                    showData()
                    print('============== Data Karyawan Baru berhasil ditambahkan =============')
                    break
                elif cekDataBaru.upper() == 'N':
                    showData()
                    print('=========== Data Karyawan Baru gagal ditambahkan ===========')
                    break
                else:
                    print('============ [Masukkan Pilihan Yang Benar [Y] / [N] =============')
        elif pilihan == '2':
            konfirmasi = input('Apakah anda ingin kembali ke menu utama? ([Y]/[N]): ')
            if konfirmasi.upper() == 'Y':
                return
            elif konfirmasi.upper() == 'N':
                continue
            else:
                print('Pilihan tidak valid. Silahkan coba lagi. ([Y]/[N])')
        else:
            print('Pilihan yang anda masukkan tidak valid. Silahkan coba lagi')            

#FITUR UPDATE
def updateData():
    while True:
        print('''
 ===================== UPDATE DATA KARYAWAN =====================
|1. Update Data Karyawan Universitas Purwadhika                  |
|2. Kembali ke Menu Utama                                        |
 ================================================================
              ''')
        pilihan = input('Ketik submenu yang ingin anda tampilkan ([1]/[2]): ')
        if pilihan == '1':
            while True:
                nikp = input("Masukkan NIKP karyawan yang ingin diupdate: ")
                for karyawan in dataKaryawan:
                    if karyawan['NIKP'] == nikp:
                        print(f"Data karyawan dengan NIKP {nikp} adalah:")
                        print(f"NIKP\t\t: {karyawan['NIKP']}")
                        print(f"Nama\t\t: {karyawan['Nama']}")
                        print(f"Jabatan\t\t: {karyawan['Jabatan']}")
                        print(f"Fakultas\t: {karyawan['Fakultas']}\n")
                        while True:
                            verifData = input('Apakah anda ingin mengubah data ini? ([Y] / [N]): ')
                            if verifData.upper() == 'N':
                                return
                            elif verifData.upper() == 'Y':
                                while True:
                                    kolom = input('Pilih bagian yang ingin diubah (Nama/ Jabatan/ Fakultas):')
                                    if kolom.lower() in ['nama', 'jabatan', 'fakultas']:
                                        break
                                    else:
                                        print('Bagian data yang anda pilih tidak tersedia')
                                newData = input(f'Masukkan {kolom} baru: ')
                                print(f'Apakah anda ingin mengupdate {kolom} dari NIKP {nikp} menjadi {newData}?')
                                verifUpdate = input('Apakah anda yakin ingin mengupdate data ini? ([Y]/ [N]): ')
                                if verifUpdate.upper() == 'Y':
                                    karyawan[kolom.capitalize()] = newData.capitalize()
                                    print('============== [Data Karyawan Berhasil di Update] ===============')
                                    print(f"|NIKP\t\t: {karyawan['NIKP']}                                 \t|")
                                    print(f"|Nama\t\t: {karyawan['Nama']}                                 \t|")
                                    print(f"|Jabatan\t: {karyawan['Jabatan']}                           \t\t|")
                                    print(f"|Fakultas\t: {karyawan['Fakultas']}                         \t\t|")
                                    print('=================================================================')
                                    return
                                elif verifUpdate.upper() == 'N':
                                    print('Update Data Karyawan Dibatalkan')
                                    return
                                else:
                                    print('Pilihan tidak valid. Silahkan coba lagi. ([Y] / [N])')
                        break
                else:
                    print(f'Tidak ada karyawan dengan NIKP {nikp}.')
        elif pilihan == '2':
            konfirmasi = input('Apakah anda ingin kembali ke menu utama? ([Y]/[N]): ')
            if konfirmasi.upper() == 'Y':
                return
            elif konfirmasi.upper() == 'N':
                continue
            else:
                print('Pilihan tidak valid. Silahkan coba lagi. ([Y]/[N])')
        else:
            print('Pilihan yang anda masukkan tidak valid. Silahkan coba lagi')


#FITUR DELETE
def hapusData():
    while True:
        print('''
 ===================== HAPUS DATA KARYAWAN =====================
|1. Hapus Data Karyawan Universitas Purwadhika                  |
|2. Kembali ke Menu Utama                                       |
 ================================================================
              ''')
        pilihan = input('Ketik submenu yang ingin anda tampilkan ([1]/[2]): ')
        if pilihan == '1':
            while True:
                nikp = input("Masukkan NIKP karyawan yang ingin dihapus: ")
                for karyawan in dataKaryawan:
                    if karyawan['NIKP'] == nikp:
                        print(f"Data karyawan dengan NIKP {nikp} adalah:")
                        print(f"NIKP: {karyawan['NIKP']}")
                        print(f"Nama: {karyawan['Nama']}")
                        print(f"Jabatan: {karyawan['Jabatan']}")
                        print(f"Fakultas: {karyawan['Fakultas']}\n")
                        konfirmasi = input('Apakah anda yakin ingin menghapus data karyawan ini? ([Y]/[N]): ')
                        if konfirmasi.upper() == 'Y':
                            dataKaryawan.remove(karyawan)
                            print(f"Data karyawan dengan NIKP {nikp} berhasil dihapus")
                        elif konfirmasi.upper() == 'N':
                            print("Penghapusan data dibatalkan.")
                        else:
                            print('Pilihan tidak valid. Silahkan coba lagi. ([Y]/[N])')
                        break
                else:
                    print(f"Tidak ada karyawan dengan NIKP {nikp}")
                return

        elif pilihan == '2':
            konfirmasi = input('Apakah anda ingin kembali ke menu utama? ([Y]/[N]): ')
            if konfirmasi.upper() == 'Y':
                return
            elif konfirmasi.upper() == 'N':
                continue
            else:
                print('Pilihan tidak valid. Silahkan coba lagi. ([Y]/[N])')
        else:
            print('Pilihan yang anda masukkan tidak valid. Silahkan coba lagi')



def menuData():
    while True:
        print("""
 ================== SISTEM INFORMASI KARYAWAN ===================
 =================== UNIVERSITAS PURWADHIKA =====================
|                                                                |
| 1. Laporan Data Seluruh Karyawan                               |
| 2. Mencari Data Karyawan                                       |
| 3. Input Data Karyawan Baru                                    |
| 4. Update Data Karyawan                                        |
| 5. Menghapus Data Karyawan                                     |
| 6. Keluar                                                      |
|                                                                | 
 ================================================================
            """)
        menuInput = input('Masukkan Menu yang Ingin Anda Pilih (1-6): ')
        print('\n')
        if menuInput == '1':
            showData()
        elif menuInput == '2':
            cariData()
        elif menuInput == "3":
            inputData()
        elif menuInput == "4":
            updateData()
        elif menuInput == "5":
            hapusData()
        elif menuInput == "6":
            konfirmasi = input('Apakah Anda yakin ingin keluar dari program ini? ([Y]/ [N]): ').upper()
            if konfirmasi == 'Y':
                print("========== [Terima kasih telah menggunakan program ini] ==========")
                break
            elif konfirmasi == 'N':
                continue
            else:
                print('\n============== Perintah yang Anda masukkan Salah! ==============')
                continue
        else:
            print('\n============ Perintah yang Anda masukkan Salah! Harap Pilih dari 1- 6 ===========')

menuData()