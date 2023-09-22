def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz
    list->floot'''
    C=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(C,matriz[i][j])
    L=sum(C)/len(C)
    return round(L,2)