def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase = frase + str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyz':
            frase = frase + frase[i]
        i = i + 1
    return frase