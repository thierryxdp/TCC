def uppCons(F):
    proximo = 0    
    F = F
    while proximo < len(F):
        if F[proximo] in 'bcdfghjklmnpqrstwxyz':
            F + str.upper(F[proximo])
            proximo = proximo + 1
        else:
            F + F[proximo]
            proximo = proximo + 1
    return F