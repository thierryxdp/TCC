def uppCons(frase):
    '''Transforma todas as consoantes de uma frase em
    maiúsculas
    str -> str'''
    i = 1
    novafrase = str.upper(frase)
    while i<len(novafrase):
        if novafrase[i] == 'A' or 'E' or 'I' or 'O' or 'U':
            frasefinal = novafrase[0:i] + str.upper(novafrase[i]) novafrase[i+1:]
        i = i+1
    return frasefinal