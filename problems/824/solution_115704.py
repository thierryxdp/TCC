def uppCons(f):
    r = ''
    for i in f:
        if i in 'BCDFGHJKLMNPQRSTVWYXZ':
            r = r + i.upper()
        else:
            r = r + i
    return r