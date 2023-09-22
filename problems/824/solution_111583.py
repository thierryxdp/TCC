def uppCons(frase):
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] in 'bcdfghjklmnopqrstvwxyz':
            str.upper(frase[proximo])
        proximo = proximo + 1
    return frase