def uppCons(frase):
    '''str -> str'''
    frase2 = ' '
    for i in range(len(frase)):
        if frase[i] in bcdfghjklmnpqrstvwxz:
            frase2 = frase2 + frase[i].upper()
        frase2 = frase2 + frase[i]
    return frase2