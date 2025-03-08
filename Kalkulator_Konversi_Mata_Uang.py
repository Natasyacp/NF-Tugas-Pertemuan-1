print(" ")
print("Kalkulator Konversi Mata Uang")
print("===========================")
print(">> Menu <<")
print("1. Rupiah ke Dollar")
print("2. Dollar ke Rupiah")
print("===========================")
print(" ")
menu = int(input("Masukkan pilihan konversi = "))
    
if menu == 1:
    idr = int(input("Masukkan jumlah idr = Rp."))
    hasil = float(idr/15265)
    print("Nilai idr Rp", idr, "= $",hasil)

elif menu == 2:
    usd = int(input("masukkan jumlah $ ="))
    hasil = usd*15265
    print("Nilai $",usd,"= Rp.",hasil)
    
else:
    print("Tidak terdefinisi")

print("====================")
print("    Terima Kasih    ")