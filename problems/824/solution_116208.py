def uppCons(F):
    proximo = 0
    frase = ''
    while proximo < len(F):
        if f[proximo] in 'bcdfghjklmnpqrstwxyz':
            frase = frase + str.upper(F[proximo])
            proximo = proximo + 1
        else:
            frase = frase + F[proximo]
            proximo = proximo + 1
    return frase