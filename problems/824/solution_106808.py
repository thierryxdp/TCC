def uppCons(frase):
    posicao = 0
    while posicao < len(frase):
        x = frase[posicao]
        if x in 'QWRTYPSDFGHJKLÇZXCVBNMqwrtypsdfghjklçzxcvbnm':
            frase = frase.replace(x,str.upper(x))
        posicao = posicao + 1
    return frase