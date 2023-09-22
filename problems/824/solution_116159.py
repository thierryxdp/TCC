def uppCons(F):
    proximo = 0
    
    a = ''
    while proximo < len(F):
        if F[proximo] in 'bcdfghjklmnpqrstwxyz':
            a + str.upper(F[proximo])
            proximo = proximo + 1
        else:
            a + F[proximo]
            proximo = proximo + 1
    return a