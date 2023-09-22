def uppCons(x): 
    for n in x:
        if n in "bcdfghjklmnpqrstvwxyz":            
            x= str.upper(n)
    return x