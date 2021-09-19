#coding

def kali():
	angka_1 = int(input('Masukkan angka : '))
	angka_2 = int(input('Masukkan angka : '))
	hasil = angka_1 * angka_2
	print ('ini hasil nya', hasil)
	return

def bagi():
	angka_3 = int(input('Masukkan angka : '))
	angka_4 = int(input('Masukkan angka : '))
	hasil_2 = angka_3 / angka_4
	print ('ini hasil nya', hasil_2)
	return

def kurang():
	angka_5 = int(input('Masukkan angka : '))
	angka_6 = int(input('Masukkan angka : '))
	hasil_3 = angka_5 - angka_6
	print ('ini hasil nya', hasil_3)
	return

def tambah():
	angka_7 = int(input('Masukkan angka : '))
	angka_8 = int(input('Masukkan angka : '))
	hasil_4 = angka_7 + angka_8
	print ('ini hasil nya' , hasil_4)
	return

print ('-' *20)

print ('Ini kalkulator')
print ('\n 1. Perkalian')
print (' 2. Pembagian')
print (' 3. Pengurangan')
print (' 4. Pertambahan')

print ('\n contoh pilihan : 1')
pilihan = str(input('Masukkan pilihan mu : '))

A = '1'
B = '2'
C = '3'
D = '4'

if pilihan in A:
	kali()
elif pilihan in B:
	bagi()
elif pilihan in C:
	kurang()
elif pilihan in D:
	tambah()
else:
	print ('Maaf anda salah pilih')

