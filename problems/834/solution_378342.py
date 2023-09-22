def media_matriz(matriz):
    '''Dada uma lista de sub-listas que representa uma matriz
    de números inteiros, retorna a média de todos o números da
    matriz com 2 casa decimais de precisão.
    list -> floaa'''
    
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return round(soma/(len(matriz)*len(matriz[0])),2)