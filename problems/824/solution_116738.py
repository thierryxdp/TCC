def uppCons(frase):
    ''' Uma função que transforma todas consoantes de uma string em maiusculas
    str -> str'''
    contador = 0
    resposta =''
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