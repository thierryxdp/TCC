def uppCons(frase):
    i = 0
    r = ''
    while i <len(frase):
        if frase[i] not in 'aeiou':
            r = str.upper(frase[i])
            f = frase [i]
            str.replace(f,r,1)
            i = i + 1
    return frase