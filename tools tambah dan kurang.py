def header():
	print(" CALCULATOR SIMPLE ^_^ By:Rm_Hcy07")
	print("1.Tambah Tambahan)
	print("2.Kurang Kurangan)
	print("pilih angka 1 untuk Tambah Tambahan dan angka 2 untuk Kurang Kurangan")
	pilihan = (input("Pilih Salah 1 :"))
	def tambah():
		hasil= angka1 + angka2
		return angka1 + angka2
		print (hasil)
	def kurang():
		hasilPengurangan= angka1 - angka2
		print (hasilPengurangan)
	if pilihan == "1":
		print ("masukan bilangan yang ingin di jumlahkan")
		angka1 = int(input("Angka1 : "))
		angka2 = int(input("Angka2 : "))
		print ("hasil pejumlahan adalah:"),tambah()
	elif pilihan == "2":
		print ("masukan bilangan yang ingin di kurangi")
		angka1 = int(input("Angka1 : "))
		angka2 = int(input("Angka2 : "))
		print ("hasil pengurangan adalah:"),kurang()
	else :
		print ("masukan pilihan yang tepat")
print (header())
