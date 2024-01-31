import math

#Eldöntés tétel:
"""def osztok(szam):
    lista=[]
    for i in range(2,round(math.sqrt),1):
        if szam % i == 0:
            lista.append(osztok)
    return lista

print(osztok(36))"""

def osztok (szam):
    osztok=2
    lista=[]
    while osztok <= math.sqrt(szam):
        if szam % osztok == 0:
            lista.append(osztok)
        osztok+=1
    return lista

print(osztok(10007))