def media_matriz(matriz):

    """ Função que calcula a media de uma matriz. Assim quando tinhamos valores
        inteiros e queríamos a média entre eles, a média da matriz é feita
        calculando a soma entre todos os termos e a dividindo pela quantidade
        de termos na matriz.
        list -> float
    """

    soma = 0
    qtd_numeros = len(matriz)*len(matriz[0])

    for m in range(len(matriz)):
        for n in range(len(matriz[0])):

            soma = soma + matriz[m][n]
            
    return round(soma/qtd_numeros,2)