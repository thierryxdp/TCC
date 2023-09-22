def uppCons(x):    
    for n in x[range(len(x))]:        
        if n in "bcdfghjklmnpqrstvwxyz":
            return [str.lower(n)]