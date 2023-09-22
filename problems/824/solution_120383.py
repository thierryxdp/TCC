def uppCons(x): 
    y= ''
    consoantes = "bcdfghjklmnpqrstvwxyzç"
    for n in range(len(x)):
        if x[n] in consoantes:
            c= x[n].upper()
            y+= c
        else:
            y+= x[n]
    return y