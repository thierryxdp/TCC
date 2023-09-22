def uppCons(F):
    proximo = 0
    frase = ''
    while proximo < len(F):
        if F[proximo] in 'bcdfghjklmnpqrstwxyzv':
            frase = frase + str.upper(F[proximo])
            proximo = proximo + 1
        else:
            frase = frase + F[proximo]
            proximo = proximo + 1
    return frase