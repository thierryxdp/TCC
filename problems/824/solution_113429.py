def uppCons (frase):
    ''''''
    frasefinal = ''
    i = 0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            str.upper(frase[i])
        frasefinal = frasefinal + frase[i]
        i += 1
    return frasefinal