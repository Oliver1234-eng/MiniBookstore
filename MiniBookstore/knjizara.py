import knjige

def prikaziMeni():
    print("\n1) Listanje knjiga")
    print("2) Dodavanje knjige")
    print("3) Izlaz")

def main():
    knjige.ucitaj("knjige.txt")
    print("Dobrodosli u knjizaru")
    izbor = ""
    while izbor != "3":
        prikaziMeni()
        izbor = input("\nOdaberite opciju: ")
        if izbor == "1":
            knjige.prikaziSve()
        elif izbor == "2":
            print("Dodajemo knjige")
            knjiga = knjige.unesiKnjigu()
            uspesnoDodavanje = knjige.dodajKnjigu(knjiga)
            if uspesnoDodavanje:
                knjige.snimi("knjige.txt")
                print("Knjiga je uspesno dodata")
            else:
                print("Postoji knjiga sa tim id-em")
        elif izbor == "3":
            print("Dovidjenja")
        else:
            print("Nepoznata komanda")

if __name__ == "__main__":
    main()