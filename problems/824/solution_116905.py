def uppCons(f):
    ''
    prox=0
    nova=[]
    while prox<len(frase):
        if frase[prox]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(f[prox])
        prox=prox+1
    return nova