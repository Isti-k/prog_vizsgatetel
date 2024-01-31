
def szamok():
    also=42
    felso=67
    i=also
    while(i <= felso and not(i % 10 ==0)):
        i+=1
    
    van = i <= felso
    if(van):
        print(f"van 0-ra végződő szám:" + str(i))
    else:
        print(f"nics 0-ra végződő szám")

szamok()
