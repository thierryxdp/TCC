def uppCons(a):
    proximo = 0
    while proximo < len(a):
        if a[proximo] in 'bcdfghjklmnpqrstwxyz':
            a + str.upper(a[proximo])
            proximo = proximo + 1
        elif a[proximo] in 'aeiou AEIOUBCDFGHJKLMNPQRSTQXYZ':
            a + a[proximo]
            proximo = proximo + 1
    return a