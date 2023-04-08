class Clan:
    def __init__ (self,id:int ,ime:str ,prezime:str , pozajmljene_stavke: list[int]):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.pozajmljene_stavke = pozajmljene_stavke

    def clan_to_dict(self):
        clan = {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "pozajmljene_stavke": self.pozajmljene_stavke
        }
        
        return clan