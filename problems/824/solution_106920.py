def uppCons(frase):
    '''uma função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsucas.
    str -> str'''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxyzw':
            str.upper(frase[contador])
            contador += 1
        else:
            contador += 1
    return frase