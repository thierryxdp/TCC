def uppCons(frase):
    frase = ''
    i = 0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase = frase + str.upper(frase[i])
        else:
            frase = frase + frase[i]
        i = i + 1
    return frase