import afra015

print("===PROGRAM OPERASI MATRIKS 3x3===")

matriks = []

print("\nMasukkan elemen matriks 3x3:")

for i in range(3):
    baris = []

    for j in range(3):
        nilai = int(input(f"Baris {i+1} Kolom {j+1}: "))
        baris.append(nilai)

    matriks.append(baris)

while True:

    print("\n===== MENU =====")
    print("1. Tampilkan Matriks")
    print("2. Transpose Matriks")
    print("3. Determinan Matriks")
    print("4. Inverse Matriks")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\nMatriks:")
        for baris in matriks:
            print(baris)

    elif pilihan == "2":
        hasil = afra015.transpose_matrix_3x3(matriks)
        print("\nTranspose Matriks:")
        for baris in hasil:
            print(baris)

    elif pilihan == "3":
        hasil = afra015.determinan_3x3(matriks)
        print("\nDeterminan Matriks:")
        print(hasil)

    elif pilihan == "4":
        hasil = afra015.inverse_matrix_3x3(matriks)
        if hasil is None:
            print("\nMatriks tidak memiliki invers karena determinannya 0.")
        else:
            print("\nInverse Matriks:")
            for baris in hasil:
                print(baris)

    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan program.")
        break

    else:
        print("\nPilihan tidak valid.")