def uppCons(F):
    proximo = 0    
    F = a
    while proximo < len(F):
        if F[proximo] in 'bcdfghjklmnpqrstwxyz':
            a + str.upper(F[proximo])
            proximo = proximo + 1
        else:
            F + F[proximo]
            proximo = proximo + 1
    return a