def uppCons(x):
    y=()
    for n in x:
        if n in "bcdfghjklmnpqrstvwxyz":            
            y= str.upper(n)
    return y