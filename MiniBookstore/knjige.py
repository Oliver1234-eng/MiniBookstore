lista_knjiga = []

def dodajKnjigu(knjiga):
    for tmp_knjiga in lista_knjiga:
        if tmp_knjiga['id'] == knjiga['id']:
            return False
    lista_knjiga.append(knjiga)

    return True

def unesiKnjigu():
    knjiga = {}
    id = input("Unesite id knjige: ")
    knjiga['id'] = id
    naziv = input("Unesite naziv knjige: ")
    knjiga['naslov'] = naziv
    autor = input("Unesite autora knjige: ")
    knjiga['autor'] = autor
    izdavac = input("Unesite izdavaca: ")
    knjiga['izdavac'] = izdavac
    cena = input("Cena: ")
    knjiga['cena'] = cena
    kolicina = input("Kolicina: ")
    knjiga['kolicina'] = kolicina
    godina = input("Godina izdavanja: ")
    knjiga['godina'] = godina

    return knjiga
    
def knjiga2Str(knjiga):
    s = knjiga['id'] + "|" + knjiga['naslov'] + "|" + knjiga['autor'] + "|" + knjiga['izdavac'] + "|" + knjiga['cena'] + "|" + knjiga['kolicina'] + "|" + knjiga['godina']

    return s

def str2Knjiga(red):
    knjiga = {}
    deo = red.strip().split("|")
    knjiga['id'] = deo[0]
    knjiga['naslov'] = deo[1]
    knjiga['autor'] = deo[2]
    knjiga['izdavac'] = deo[3]
    knjiga['cena'] = deo[4]
    knjiga['kolicina'] = deo[5]
    knjiga['godina'] = deo[6]

    return knjiga

def snimi(nazivFajla):
    target = open(nazivFajla, "w")
    for knjiga in lista_knjiga:
        target.write(knjiga2Str(knjiga) + "\n")
    target.close()

def ucitaj(nazivFajla):
    target = open(nazivFajla, "r")
    for red in target.readlines():
        lista_knjiga.append(str2Knjiga(red))
    target.close()

def prikaziSve():
    print("id  naslov  autor  izdavac  cena  kolicina  godina")
    print("--------------------------------------------------")
    for knjiga in lista_knjiga:
        print(str(knjiga["id"]).ljust(4) + knjiga["naslov"][:7].ljust(8) 
        + knjiga["autor"][:6].ljust(7) + knjiga["izdavac"][:8].ljust(9) 
        + str(knjiga["cena"])[:5].ljust(6) + str(knjiga["kolicina"])[:9].ljust(10) 
        + str(knjiga["godina"])[:7].ljust(8))
    print("\n")