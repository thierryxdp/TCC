def uppCons(frase):
    i = 0
    r = ''
    while i <len(frase):
        if frase[i] not in 'aeiou':
            r = str.upper(frase[i])
            str.replace(frase[i],r,1)
            i = i + 1
    return frase