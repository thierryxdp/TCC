def uppCons(frase):
    posicao = 0
    while posicao < len(frase):
        x = frase[posicao]
        a = str.upper(x)
        if x in 'QWRTYPSDFGHJKLÇZXCVBNMqwrtypsdfghjklzxcvbnm':
            frase.replace(x,a)
        posicao = posicao + 1
    return frase