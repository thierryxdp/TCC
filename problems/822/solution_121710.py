def repetidos(lista):
    """Este código recebe uma lista de números, e informe a quantidade
    de numeros que se repetem na lista
    Recebe: list
    Retorna: int"""
    repetidos = []
    posicao = 0
    
    while posicao < len(lista):
        if lista[posicao] == lista[posicao-1]:
            list.append(repetidos, 1)
        posicao = posicao + 1
    return sum(repetidos)