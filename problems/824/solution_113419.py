def uppCons (frase):
    ''''''
    i = 0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            str.upper(frase[i])
        i += 1
    return frase