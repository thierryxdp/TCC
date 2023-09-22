def media_matriz(matriz):
    """ dado uma matriz de inteiros não vazia, retorna a média de todos os números da matriz.
    entrada matriz -> saida intero. """
   	
    qtd_elementos = len(matriz)* len(matriz[0])
    total = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total = total + matriz[i][j]
    return range(total/qtd_elementos, )