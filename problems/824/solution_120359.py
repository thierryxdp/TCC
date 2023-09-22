def uppCons(x):
    for n in range(len(x)):
        if x[n] in "bcdfghjklmnpqrstvwxyz":            
            x[n].upper()
        return x