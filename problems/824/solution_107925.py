def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            frase.replace(frase[i], frase[i].upper)
        i += 1
    return frase