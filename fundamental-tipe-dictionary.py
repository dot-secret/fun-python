print("\nini dikirim oleh Server Gojek, untuk mengirimkan info Driver di Sekitar Pengguna Aplikasi")
data_dari_server_gojek = {
    'tanggal': '2020-07-07',
    'driver_list' : [
        {'nama':'WAE','jarak':100},
                     {'nama':'KUDIA','jarak':200},
                     {'nama':'SAMNAH', 'jarak':250},
                     {'nama':'LINGGA','jarak':150}
    ]
}
print(data_dari_server_gojek)
print(f"Driver disekitar Sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver Terdekat Dengan Anda {data_dari_server_gojek['driver_list'][0]['jarak']} meter bung")