from status import Status
from stavka import Stavka
from tip_stavka import TipStavka

class Knjiga(Stavka):
    def __init__ (self, status: Status, autor: str , izdavac: str , naslov: str, id: int):
        super().__init__(status, naslov, id, TipStavka.KNJIGA)
        self.autor = autor
        self.izdavac = izdavac

