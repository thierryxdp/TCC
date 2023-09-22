uppCons(frase):
    '''funcao que recebe uma frase de entrada e retorna essa mesma frase com todas as consoantes em letras maiusculas;
    str -> str'''
    i = 0
    f = ' '
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            f = f + str.upper(frase[i])
        i = i + 1
    return f