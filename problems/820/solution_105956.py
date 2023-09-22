def posLetra(x,y,z):
    
    n=0
    p=1
    
    while n<len(x):
        if x[n]==y :
           
            
            if p==z:
                return n
            elif p<z:


                 if y in x[n:]:
                    p=p+1
                 else:
                    return -1 
                
                
           
        elif x[n]!=y:

            n=n+1