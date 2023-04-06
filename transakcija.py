from enum import Enum
import datetime
from stavka import Stavka
from clan import Clan

class TipTransakcije(Enum):
    POVRAT = 1
    POZAJMICA = 2

class Transakcija:
    def __init__ (self, stavka: Stavka,clan: Clan, tip_transakcije: TipTransakcije):
        self.stavka = stavka
        self.clan = clan
        self.vreme_transakcije = datetime.datetime.now()
        self.tip_transakcije: TipTransakcije = tip_transakcije
