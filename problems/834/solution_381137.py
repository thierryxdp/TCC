def media_matriz(matriz):
    '''Dada uma matriz não vazia retorna sua média
    list -> float'''
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista.append(matriz[i][j])
    return round(sum(lista)/len(lista),2)