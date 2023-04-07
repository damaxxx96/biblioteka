from biblioteka import Biblioteka
from clan import Clan
import os

biblioteka = Biblioteka()
biblioteka.ucitaj_stavke()
biblioteka.ucitaj_clanove()
prijavljeni_clan: Clan = None

while True:

    ime = input ("Unesite ime: ")
    os.system('cls')

    try:
        pronadjeni_clan = next(filter(lambda clan: ime == clan.ime, biblioteka.clanovi))

        if isinstance(pronadjeni_clan, Clan):
            prijavljeni_clan = pronadjeni_clan

            while True:
                print ("-----------------------")
                print(prijavljeni_clan.ime + " " + prijavljeni_clan.prezime)
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
                    biblioteka.prikaz_svih_pozajmljenih_stavki_jednog_clana()
                elif unos == "5":
                    biblioteka.pozajmi_stavku(prijavljeni_clan)  
    except:
        print("Nepostojeci clan!")




