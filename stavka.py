from status import Status

class Stavka:
    def __init__(self, status: Status, naslov: str, id:int ):
        self.naslov = naslov
        self.status = status
        self.id = id
