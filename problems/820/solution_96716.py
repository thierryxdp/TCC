def posLetra(frase,letra,pos):
    """ Essa função retorna a posição da letra recebida
    no argumento da função. str,str,int->int"""
    posicao = 0
    while frase[posicao] < len(frase):
        if letra in frase:
            frase1 = str.find(letra,pos)
    return frase1
else:
    return -1