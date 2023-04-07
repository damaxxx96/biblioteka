from status import Status
from stavka import Stavka
from knjiga import Knjiga
from clan import Clan
import json

from tip_stavka import TipStavka

class Biblioteka:
    def __init__ (self):
        self.stavke: list[Stavka] = []
        self.clanovi: list[Clan] = []

    def ucitaj_stavke(self) -> None:
        f = open("stavke.json", "r")
        ucitane_stavke: list[dict] = json.load(f)

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

    def prikaz_svih_pozajmljenih_stavki_jednog_clana(self, clan: Clan) -> None:
        knjige = filter(lambda stavka: stavka.id in clan.pozajmljene_stavke, self.stavke)

        for knjiga in knjige:
            print("Naslov knjige: " + knjiga.naslov)



