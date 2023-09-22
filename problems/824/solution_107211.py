def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas;
    str->str'''
    frase2 = ''
    i = 0
    cons = 'bcdfghjklmnpqrstvwxyz'
    while i<len(frase):
        letra=frase[i]
        if frase[i] in cons:
            letra = str.upper(frase[i])
        frase2 = frase2 + letra
        i = i + 1
    return frase2