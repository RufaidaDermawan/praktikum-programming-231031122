print('praktikum-2\n\n')


a = True
b = False
print('============Ini and============')
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)

print('============Ini or============')
hasil = a or a
print('nilai',a,'or',a,'adalah',hasil)
hasil = a or b
print('nilai',a,'or',b,'adalah',hasil)
hasil = b or a
print('nilai',b,'or',a,'adalah',hasil)
hasil = b or b
print('nilai',b,'or',b,'adalah',hasil)

print('\n============Ini not============')
hasil = a or a
print('hasil not',a,'adalah',hasil)
hasil = not b
print('hasil not',b,'adalah',hasil)

print('\n============Ini xor============')
hasil = a ^ a
print('nilai',a,'xor',a,'adalah',hasil)
hasil = a ^ b
print('nilai',a,'xor',b,'adalah',hasil)
hasil = b ^ a
print('nilai',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print('nilai',b,'xor',b,'adalah',hasil)

print('\n============Ini nand============')
hasil =not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
hasil =not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)
hasil =not (b and a)
print('Nilai',b,'nand',a,'adalah',hasil)
hasil =not (b and b)
print('Nilai',b,'and',b,'adalah',hasil)

print('\n============Ini nor============')
hasil =not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil =not (a or b)
print('Nilai',a,'nor',b,'adalah',hasil)
hasil =not (b or a)
print('Nilai',b,'nor',b,'adalah',hasil)
hasil =not (b or b)
print('Nilai',b,'nor',a,'adalah',hasil)

print('\n============Ini xor============')
hasil = a ^ a
print('nilai',a,'xor',a,'adalah',not hasil)
hasil = a ^ b
print('nilai',a,'xor',b,'adalah',not hasil)
hasil = b ^ a
print('nilai',b,'xor',a,'adalah',not hasil)
hasil = b ^ b
print('nilai',b,'xor',b,'adalah',not hasil)

print('================ Is')
a = 5 
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
print('a is b =',hasil)
hasil = a is b
a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('\n================ Is NOT')
a = 5 
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
print('a is not b =',hasil)
hasil = a is not b
a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n================ in')
nama = 'bacharuddin jusuf habibie'

test = 'rud'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'bach'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'ib'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'a'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'i'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'u'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'e'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'o'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

print('\n================ not in')
nama = 'Rufaida Dermawan'

test = 'rud'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'bach'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'ib'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'a'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'i'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'u'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'e'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'o'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 


print('\n================ not in')
data = ['institut',
        'teknologi',
        'bacharuddin',
        'jusuf',
        'habibie']
print('data adalah',data)
test1 = 'habibie'
test2 = 'parepare'
test3 = 'kampus'
test4 = 'institut'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))

print('\n================ not in')
data = ['Rufaida',
        'dermawan']
print('data adalah',data)
test1 = 'Rufaida'
test2 = 'dermawan'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))


# INI OPERATOR BITWISE
print('\n================ not in')
a = 24
b = 7
b += 2005
print('\n================ AND')
print('nilai',a,'dalam biner   =',format(a,'08b'))
print('nilai',b,'dalam biner   =',format(b,'08b'))
print('------------------------------------and')
c = a & b
print('nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print('\n================ not in')
a = 24
b = 7
b += 2005
print('\n================ QR')
print('nilai',a,'dalam biner   =',format(a,'08b'))
print('nilai',b,'dalam biner   =',format(b,'08b'))
print('------------------------------------and')
c = a | b
print('nilai',a,'|',b,'dalam biner adalah',format(c,'08b'))

print('\n============Ini xor============')
hasil = a ^ b
print('nilai',a,'xor',b,'adalah',not hasil)
hasil = a ^ a
print('nilai',a,'xor',a,'adalah',not hasil)
hasil = b ^ a
print('nilai',b,'xor',a,'adalah',not hasil)
hasil = b ^ b
print('nilai',b,'xor',b,'adalah',not hasil)

print('\n============Ini not============')
hasil = c or c
print('hasil not',a,'adalah',hasil)
hasil = not a
print('hasil not',b,'adalah',hasil) 

print('\n============Ini not============')
hasil = b or b
print('hasil not',a,'adalah',hasil)
hasil = not a
print('hasil not',b,'adalah',hasil)

print('\n============geser kanan============')
a = 16
c = a >> 2
print(c) # output : 4

print('\n============geser kiri============')
a = 16
c = a << 2
print(c) # output : 4

print('============not and============')
hasil = a & b
print('Nilai',a,'&',b,'adalah',hasil)
hasil = b & a
print('Nilai',b,'&',a,'adalah',hasil)
hasil = b & b
print('Nilai',b,'&',b,'adalah',hasil)
hasil = b & a
print('Nilai',b,'&',a,'adalah',hasil)

print('============not or============')
hasil = a | b
print('nilai',a,'|',b,'adalah',hasil)
hasil = b | a
print('nilai',b,'|',a,'adalah',hasil)

print('\n============not xor============')
hasil = a ^ b
print('nilai',a,'xor',b,'adalah',not hasil)
hasil = a ^ a
print('nilai',a,'xor',a,'adalah',not hasil)
hasil = b ^ a
print('nilai',b,'xor',a,'adalah',not hasil)
hasil = b ^ b
print('nilai',b,'xor',b,'adalah',not hasil)

print('\n============not geser kanan============')
a = 16   # reprensi binar dari 16 adalah '10000'
c = ~(a >> 2)
print(c)

print('\n============not geser kiri============')
a = 16   # reprensi binar dari 16 adalah '10000'
c = ~(a << 2)
print(c)























