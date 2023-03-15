# Membuat set baru

set_saya = {1,2,3}
print(set_saya)

# bila # dihilangkan dari baris 6 maka akan muncul TypeError
# set_saya[0]

# menambah satu anggota
# output: {1,2,3,4}
set_saya.add(4)
print(set_saya)

# menambah beberapa a nggota
# set akan menghilangkan duplikasi
# output : {1,2,3,4,5,6}
set_saya.update([3,4,5,6])
print(set_saya)