def posLetra(x,y,z):
    
    n=0
    p=1
    while n<len(x):
        if p<z:
            p=p+1
        if p==z:
           return x[range(n,len(x))].find(y)
        else:
            n=n+1