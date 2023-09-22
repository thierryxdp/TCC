def media_matriz(matriz):
    '''funçao dado uma matriz retorna a media de todos os numero dela
    list -> float'''
    soma = 0
    quantidade = 0
    for indice in matriz:
        if type(indice) == list:
            for elemento in indice:
                soma += indice
                quantidade += 1
        soma += indice
        quantidade += 1
    return round(soma/quantidade, 2)