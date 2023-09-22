def uppCons(frase):
    '''str --> str'''
    i = 0
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOU':
            frase[i] = frase[i].upper()
        i = i+1
    return frase