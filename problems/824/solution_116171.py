def uppCons(frase):
    proximo = 0
    frase = frase
    while proximo < len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstwxyz':
            frase + str.upper(frase[proximo])
            proximo = proximo + 1
        elif frase[proximo] in 'aeiou AEIOUBCDFGHJKLMNPQRSTQXYZ':
            frase + frase[proximo]
            proximo = proximo + 1
    return frase