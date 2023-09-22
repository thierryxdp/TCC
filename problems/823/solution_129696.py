def faltante(lista):
    """..."""
    posicao = 0
    resposta = []
    while posicao < len(lista):
        if lista[posicao] - lista[posicao - 1] !=1:
            list.append(resposta, lista[posicao] - 1)
        posicao = posicao + 1
    return resposta