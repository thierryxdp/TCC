# Consoantes em Maiúsculas
def uppCons(frase):
    '''Essa função recebe uma frase e retorna a mesma com todas as
    consoantes em maiúsculo;
    STR -> STR'''
    ffinal = ''
    i = 0
    while i in range(0,len(frase)):
        if str.lower(frase[i]) in 'bcdfghjklmnpqrstvwxyz':
            ffinal = ffinal + str.upper(frase[i])
        else:
            ffinal = ffinal + frase[i]
        i += 1
    return ffinal