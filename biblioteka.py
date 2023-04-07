from status import Status
from stavka import Stavka
from knjiga import Knjiga
from clan import Clan
from transakcija import Transakcija
from transakcija import TipTransakcije
import json
import os
from tip_stavka import TipStavka

class Biblioteka:
    def __init__ (self):
        self.stavke: list[Stavka] = []
        self.clanovi: list[Clan] = []

    def ucitaj_stavke(self) -> None:
        f = open("stavke.json", "r")
        ucitane_stavke: list[dict] = json.load(f)
        f.close()

        for ucitana_stavka in ucitane_stavke:
            if ucitana_stavka["tip"] == TipStavka.KNJIGA.name:
                knjiga = Knjiga(
                    status=ucitana_stavka["status"],
                    autor=ucitana_stavka["autor"],
                    izdavac=ucitana_stavka["izdavac"],
                    naslov=ucitana_stavka["naslov"],
                    id=ucitana_stavka["id"]
                )

                self.stavke.append(knjiga)
            else:
                raise Exception("Nepostojeca stavka!")
        
        
     
    def ucitaj_clanove(self) -> None:
        f = open ("clanovi.json", "r")
        ucitani_clanovi: list[dict] = json.load(f)
        f.close()

        for ucitani_clan in ucitani_clanovi:
            clan = Clan(
                id=ucitani_clan["id"],
                ime=ucitani_clan["ime"],
                prezime=ucitani_clan["prezime"],
                pozajmljene_stavke=ucitani_clan["pozajmljene_stavke"]
            )

            self.clanovi.append(clan)

    def ispisi_stavke (self) -> None:
        for stavka in self.stavke:
            if isinstance(stavka, Knjiga):
                print("--------------------------")
                print("Naslov knjige: " + stavka.naslov)
                print("Naziv autora: " + stavka.autor)
                print("Naziv izdavaca: " + stavka.izdavac)
                print("Dostupnost: " + stavka.status)
                if stavka.status == Status.ZAUZET.name:
                    clan = next(filter(lambda clan: stavka.id in clan.pozajmljene_stavke, self.clanovi))

                    if isinstance(clan, Clan):
                        print ("Trenutno kod clana: " + clan.ime + " " + clan.prezime)
                    else:
                        raise Exception("Nepostojeci clan!")

    def prikaz_svih_dostupnih_stavki(self) -> None:
        """
        Ispis svih dostupnih stavki u biblioteci.
        """
        for stavka in self.stavke:
            if isinstance (stavka,Knjiga):
                if stavka.status == Status.SLOBODAN.name:
                    print("--------------------------")
                    print ("Naslov knjige: " + stavka.naslov)
    
    def prikaz_svih_clanova(self) -> None:
        for clan in self.clanovi:
            print ("Ime: " + clan.ime + ", Prezime: " + clan.prezime) 

    def prikaz_svih_pozajmljenih_stavki_jednog_clana(self) -> None:
        os.system("cls")
        for index, clan in enumerate(self.clanovi):
            print(str(index + 1) + ". " + clan.ime + " " + clan.prezime)

        try:
            unos = int(input("Izaberite clana: "))

            if unos <= len(self.clanovi) and unos > 0:
                izabrani_clan = self.clanovi[unos - 1]
                knjige = filter(lambda stavka: stavka.id in izabrani_clan.pozajmljene_stavke, self.stavke)

                for knjiga in knjige:
                    print("Naslov knjige: " + knjiga.naslov)
            else:
                raise

        except:
            print("Nije dobar unos!")
            input("Pritisnite ENTER da nastavite...")
            os.system("cls")

    def pozajmi_stavku(self, prijavljeni_clan: Clan) -> None:
        os.system("cls")
        self.prikaz_svih_dostupnih_stavki()
        unos = input("Unesi ime stavke: ")
        try:
            stavka = next(filter(lambda stavka: unos == stavka.naslov, self.stavke))
            if isinstance(stavka, Knjiga):
                try:
                    stavka.status = Status.ZAUZET
                    f = open("stavke.json", "w")
                    stavke_json = json.dumps(self.stavke, default=lambda o: o.__dict__, indent=4)
                    f.write(stavke_json)
                    f.close()

                    prijavljeni_clan.pozajmljene_stavke.append(stavka.id)
                    f = open("clanovi.json", "w")
                    clanovi_json = json.dumps(self.clanovi, default=lambda o: o.__dict__, indent=4)
                    f.write(clanovi_json)
                    f.close()

                    transakcija = Transakcija(stavka, prijavljeni_clan, TipTransakcije.POZAJMICA)
                    transakcija.snimi_transakciju_pozajmica()
                    print("Pozajmljena knjiga: " + stavka.naslov)
                except Exception as e:
                    print("Problem kod pozajmljivanja stavke")
        except:
            print("Ne postoji izabrana knjiga")
       


        



