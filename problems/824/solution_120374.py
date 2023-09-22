def uppCons(x): 
    y= ''
    consoantes = "bcdfghjklmnpqrstvwxyz"
    for n in x:
        if n in consoantes:
            y+= n.upper()
        return y