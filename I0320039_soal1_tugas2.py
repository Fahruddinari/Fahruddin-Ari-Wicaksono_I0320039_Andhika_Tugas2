#manampilkan informasi pogram
print("Menghitung Luas Persegi Panjang")
print("++++++++++++++++++++++++++++++++")

#input nilai panjang dan lebar
Panjang = float(input("Masukan nilai panjangnya: "))
Lebar = float(input("Masukan nilai lebarnya: "))

#menghitung luas persegi panjang
luas = Panjang*Lebar

#menampilkan hasil perhitungan
print("Luas persegi panjang adalah " + str(luas) + ".")

#menampilkan informasi program
print("Menghitung Luas Lingkaran")

#input nilai jari-jari lingkaran
jari_jari = float(input("Berapa nilai jari-jari : "))

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (jari_jari ** 2)

#menampilkan luas lingkaran
print("Luas lingkaran adalah "+str(luas_lingkaran)+".")

#menampilkan informasi pogram
print("Menghitung Luas Kubus")

#input nilai rusuk kubus
rusuk_kubus = float(input("Berapa nilai rusuk kubus : "))

#menghitung nilai luas kubus
luas_kubus = 6*(rusuk_kubus ** 2)

#menampilkan nilai luas kubus
print("Nilai luas kubus adalah "+str(luas_kubus)+".")

#menampilkan konversi suhu dari celcius ke farenheit
print("Menghitung Konversi Suhu dari Celcius ke Farenheit")

#input nilai suhu celcius
C = float(input("Suhu dalam Celcius: "))

#konversi suhu dalam Celcius ke Farenheit
F = (9*C)/5 + 32

#menampilkan hasil perhitungan
print("Suhu dalam Farenheit: "+str(F)+".")

#menghitung konversi suhu dari Rearmur ke Kelvin
print("Menghitung Konversi Suhu dari Rearmur ke Kelvin")

#input nilai suhu dalam Rearmur
R = float(input("Suhu dalam Rearmur: "))

#menghitung konversi suhu ke Kelvin
K = (5*R)/4 + 273

#menampilkan konversi suhu
print("Suhu dalam Kelvin: "+str(K)+".")


