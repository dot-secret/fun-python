# KONSTRUKSI DASAR PYTHON
# SEQUENSIAL :Eksekusi Berurutan
print('heloo WOrld')
print('By Redha ')
print('Tanggal 12 Juni 2020')
print('---' * 3)

# PERCABANGAN: Eksekusi terpilih
ingin_cepat = True
if ingin_cepat:
    print('Jalan Lurus Aja')
else:
    print('Jalan Lain')

# PERCABANGAN
ingin_balik = True

# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): # Jumlah Perulangan = 5-1 =4
    print(f'Halo Anak #{index_anak}')
