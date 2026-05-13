import requests
import csv


def szerzok_szovegge(szerzok):
    nevek = []

    for szerzo in szerzok:
        nevek.append(szerzo.get("name", ""))

    return ", ".join(nevek)


def konyvek_lekerese():
    url = "https://gutendex.com/books/?languages=hu"
    konyvek = []
    oldal = 1

    while url is not None and oldal <= 3:
        print("Oldal:", oldal)

        try:
            valasz = requests.get(url)
            adat = valasz.json()
        except:
            print("Hiba történt a lekérés közben.")
            break

        for book in adat.get("results", []):
            konyv = {
                "cim": book.get("title", ""),
                "szerzok": szerzok_szovegge(book.get("authors", [])),
                "letoltes": book.get("download_count", 0),
                "oldal": oldal
            }

            konyvek.append(konyv)

        url = adat.get("next")
        oldal +=1

    return konyvek


def csv_mentes(konyvek):
    with open("talalatok.csv", "w", newline="", encoding="utf-8") as fajl:
        iro = csv.DictWriter(fajl, fieldnames=["cim", "szerzok", "letoltes", "oldal"])
        iro.writeheader()
        iro.writerows(konyvek)


def keres(konyvek, szo):
    talalatok = []

    for konyv in konyvek:
        if szo in konyv["cim"]:
            talalatok.append(konyv)

    return talalatok


def listaz(konyvek):
    for konyv in konyvek:
        print(konyv["cim"] + " - " + konyv["szerzok"])


print("Magyar nyelvű Gutenberg könyvek")

konyvek = konyvek_lekerese()

csv_mentes(konyvek)

print("A lekért könyvek száma:", len(konyvek))
print("A fájl elkészült: talalatok.csv")

keresett = input("Adj meg egy keresett szót a címben: ")
talalatok = keres(konyvek, keresett)

print("Találatok:")
listaz(talalatok)