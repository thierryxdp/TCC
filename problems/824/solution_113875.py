def uppCons(x):
    i = 0
    while i < len(x):
        if x[i] in 'bcdfghjklmnpqrstwxyz':
            str.upper(x[i])
        i += 1
    return x