def madia_matriz(matriz):
    '''funcao que, dada uma matriz de inteiros nao vazia, retorna a media de todos os numeros dela;
    list -> float'''
    soma=0
    for i in range(1,len(matriz)):
        for j in range(1,len(matriz[0])):
            soma=soma+matriz[i][j]
    return soma/(i*j)