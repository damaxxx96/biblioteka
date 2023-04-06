from biblioteka import Biblioteka

biblioteka = Biblioteka()
biblioteka.ucitaj_stavke()
biblioteka.ucitaj_clanove()
while True:
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
    if unos == "1":
        biblioteka.ispisi_stavke()

