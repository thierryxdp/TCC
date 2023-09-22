def uppCons(frase):
    '''A função recebe uma frase e a retorna com as consoantes maiúsculas.
str -> str'''
    i2 = 0
    conso = ''
    while i2 < len(frase):
        if frase[i2] not in 'bcdfghjklmnpqrstvwxyzç':
            conso = conso + frase[i2].upper()
        else:
            conso = conso + frase[i2]
        i2 = i2+1
    return conso