def uppCons(x):
    y=""
    for n in range(len(x)):
        if x[n] in "bcdfghjklmnpqrstvwxyz":
            y= x[n].upper()
        return x