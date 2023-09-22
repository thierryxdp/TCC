def filtraMultiplos (listainicial:list, n:int) -> list:
    """Função que irá filtrar a lista original e formar uma nova lista contendo todos os elementos da lista original que forem divisíveis por n.

    Parameters:
    listainicial: lista com números inteiros
    n: número inteiro

    Returns:
    lista final: lista com todos os valores da listainicial que são múltiplos de n
    """

    posicao = 0
    listafinal = []
    while posicao < len(listainicial):
        if listainicial[posicao]%n == 0:
            listafinal = listafinal + [listainicial[posicao]]
        posicao = posicao + 1
    return listafinal