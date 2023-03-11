# Set integer
set_saya = {1, 2, 3}
print(set_saya)

# Set dengan menggunakan fungsi set()
set_saya = set([1, 2, 3])
print(set_saya)

# Set data campuran 
set_saya = {1, 2.0, "Python", (3, 4, 5)}
print(set_saya)

# bila terdapat duplikasi maka set akan menghilangkan salah satu
# output {1,2,3}
set_saya = {1,2,2,3,3,3}
print(set_saya)

# set tidak bisa berisi anggota list
# set berikut akan menghasilkan TypeError
set_saya = {1, 2, [3, 4, 5]}
