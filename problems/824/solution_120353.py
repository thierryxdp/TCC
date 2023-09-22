def uppCons(x): 
    for n in range(len(x)):
        if x[n] in "bcdfghjklmnpqrstvwxyz":
            str.upper(x[n])