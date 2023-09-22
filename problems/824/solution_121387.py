def uppCons(frase):
    i = 0
    r = ''
    while i <len(frase):
        if frase[i] not in 'aeiou':
            frase = str.upper(frase[2])
            i = i + 1
    return frase