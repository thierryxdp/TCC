def uppCons (frase):
    '''função que destaca as consoantes em uma frase; str -> str'''
    i = 0
    acumulador = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            acumulador = acumulador + str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyzç':
            acumulador = acumulador + frase[i]
        i = i + 1
    return acumulador