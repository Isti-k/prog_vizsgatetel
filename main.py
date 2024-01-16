def feladat():
    n=int(input("N="))
    while n < 0:
        ossz=0
    
    for i in range(0,n+1,1):
        ossz+=i
    
    print(f"Az első {n}db természetes szám összege:{ossz}")