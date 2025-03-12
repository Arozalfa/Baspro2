nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

gaji = 0
bonus = 0

if status == "Tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
elif status == "Honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000
else:
    print("Status tidak valid. Harap masukkan Pegawai Tetap atau Honor.")
    exit()

gaji_total = gaji + bonus

print("--- Informasi Gaji Karyawan ---")
print("Nama        : {}".format(nama))
print("NIK         : {}".format(nik))
print("Status      : Pegawai {}".format(status.capitalize()))
print("Golongan    : {}".format(golongan))
print("Gaji        : Rp {:,}".format(gaji))
print("Bonus       : Rp {:,}".format(bonus))
print("Gaji Total  : Rp {:,}".format(gaji_total))