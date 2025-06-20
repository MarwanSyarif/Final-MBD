import pandas as pd

data = {
    'id1': {'nama': 'Ali', 'prodi': 'Informatika', 'nilai': 85},
    'id2': {'nama': 'Budi', 'prodi': 'Sistem Informasi', 'nilai': 90},
    'id3': {'nama': 'Citra', 'prodi': 'Informatika', 'nilai': 78},
    'id4': {'nama': 'Dina', 'prodi': 'Teknik Komputer', 'nilai': 88},
    'id5': {'nama': 'Eka', 'prodi': 'Informatika', 'nilai': 92},
}

df = pd.DataFrame.from_dict(data, orient='index')

print("Output Wide-Column (DataFrame):\n")
print(df)
