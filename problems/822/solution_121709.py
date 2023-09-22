def repetidos(lista):
    """..."""
    repetidos = []
    posicao = 0
    
    while posicao < len(lista):
        if lista[posicao] == lista[posicao-1]:
            list.append(repetidos, 1)
        posicao = posicao + 1
    return sum(repetidos)