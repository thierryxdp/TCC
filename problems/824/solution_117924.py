def uppCons(frase):
    '''retorna a frase com todas as consoantes maisculas
str -> str'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
    i=i+1
    return frase