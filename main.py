from periodic import test

def main():
    points = 0  # Inisialisasi poin di sini
    try:
        while True:
            print(f"Poin Anda: {points}")
            print("==================")
            print("Pilih Level:")
            print("1. Easy")
            print("2. Normal")
            print("3. Hard")
            print("4. All")
            print("==================")
            level = input("Masukkan level(1/2/3/4): ")
            if level == "1":
                points += test.easy()  # Tambahkan poin yang diperoleh
            elif level == "2":
                points += test.normal()
            elif level == "3":
                points += test.hard()
            elif level == "4":
                points += test.all()
    except KeyboardInterrupt:
        print("\nTerima kasih sudah bermain! Skor akhir Anda adalah:", points)

if __name__ == "__main__":
    main()
