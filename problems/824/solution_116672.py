def uppCons(frase):
    '''função que dada uma frase, retorna a frase com todas as 
    consoantes em maiusculo. str --> str'''
    fraseupp = ''
    indice = 0
    while indice < len(frase):
        letra = frase[indice]
        if letra in 'bcdfghjklmnpqrstvwxyz':
            letra = str.upper(letra)
        fraseupp =fraseupp + letra
        indice = indice + 1
    return fraseupp