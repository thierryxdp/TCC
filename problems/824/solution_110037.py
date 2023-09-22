def uppCons(frase):
    frase = frase
    x = 0
    i = 0
    lista = list(frase)
    while len(frase) > x:
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase[i] = frase[i].upper
        x += 1
        i += 1
    return frase