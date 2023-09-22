def media_matriz(matriz):
    ''' função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão).
    Entrada: list;
    Saída: int'''
    contador = 0
    divisor = len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            contador = contador + matriz[i][c]
    return contador/divisor