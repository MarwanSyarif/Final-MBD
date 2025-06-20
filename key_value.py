import dbm

with dbm.open('db_key_value', 'c') as db:
    db['nama'] = 'Marwan'
    db['nim'] = 'D0222353'
    db['prodi'] = 'Informatika'
    db['kelas'] = 'TI-D'
    db['angkatan'] = '2022'

with dbm.open('db_key_value', 'r') as db:
    for key in db.keys():
        print(f"{key.decode()} : {db[key].decode()}")
