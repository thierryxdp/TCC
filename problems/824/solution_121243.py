def uppCons(frase):
    '''funçao dada um frase retorna essa frase com as consoantes maisculas
    str -> str'''
    f_maiscula = ''
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyz':
            f_maiscula += str.upper(frase[contador])
            contador += 1
        else:
            f_maiscula += frase[contador]
            contador += 1
    return f_maiscula