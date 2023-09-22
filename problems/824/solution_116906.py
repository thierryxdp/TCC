def uppCons(f):
    ''
    prox=0
    while prox<len(frase):
        if frase[prox]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(f[prox])
        prox=prox+1
    return f