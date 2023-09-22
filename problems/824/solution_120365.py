def uppCons(x):
    nf= []
    for n in range(len(x)):
        if x[n] in "bcdfghjklmnpqrstvwxyz":  
            nf= x.append(x[n].upper())
        return nf