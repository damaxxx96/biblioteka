from enum import Enum
import datetime
from stavka import Stavka
from clan import Clan

class TipTransakcije(Enum):
    POVRAT = 1
    POZAJMICA = 2

class Transakcija:
    def __init__ (self, stavka: Stavka, clan: Clan, tip_transakcije: TipTransakcije):
        self.stavka = stavka
        self.clan = clan
        self.vreme_transakcije = datetime.datetime.now()
        self.tip_transakcije: TipTransakcije = tip_transakcije
        
    def snimi_transakciju(self):
        akcija = "pozajmio" if self.tip_transakcije == TipTransakcije.POZAJMICA else "vratio"

        f = open("transakcije.txt", "a")
        f.write("--------------------------\n")
        f.write("Clan " + self.clan.ime + " " + self.clan.prezime + " je " + akcija + " stavku " + self.stavka.naslov + '\n')
        f.write("Datuma " + str(self.vreme_transakcije) + '\n')
        f.write("--------------------------\n")
        f.close()
