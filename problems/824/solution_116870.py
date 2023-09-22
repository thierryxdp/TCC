def uppCons(frase0):
    '''função que recebe uma frase e retorna a frase com todas as suas consoantes em maiuscula;
    str->str'''
    i = 0
    frase1 = ''
    while i<len(frase0):
        if frase0[i] in 'bcdfghjklmnpqrstvwxyz':
            frase1 = frase1 + str.upper(frase0[i])
        else:
            frase1 = frase0
    i = i+1
    return frase1