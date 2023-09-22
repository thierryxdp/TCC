def uppCons(frase):
    '''uma função que recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsucas.
    str -> str'''
    contador = 0
    resposta = ''
    letra = ''
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxyzwç':
            letra = str.upper(frase[contador])
            resposta += letra
            contador += 1
        else:
            resposta += frase[contador]
            contador += 1
    return resposta