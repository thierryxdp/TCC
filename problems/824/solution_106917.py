def uppCons(frase):
    '''uma função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsucas.
    str -> str'''
    contador = 0
    acumulador = frase[::]
    while contador < len(frase):
        if acumulador[contador] in 'bcdfghjklmnpqrstvxyzw':
            acumulador == str.upper(acumulador[contador])
            contador += 1
        else:
            contador += 1
    return acumulador