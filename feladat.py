import math



def feladat():
    n=int(input("N="))
    while (n < 0):
        ossz=0
        
    for i in range(0,n+1,1):
        ossz+=i
        
    print(f"Az első {n}db természetes szám összege:{ossz}")

def feladat2():
    print("\nszám")
    n:int=int(input("N="))
    if (n<2):
        prim=False
    else:
        i=2
        while(i<=math.sqrt(n) and n%i !=0):
            i+=1
        prim=i>math.sqrt(n)
    
    print(prim)


