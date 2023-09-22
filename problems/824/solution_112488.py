def uppCons(frase):
    '''Recebe uma frase e a retorna com todas as
    consoantes em maísculo
    str -> str'''
    frase = frase.lower()
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxyz':
            frase[i] = frase[i].upper()
        i += 1
    return frase