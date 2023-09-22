def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas as consoantes em letra maiúscula.'''
    '''str->str'''
    i = 0
    consoantes = ""
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZçÇ":
            consoantes = str.replace(frase, frase[i], str.upper(frase[i]))
            frase = consoantes
        i = i + 1
    return frase