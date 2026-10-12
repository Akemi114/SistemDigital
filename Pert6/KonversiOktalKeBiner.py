input_oktal = input("Masukkan bilangan oktal: ")
oktal = int(input_oktal, 8)

if oktal < 0:
    print("Masukkan bilangan oktal yang valid (>= 0).")

elif oktal == 0:
    print("0 dalam biner adalah 0")

else:
    angka = oktal
    biner = ""
    proses = ""

    while angka > 0:
        hasilBagi = angka // 2
        sisa = angka % 2
        proses += (
            str(angka) +
            " ÷ 2 = " +
            str(hasilBagi) +
            " sisa " +
            str(sisa) +
            "\n"
        )
        biner = str(sisa) + biner
        angka = hasilBagi

    print()
    print("Bilangan Oktal:", input_oktal)
    print()
    print("Tahapan Perhitungan:")
    print(proses)
    print("Baca sisa dari bawah ke atas:")
    print(biner)
    print()
    print(
        "Jadi,",
        input_oktal,
        "oktal =",
        biner,
        "biner"
    )