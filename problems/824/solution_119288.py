def uppCons(x):
    ab = ''
    for c in list(x):
        if c in 'bcdfghjklmnpqrstvxwyz':
            str.upper(c)
            return c
        else:
            ab + c
            return ab+c