from status import Status
from tip_stavka import TipStavka

class Stavka:
    def __init__(self, status: Status, naslov: str, id:int, tip: TipStavka):
        self.naslov = naslov
        self.status = status
        self.id = id
        self.tip = tip
