def uppCons(x): 
    y= ''
    consoantes = "bcdfghjklmnpqrstvwxyz"
    for n in range(len(x)):
        if x[n] in consoantes:
            c= n.upper()
            y += c
    return y