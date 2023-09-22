def uppCons(frase):
    i = 0
    r = ''
    while i <len(frase):
        if frase[i] not in 'aeiou':
            str.upper(frase[i])
            i = i + 1
return frase