def uppCons(x):
    a=''
    for h in x:
        if h in 'bcdghjklmnpqrstvwxyzç':
            a += h.upper()
        else:
            a +=h
    return a