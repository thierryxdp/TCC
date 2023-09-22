def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia de entrada,retorna a média de todos os números da matriz com apenas duas casas decimais'''
    soma = 0
    divisor = len(matriz)*len(matriz[0])
    for n in range(len(matriz)):
        soma += sum(matriz[n])
    return round(soma / divisor,2)