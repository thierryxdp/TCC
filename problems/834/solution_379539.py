def media_matriz(matriz):
    '''funçao que dada uma matriz de inteiros não vazia,retorna a média de todos os numeros contidos na matriz com 2 casas de precisão;list -> float'''
    qtd = len(matriz) * len(matriz[0])
    soma = []
    for i in matriz:
        list.append(soma.sum(i))
    return round ((sum(soma)/qtd), 2)