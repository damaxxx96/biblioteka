from stavka import Stavka
from knjiga import Knjiga
from clan import Clan
from tip_stavke import TipStavke
import json

class Biblioteka:
    def __init__ (self):
        self.stavke: list[Stavka] = []
        self.clanovi: list[Clan] = []

    def ucitaj_stavke(self) -> None:
        f = open("stavke.json", "r")
        ucitane_stavke: list[dict] = json.load(f) 
        
        for ucitana_stavka in ucitane_stavke:
            if ucitana_stavka["tip"] == TipStavke.KNJIGA.name:
                knjiga = Knjiga(
                    status = ucitana_stavka["status"],
                    autor = ucitana_stavka["autor"],
                    izdavac = ucitana_stavka["izdavac"],
                    naslov = ucitana_stavka["naslov"],
                    id = ucitana_stavka["id"]
                )
                
                self.stavke.append(knjiga)
            else:
                raise Exception("Neispravna stavka!")
            
     
    def ucitaj_clanove(self) -> None:
        f = open ("clanovi.json", "r")
        ucitani_clanovi: list[dict] = json.load(f)
        
        for ucitani_clan in ucitani_clanovi:
            clan = Clan(
                ime = ucitani_clan["ime"],
                prezime = ucitani_clan["prezime"],
                pozajmljene_stavke = ucitani_clan["pozajmljene_stavke"],
                id = ucitani_clan["id"]
            )
            
            self.clanovi.append(clan)

    def ispisi_stavke (self) -> None:
        for stavka in self.stavke:
            if isinstance(stavka, Knjiga):
                print(stavka.naslov)
                print(stavka.autor)
                print(stavka.izdavac)
                print(stavka.status)
                if stavka.status == "ZAUZET":
                    clan = filter(lambda clan: stavka.id in clan.pozajmljene_stavke, self.clanovi)
                    print ("Trenutno kod clana: " + clan)

