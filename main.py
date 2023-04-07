from biblioteka import Biblioteka
import os

biblioteka = Biblioteka()
biblioteka.ucitaj_stavke()
biblioteka.ucitaj_clanove()
while True:
    print ("-----------------------")
    print ("DOBRODOSLI U BIBLIOTEKU")
    print ("-----------------------")
    print ("1.Prikaz svih stavki u biblioteci")
    print ("2.Prikaz svih dostupnih stavki u biblioteci")
    print ("3.Prikaz svih clanova u biblioteci")
    print ("4.Prikaz svih stavki pozajmljenih od strane odredjenih clanova")
    print ("5.Pozajmiti stavku")
    print ("6.Vratiti stavku")
    print ("7.Izlaz iz programa")


    unos = input ("Unesite broj da bi zapoceli program: ")
    os.system("cls")

    if unos == "1":
        biblioteka.ispisi_stavke()
    elif unos == "2":
        biblioteka.prikaz_svih_dostupnih_stavki()
    elif unos == "3":
        biblioteka.prikaz_svih_clanova()
    elif unos == "4":
        os.system('cls')

        for index, clan in enumerate(biblioteka.clanovi):
            print(str(index + 1) + ". " + clan.ime + " " + clan.prezime)

        try:
            unos = int(input("Izaberite clana: "))

            if unos <= len(biblioteka.clanovi) and unos > 0:
                izabrani_clan = biblioteka.clanovi[unos - 1]
                biblioteka.prikaz_svih_pozajmljenih_stavki_jednog_clana(izabrani_clan)
            else:
                raise

        except:
            print("Nije dobar unos!")
            input("Pritisnite ENTER da nastavite...")
            os.system("cls")

