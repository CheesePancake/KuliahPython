tuple1 = (2, 3, 4, [5, 6])
# Anggota tuple tidak bisa diubah
# bila tanda # pada baris 6 
# maka error : TypeError: 'tuple' object does not support live item assignment

# tuple1[1] = 8

# tapi list dalam tuple dapat diubah
# output (2, 3, 4, [7, 6])

tuple1[3][0] = 7
print(tuple1)

# tuple bisa diubah dengan penugasan kembali
# output : ('p', 'y', 't', 'h', 'o', 'n')
tuple1 = ('p', 'y', 't', 'h', 'o', 'n')
print(tuple1)

# anggota tuple tidak bisa dihapus menggunakan del
# perintah berikut akan menampilkan error TypeError
# kalau # dihilangkan

# del tuple1[0]
# tuple bisa dihapus keseluruhan
del tuple1
