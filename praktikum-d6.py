a = True

while a:
    jawab = input('apakah ingin lanjutkan? (y/n)')
    if jawab == 'y':
        print('terima kasih')
        a = True
    elif jawab == 'n':
        print('sampai jumpa :D')
        a = False
    else:
        print('jangan aneh deh:D')
        a = True