def uppCons(x): 
    y= ''
    consoantes = "bcdfghjklmnpqrstvwxyz"
    for n in x:
        if n in consoantes:
            return n.upper()