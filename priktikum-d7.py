pwd_benar = 'si23d'
a = True
limit= 3
i = 0

while a:
    i += 1
    pwd = input('masukkan password: ')
    if pwd == pwd_benar:
        print('password benar! selamat anda login :D')
        a = False
    else:
        print('password salah ')
        if i == limit:
                     print('kesempatan anda habis')
                     a = False
        else:print(f'kesempatan anda tersisa {limit-i}')

        
        #tugas buat pasword berlapis 3
        #jika salah: password salah, anda gagal pada halaman 1
        #jika salah: password salah, anda gagal pada halaman 2
        #jika salah: password salah, anda gagal pada halaman 3
        
        #jika benar: password benar, selamat datang dihalaman 1
        #jika benar: password benar, selamat datang dihalaman 2
        #jika benar: password benar, selamat anda berhasil login

        #tiap halaman, memiliki kesempatan 3 kali masukan password
        