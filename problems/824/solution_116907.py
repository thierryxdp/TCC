def uppCons(f):
    ''
    prox=0
    while prox<len(fras):
        if f[prox]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(f[prox])
        prox=prox+1
    return f