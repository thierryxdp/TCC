def uppCons(x): 
    y= ''
    consoantes = "bcdfghjklmnpqrstvwxyz"
    for n in range(len(x)):
        if x[n] in consoantes:
            c= x[n].upper()
            y += c
    return y