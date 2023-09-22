def uppCons(frase):
    '''Transforma todas as consoantes de uma frase em
    maiúsculas
    str -> str'''
    i = 0
    novafrase = ''
    while i<len(frase):
        if frase[i] == 'A' or 'E' or 'I' or 'O' or 'U':
            novafrase += str.lower(frase[i])
        else:
            novafrase += str.upper(frase[i])
        i = i+1
    return novafrase