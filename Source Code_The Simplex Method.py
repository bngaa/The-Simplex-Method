import numpy as np

def simplex(matriks):
    while any(matriks[-1, :-1] < 0):
        kolom_pivot = np.argmin(matriks[-1, :-1])
        rasio = matriks[:-1, -1] / matriks[:-1, kolom_pivot]
        rasio[rasio <= 0] = np.inf
        baris_pivot = np.argmin(rasio)
        pivot = matriks[baris_pivot, kolom_pivot]
        matriks[baris_pivot, :] /= pivot
        for i in range(len(matriks)):
            if i != baris_pivot:
                matriks[i, :] -= matriks[i, kolom_pivot] * matriks[baris_pivot, :]
    return matriks

# Contoh Input
matriks_awal = np.array([
    [2, 3, 1, 0, 0, 18],
    [2, 1, 0, 1, 0, 14],
    [1, 2, 0, 0, 1, 10],
    [-3, -5, 0, 0, 0, 0]
], dtype=float)

hasil = simplex(matriks_awal)
print("Hasil Akhir Tabel Simplex:")
print(hasil)