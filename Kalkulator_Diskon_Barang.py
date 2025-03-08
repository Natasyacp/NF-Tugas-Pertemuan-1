print(" ")
print(" Kalkulator Diskon Barang ")
print("==========================") 
print(">> Menu <<")
print("1. Kalkulator Diskon Simpel")
print("2. Kalkulator Diskon Lengkap")
print("===========================")
print(" ")

menu = int(input("Pilih menu : "))

if menu == 1 :
    harga_barang = float(input("Masukkan Harga Barang : "))
    presentase_diskon = float(input("Masukkan presentase diskon : "))

    diskon = harga_barang * (presentase_diskon/100)
    print("Harga setelah diskon adalah: ",harga_barang-diskon)

elif menu == 2 :
    jumlah = int (input("Masukkan jumlah Barang : "))
    harga_barang = float(input("Masukkan Harga Barang : "))
    
    presentase_diskon = float(input("Masukkan presentase diskon : "))
    diskon = (presentase_diskon/100)
    
    print("Harga barang setelah diskon : ", jumlah * harga_barang * diskon)
else :
    print("Tidak terdefinisi")
    
print(" ")
print("====================")
print("    Terima Kasih    ")