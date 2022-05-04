from random import choice

ITEM = ["gajah", "orang", "semut"]
main = True
skor = 0

while main:
    print("\nSuwit Jawa")
    print("10 MIPA 2 - Aullya Nadine Kuswandi (2)")

    input_user = input("Pilih (Gajah | Orang | Semut): ").lower()
    komputer = choice(ITEM)
    hasil = ""

    if input_user == komputer:
        hasil = "Seri!"
    elif input_user == "gajah":
        hasil = "Menang!" if komputer == "orang" else "Kalah!"
    elif input_user == "orang":
        hasil = "Menang!" if komputer == "semut" else "Kalah!"
    elif input_user == "semut":
        hasil = "Menang!" if komputer == "gajah" else "Kalah!"
    else:
        hasil = "Pilih yang benar dong :v"

    if hasil == "Menang!":
        skor += 1

    print(f"Anda pilih {input_user}, komputer pilih {komputer}")
    print(hasil)

    lagi = input("Main lagi? (ya/tidak): ").lower()

    if lagi == "ya":
        continue
    elif lagi == "tidak":
        break
    else:
        print("Pilih yang benar dong... yodah lanjut lagi aja yuk :D")

print("Terima kasih sudah bermain!")
print(f"Total Skor Anda: {skor}")
