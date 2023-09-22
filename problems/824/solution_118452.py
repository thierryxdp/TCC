def uppCons(frase):
    '''Função que retorna a frase de entrada com
    todas as consoantes em letras maiúsculas (as
    vogais se mantém da forma que foram inseridas)
    str -> str'''
    i = 0
    p = ''
    while i<len(frase):
        if 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ' in frase[i]:
            str.join(str.upper(frase[i],p))
            i = i + 1
    return p