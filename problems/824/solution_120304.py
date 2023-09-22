def uppCons(x):
    y=()
    for n in x:
        if n in "bcdfghjklmnpqrstvwxyz":            
            y= y.append(n)
    return y