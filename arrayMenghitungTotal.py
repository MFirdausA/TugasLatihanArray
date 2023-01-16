#deklarasikan array
array = []
#membuat variable total
total = 0
#membuat variable n untuk menampung jumlah array yang akan di input
#n = jumlah elemen
n = int(input("masukan jumlah elemen array: "))
for x in range(n) :
    #menginputkan nilai yang akan bertambah 1
    nilai = float(input("masukab Nilai ke- {}: ".format(x+1)))
    array.append(nilai)
    #menampilkan jumlah dari nilai
    print("\nHasil nilai total adalah:  {}".format(sum(array)))
    #menampilkan rata rata
    print("hasil rata rata adalah : {}".format(sum(array)/n))
