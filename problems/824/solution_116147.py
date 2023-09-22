def uppCons(frase):
    proximo = 0
    frase = frase
    while proximo < len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstwxyz':
            str.upper(frase[proximo])
            proximo = proximo + 1
        else:
            proximo = proximo + 1
    return frase