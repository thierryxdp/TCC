def uppCons(frase0):
    '''função que recebe uma frase e retorna a frase com todas as suas consoantes em maiuscula;
    str->str'''
    indice = 0
    frase1 = ''
    while indice < len(frase0):
        if frase0[indice] in 'bcdfghjklmnpqrstvwxyz':
            frase1 = frase1 + str.upper(frase0[indice])
        else:
            frase1 = frase1
    indice = indice +1
    return frase1