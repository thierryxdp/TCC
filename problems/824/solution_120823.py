def uppCons(f):
    s = ''
    for c in f:
        if c in 'bcdfghjklmnpqrstvxwyzç':
            s += c.upper() 
        else: 
            s += c
    return s