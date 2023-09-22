def uppCons(x):
    a = ''
    for c in x:
        if c in 'bcdfghjklmnpqrstvxwyzç':
            a +=str.upper(c)
        else:
            a += c
    return a