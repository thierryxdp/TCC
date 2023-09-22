def uppCons(frase):
    proximo = 0
    a = ''
    while proximo < len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstwxyz':
            a + str.upper(frase[proximo])
            proximo = proximo + 1
        elif frase[proximo] in 'aeiou AEIOUBCDFGHJKLMNPQRSTQXYZ':
            a + frase[proximo]
            proximo = proximo + 1
    return a