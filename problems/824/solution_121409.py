def uppCons(frase):
    i = 0
    r = ''
    while i <len(frase):
        if frase[i] not in 'aeiou':
            r = r + str.upper(frase[i])
            i = i + 1
    return r