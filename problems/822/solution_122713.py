def repetidos(lista):
    """..."""
    vezes_repetidas = 0
    posicao = 0
    
    while posicao < len(lista) - 1 :
        if lista[posicao] ==  lista[posicao + 1]:
            vezes_repetidas = vezes_repetidas + 1
        posicao = posicao  + 1
    return vezes_repetidas