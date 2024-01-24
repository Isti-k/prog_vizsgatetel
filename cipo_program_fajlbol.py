

from Cipo import Cipo

def pldListaban():
    cipok=[]
    fajl=open("cipok.txt", "r", encoding="utf-8")
    fajl.readline()
    fajl_lista=fajl.readlines()
    fajl.close()
    for i in range(0,len(fajl_lista),1):
        sor_lista=fajl_lista[i].strip()
        sor_lista=sor_lista.split(",")
        peldany=Cipo(sor_lista[0], int(sor_lista[1]))
        cipok.append(peldany)
    return cipok


    """peldany1=Cipo("Nike",42)
    peldany2=Cipo("Adidas",41)
    peldany3=Cipo("Adidas",45)

    
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    return cipok"""

def litsaKiir(lista):
    for i in range(0,len(lista),1):
        nev = lista[i].nev
        meret = lista[i].meret
        print(f"{nev} ({meret})")

#Rövid verzió
"""litsaKiir(pldListaban())"""

#Ez a hosszú verzió
cipok_lista=pldListaban()
litsaKiir(cipok_lista)


def osszegzes_tetele(cipok):
    ossz:int=0
    for i in range(0,len(cipok),1):
        ossz += cipok[i].meret
    print(round(ossz / len(cipok),3))




def maximum_kivalasztas_tetel(cipok):
    print("Melyik a legnagyobb márkájú cipő: ", end=" ")
    meret:int=0
    for i in range(0,len(cipok),1):
        if cipok[i].meret > meret:
            meret = cipok[i].meret        
    
    print(cipok[i].nev)


def megszamlalas_tetel(cipok):
    print("Hány db Adidas cipő van: ", end="")
    db:int=0
    for i in range(0,len(cipok),1):
        if cipok[i].nev == "Adidas":
            db+=1
    print(f"{db}db Adidas termék van.")


#eldöntés tétel
def eldontes_tetel(cipok):
    print("Van 42-nél nagyobb Adidas:", end=" ")
    van = False
    for i in range(0,len(cipok),1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van = True
    if van == True:
        print("Van")
    else:
        print("Nincs")


osszegzes_tetele(cipok_lista)
maximum_kivalasztas_tetel(cipok_lista)
megszamlalas_tetel(cipok_lista)
eldontes_tetel(cipok_lista)




