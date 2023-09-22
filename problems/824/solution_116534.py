def uppCons(frase):
    '''Transforma todas as consoantes de uma frase em
    maiúsculas
    str -> str'''
    i = 0
    novafrase = ''
    while i<len(frase):
        if frase[i] != 'a' or != 'e' or != 'i' or != 'o' or != 'u':
            novafrase += str.upper(frase[i])
        i = i+1
    return novafrase