def uppCons(frase):
    posicao = 0
    modificada = ''
    while posicao < len(frase):
        if frase[posicao] not in 'aeiouAEIOU':
            modificada = modificada + frase[posicao].upper()
        else:
            modificada = modificada + frase[posicao]
    	posicao = posicao + 1
    return modificada