# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:16:36 2021

@author: Tio Chalil Gibran Findianto | 20083000152 - 2E
"""
#Pada materi yang telah dipelajari adalah transaksi dimana pembeli 
#HANYA dapat melakukan pembelian 1 item pada 1 kali transaksi. 
#Namun realita menunjukkan bahwa seorang pembeli dapat membeli 
#lebih dari 1 macam item/barang dalam 1 kali transaksinya. Dan setiap 
#item tersebut dapat lebih dari 1 buah.

#Buat program untuk kasir dengan catatan sbb:
#1. Setiap orang/pembeli dapat membeli lebih dari 1 menu makanan dan minuman, baik 
#makanan maupun minuman sekaligus. (Dapat membeli makanan saja atau minuman saja 
#atau kedua-duanya)
#2. Terdapat input uang bayar dan hitung kembalian
#3. Tampilkan menu2 tsb di layar
#4. Utk OUTPUT tampilkan: menu yg sdh dibeli+harga satuannya+qty+jumlah, 
#termasuk total bayarnya, Uang yg dibayarkan dan kembalianny

print("")
print("=======================================================")
print("=======   SELAMAT DATANG DI RUMAH MAKAN UNMER   =======")
print("=======================================================")
print("")

pembeli = input("Masukkan Nama Pembeli : ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n---- MENU MAKANAN ----")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Lontong Goreng - Rp 14900")
   print("3. Bakso Goreng - Rp 12900")
   print("4. Rujak Bakso - Rp 13000")
   print("5. Rujak Bakso - Rp 15000")
   print("6. Rujak Bakso Pecel - Rp 17000")
   nomor=int(input("Masukan Pilihan : "))
   porsi= int(input("Berapa Mau Makanan? : "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi,"Makanan Nasi Goreng = Rp. ", total1)
       jenis1=("Nasi Goreng")
   elif nomor==2:
       total1=porsi*14900
       print (porsi,"Makanan Lontong Goreng = Rp. ", total1)
       jenis1=("Lontong Goreng")
   elif nomor==3:
       total1=porsi*12900
       print (porsi, "Makanan Bakso Goreng = Rp. ", total1)
       jenis1=("Bakso Goreng")
   elif nomor==4:
       total1=porsi*13000
       print(porsi, "Makanan Rujak Goreng = Rp. ", total1)
   elif nomor==5:
       total1=porsi*15000
       print(porsi, "Makanan Rujak Bakso = Rp. ", total1)
   elif nomor==6:
       total1=porsi*17000
       print(porsi, "Makanan Rujak Bakso Pecel = Rp. ", total1)
   else:
      print("Pilihan Tidak Ada Makanan, Silahkan Ditanyakan Ke Kasir !")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n---- MENU MINUMAN ----")
   print("1. Teh Dingin/Hangat/Panas - Rp 2500")
   print("2. Kopi Dingin - Rp 5000")
   print("3. Kopi Teh Panas - Rp 6500")
   print("4. Coca Cola Dingin - Rp 3500")
   print("5. Coca Cola Panas - Rp 5000")
   nomor=int(input("Masukan Pilihan : "))
   gelas= int(input("Berapa Mau Gelas? : "))

   if nomor==1:
       total2=gelas*2500
       print (gelas,"Minuman Teh Dingin/Hangat/Panas = Rp. ", total2)
       jenis2=("Teh Dingin/Hangat/Panas")
   elif nomor==2:
       total2=gelas*5000
       print (gelas, "Minuman Kopi Dingin = Rp. ", total2)
       jenis2=("Kopi Dingin")
   elif nomor==3:
       total2=gelas*6500
       print (gelas, "Kopi Teh Panas = Rp. ", total2)
       jenis2=("Kopi Teh Panas")
   elif nomor==4:
       total2=gelas*3500
       print(gelas, "Minuman Coca Cola Dingin = Rp. ", total2)
       jenis2=("Coca Cola Dingin")
   elif nomor==5:
       total2=gelas*5000
       print(gelas, "Minuman Coca Cola Panas = Rp. ", total2)
       jenis2="Coca Cola Panas"
   else:
      print("Pilihan Tidak Ada Minuman, Silahkan Ditanyakan Ke Kasir !")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal Harus Dibayar : Rp. ",totalsemua)
uang=int(input("Uang Tunai Pembeli : Rp. "))
kembalian=int(uang-totalsemua)
print("Kembalian : Rp. ",kembalian)

print("\n=======================================================")
print("=======          MENU MAKANAN & MINUMAN          ======")
print("=======================================================")
print (" Nama Pembeli            :",pembeli)
print (" Beli Makanan & Minuman  :",porsi,jenis1,"- Rp.", total1)
print ("                          ",gelas,jenis2,"- Rp.", total2)
print (" Transaksi               : Rp. ",totalsemua)
print (" Uang                    : Rp. ",uang)
print (" Kembalian               : Rp. ",kembalian)
print("=======================================================")
print("----- TERIMA KASIH TELAH DIBELI MAKANAN & MINUMAN -----")
print("=======================================================")