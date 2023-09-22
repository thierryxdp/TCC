def uppCons(x):
    a=''
    for h in x:
        if h in 'bcdfghjklmnpqrstvwxyzç':
            a += h.upper()
        else:
            a +=h
    return a