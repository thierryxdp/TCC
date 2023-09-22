def posLetra(x,y,z):
    n=0
    p=1
    while n<len(x):
        
        if x[n]==y:
            
            if p==z:
                return n
            if p<z:              
                if x[n] in x[n+1:]:
                	p=p+1 
                else:                    
                 	return -1
        n=n+1