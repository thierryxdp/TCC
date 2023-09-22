def uppCons(x):    
    consoantes = "bcdfghjklmnpqrstvwxyz"
    for n in x:
        if n in consoantes:
            str.upper(n)
            return x