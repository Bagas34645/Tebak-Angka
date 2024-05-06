import random

def main(): 
    angka_rahasia = random.randint(1, 10)
    tebakan = None
    jumlah_tebakan = 0

    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Tebak angka antara 1 dan 10: "))
            jumlah_tebakan += 1
            if tebakan < angka_rahasia:
                print("Tebakanmu terlalu rendah.")
            elif tebakan > angka_rahasia:
                print("Tebakanmu terlalu tinggi.")
            else:
                print(f"Selamat! Kamu berhasil menebak angka dengan benar dalam {jumlah_tebakan} kali tebakan.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()