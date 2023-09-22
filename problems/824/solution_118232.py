def uppCons(frase):
    i = 0
    while frase[i] in 'bcdfghjklmnpqrstvxwyz':
        frase[i] = frase[i].upper
    i = i + 1
    return frase