def posLetra(x,y,z):
    n=0
    p=1
    while n<len(x):
        if x[n]==y:
           if p<z:
              p=p+1
           elif p==z:
              return x
        elif x[n]!=y:
            n=n+1
        
    return x.index(n)