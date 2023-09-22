def uppCons(x): 
    for n in x:
        if n in "bcdfghjklmnpqrstvwxyz":
            return "bcdfghjklmnpqrstvwxyz".upper()
    return x