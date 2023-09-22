def uppCons(frase):
    i = 0
    while i < len(frase):
        frase = frase.split()
        if frase[i] not in 'aeiouAEIOU':
            frase[i].upper()
        i += 1
    return frase