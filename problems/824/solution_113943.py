def uppCons(x):
    i = 0
    strFinal = ''
    while i < len(x):
        if x[i] in 'bcdfghjklmnpqrstwxyz':
            str.upper(str(x[i]))
        i += 1
    return x