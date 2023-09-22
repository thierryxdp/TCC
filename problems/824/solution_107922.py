def uppCons(frase):
    i = 0
    frase = frase.strip()
    frase = str.split(frase)
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            frase[i].upper()
        i += 1
    return ''.join(frase)