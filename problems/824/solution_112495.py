def uppCons(frase):
    '''Recebe uma frase e a retorna com todas as
    consoantes em maísculo
    str -> str'''
    frase = frase.lower()
    frase_cons = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxyz':
            frase_cons = frase[i].upper()
        else:
            frase_cons = frase[i]
        i += 1
    return frase