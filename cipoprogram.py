from Cipo import Cipo
import math

peldany1=Cipo("Nike",42)
peldany2=Cipo("Adidas",41)
peldany3=Cipo("Adidas",45)

cipok=[]
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)
for i in range(0,len(cipok),1):
    nev = cipok[i].nev
    meret = cipok[i].meret
    print(f"{nev} ({meret})")

def cipo_atlag():
    ossz:int=0
    for i in range(0,len(cipok),1):
        ossz += cipok[i].meret
    print(round(ossz / len(cipok),3))

cipo_atlag()


def nagyobb42adidas():
    print("Van 42-nél nagyobb Adidas:", end="")
    van = False
    for i in range(0,len(cipok),1):
        if cipok[i].nev == "Adidas" and cipok[i].meret:
            van = True
    if van == True:
        print("Van")
    else:
        print("Nincs")

nagyobb42adidas()



