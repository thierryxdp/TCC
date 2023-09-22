def melhor_volta(matriz):
    '''Função que recebe uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta
    e que retorna uma tupla;
    list->tupla'''
    menor=100
    for L in range(len(matriz)):
        for C in range(len(matriz[L])):
            if matriz[L][C]<menor:
                menor=matriz[L][C]
                linha=L
                coluna=C
    return linha+1,menor,coluna+1