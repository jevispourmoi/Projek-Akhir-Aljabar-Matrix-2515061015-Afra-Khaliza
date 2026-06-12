import afra015

print("===PROGRAM OPERASI MATRIKS 3x3===")

print("\nMasukkan elemen matriks 3x3:")
matriks = [
    [int(input(f"Baris {i+1} Kolom {j+1}: ")) for j in range(3)]
    for i in range(3)
]

while True:

    print("\nMENU")
    print("1. Tampilkan Matriks")
    print("2. Transpose Matriks")
    print("3. Determinan Matriks")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print("\nMatriks:")
        for row in matriks:
            print(row)

    elif pilihan == "2":
        print(f"\nTranspose Matriks:{afra015.transpose(matriks)}")

    elif pilihan == "3":
        print("\nDeterminan:", afra015.determinan(matriks))

    elif pilihan == "4":
        print("\nTerima kasih telah menggunakan program.")
        break

    else:
        print("\nPilihan tidak valid.")