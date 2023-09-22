def media_matriz(matriz):
    '''Função que, dada uma matriz de inteiros não vazia, retorna a
    média de todos os números da matriz.
    lista -> int'''
    soma=0
    num_elementos=0
    for i in range(len(matriz)):    
        soma+=sum(matriz[i])
        num_elementos+=len(matriz[i])
    return round(soma/num_elementos, n)