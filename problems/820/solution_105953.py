def posLetra(x,y,z):
    
    n=0
    p=1
    while n<len(x):
        if x[n]==y :
           
            
            if p==z:
                return x.find(y,n,len(x))
            elif p<z:
                p=p+1
            
        elif x[n]!=y:

            n=n+1