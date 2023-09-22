def uppCons(x):
    y= []
    for n in x:
        if n in "bcdfghjklmnpqrstvwxyz":
            str.upper(x,n)
    return x