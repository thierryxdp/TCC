def media_matriz (matriz):
    '''função em que dada uma matriz de inteiros não vazia, retorna a média de
    todos os números da matriz com duas casas decimais de precisão;
    list -> float'''
    s=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] in matriz[i]:
                s+=matriz[i][j]
    return round((s/(len(matriz)*len(matriz[0]))),2)