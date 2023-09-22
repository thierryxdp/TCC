def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxywz':
            frase = frase[i].upper()
        i = i + 1
    return frase