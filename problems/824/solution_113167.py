def uppCons(frase):
    '''str --> str'''
    i = 0
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            frase[i] = upper(frase[i])
        i = i+1
    return frase