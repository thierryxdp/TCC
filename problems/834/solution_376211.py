def media_matriz(matriz):
    """Essa funcao recebe uma matriz nao vazia e faz a
       media de todos elementos dela.

       list, -> float"""

    soma = 0
    qtd_elementos = 0

    for i in matriz:
        for elemento in i:
            soma += elemento
            qtd_elementos += 1
    return round((soma/qtd_elementos),2)