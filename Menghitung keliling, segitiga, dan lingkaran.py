#1
print("PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA")

a = float(input("\nMasukan Alas  : "))
t = float(input("Masukan Tinggi: "))
luas = 0.5*a*t
print("\nLuas Segitiga  = %0.2f" % luas)




#2
print('MENGHITUNG LUAS LINGKARAN')

r = int(input('masukan jari-jari lingkaran: '))
phi = 3.14
L = phi * (r * r)
print('Luas lingakaran dengan jari-jari {} adalah {}'.format(r, L))


#3
print("MENGHITUNG LUAS & KELILING PERSEGI")

s = float(input("\nMasukan Panjang Sisi: "))
luas = s**2
keliling = 4 * s
print("\nLuas Persegi \t\t:",luas)
print("Keliling Persegi\t:",keliling)