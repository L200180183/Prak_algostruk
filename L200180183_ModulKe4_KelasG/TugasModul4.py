from L200180183_ModulKe4_KelasG.Latihan1 import *

#NOMOR1
def pencarian(list,target):
    hasil = []
    for i in list:
        if i.kotaTinggal == target:
            hasil.append(list.index(i))
    print(hasil)

pencarian(Daftar,'Klaten')

#NOMOR2
def uangSakuTerkecil(list):
    terkecil = 99999999
    for i in list:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    return terkecil

uangSakuTerkecil(Daftar)

#NOMOR3
def uangSakuTerkecilObject(list):
    temp = [list[0]]
    for i in list:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

uangSakuTerkecilObject(Daftar)

#NOMOR4
def uangKurangDari(list):
    temp = []
    for i in list:
        if i.uangSaku < 250000:
            temp.append(i)
    return temp

uangKurangDari(Daftar)

#NOMOR5
class node(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

    def cariLinkedList(self, dicari):
        curNode = self
        while curNode is not None:
            if curNode.next != None:
                if curNode.data != dicari:
                    curNode = curNode.next
                else:
                    print ("Data", dicari, "ada dalam Linked List")
                    break
            elif curNode.next == None:
                print ("Data", dicari, "tidak ada dalam Linked List")
                break
a = node(45)
menu = a
a.next = node (9)
a = a.next
a.next = node (17)
a = a.next
a.next = node (23)

menu.cariLinkedList(9)
menu.cariLinkedList(22)

#NOMOR6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False
kumpulan = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

#NOMOR7
def binSe2(target):
    low = 0
    high = len(kumpulan)-1
    x = []

    while low < high:
        if kumpulan[low] == target:
            x.append(low)
            low+=1
        else:
            low+=1
    return x
kumpulan = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]

#NOMOR8
print
"""Karena menggunakan konsep Big-O. Dimana yang dipakai
adalah rumus O(log n) dengan rincian 1 = 1, 2 = 2, 4 = 3, 10 = 4, 100 = 7, 1000=10.
Di mana log berasal dari pangkat log berbasis 2. Dengan begitu dapat mengetahui jumlah
maksimal tebakan.
Untuk pola sendiri:
        apabila ingin menebak angka 70

        a = nilai tebakan pertama // 2
        tebakan selanjutnya = nilai tebakan "lebih dari" + a
        *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang dipakai
        tetap nilai lebih dari sebelumnya*
        a = a // 2
    Simulasi
        tebakan ke 1: 50 (mengambil nilai tengah) jawaban= "lebih dari itu"
        tebakan ke 2: 75 (dari 50 + 25) jawaban = "kurang dari itu"
        tebakan ke 3: 62 (dari 50 + 12) jawaban = "lebih dari itu"
        tebakan ke 4: 68 (dari 62 + 6) jawaban = "lebih dari itu"
        tebakan ke 5: 71 (dari 68 + 3) jawaban = "kurang dari itu"
        tebakan ke 6: 69 (dari 68 + 1) jawaban = "lebih dari itu"
        tebakan ke 7: antara 71 dan 69 hanya ada 1 angka = 70!!!
"""