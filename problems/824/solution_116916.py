def uppCons(f):
    ''
    n=''
    prox=0
    while prox<len(f):
        if f[prox]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(f[prox])
            n=n+f[prox]
        else:
            n=n+f[prox]
        prox=prox+1
    return n