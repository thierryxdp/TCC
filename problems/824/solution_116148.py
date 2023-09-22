def uppCons(frase):
    proximo = 0
    a = ''
    while proximo < len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstwxyz':
            a + str.upper(frase[proximo])
            proximo = proximo + 1
        else:
            a + frase[proximo]
            proximo = proximo + 1
    return a