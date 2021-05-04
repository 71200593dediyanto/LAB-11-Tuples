# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# Tuple

'''
Kane yang sedang duduk di bangku SMP kesulitan untuk memahami
materi KPK (kelipatan persukutuan terbesar) di sekolahnya.
Suatu hari Kane yang malas untuk belajar, diberikan soal 
tentang materi KPK oleh gurunya , kebetulan kakak Kane 
adalah seorang mahasiswa informatika, dia meminta kakaknya
untuk membuatkan sebuah program yang dapat menghitung KPK 
dari sebuah bilangan bulat positif yang diberikan dan 
menyimpan data hasil perhitungan tersebut. 
Kane mengilustrasikan program yang dia inginkan dapat:
1.Menghitung KPK dari bilangan bulat positif yang diberikan, dan program
  dapat menerima 2 bilangan atau lebih.
2.Program dapat menyimpan data hasil perhitungan KPK, 
  dari bilangan bulat positif yang diberikan dan dapat 
  menampilkan pemberitahuan hasil dari perhitungan KPK 
  dari data yang telah disimpan sebelumnya. 
3.Setelah program selesai digunakan, program dapat 
  menampilkan data mentah yang telah disimpan semuanya.

Anggaplah anda adalah kakaknya Kane, bantulah kane 
dalam membuat sebuah program seperti diatas !!.

'''

'''

Input:
1. menambahkan data
2. menampilkan data
3. exit

input : 1
masukkan 2 angka atau lebih : 4 2 3


Proses:
4 2 3

2 = [2,4,6,8,10,12]
3 = [3,6,9,12,15,18]
4 = [4,8,12,16,20,24]

a x (n + 1)
n = 0 + 1
2 x (0+1)
3 x (0+1)
4 x (0+1)

kpk = 2

(2,3,4) = 12


Output:
1. menambahkan data
2. menampilkan data
3. exit

kpk dari (2,3,4) adalah 12

{(2,3,4):12}

'''

# Source Code
data_kpk = {}
while True:
  print("1. Menambahkan data\n2. Menampilkan data\n3. Exit")
  pilihan = int(input("Masukkan pilihan anda : "))
  if pilihan == 1:
    print("\nSilahkan tambahkan data anda !!\n(Pisahkan tiap data dengan spasi!)")
    data = [int(i) for i in input("Masukkan 2 angka atau lebih : ").split()]
    data.sort()
    list_kpk = [[] for i in range(len(data))]
    kpk = 0
    n = 0
    while True:
      hitung = 0
      for i in range(len(data)):
        list_kpk[i].append(data[i]*(n+1))
      kpk = data[0]*(n+1)
      n += 1
      for i in list_kpk:
        if kpk in i:
          hitung += 1
      if hitung == len(data):
        data_kpk[tuple(data)] = kpk
        break
    print('Data berhasil di tambahkan\n')
  elif pilihan == 2:
    if len(data_kpk) == 0:
      print("Belum ada data yang dimasukkan !")
    else:
      for i in data_kpk:
        print('Kpk dari',i,'=',data_kpk[i])
    print()
  elif pilihan == 3:
    if len(data_kpk) == 0:
      print("Belum ada data yang dimasukkan !")
    else:
      print(data_kpk)
    break
  else:
    print("Invalid Input !")