# TIPE DATA LIST/ DAFTAR/ARRAY
anak = ['WAE', 'KUDIA', 'SAMNAH', 'LINGGA']
print(anak)
anak.append('LISAH')
print(anak)
# Sapa Anak ke-2
print(f'hai {anak[1]} !')

# Tampilkan Semua Anak
for a in anak:
    print(f'hai {a} !')

for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]} !')

