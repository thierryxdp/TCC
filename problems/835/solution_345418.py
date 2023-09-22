def melhor_volta(matriz):
    '''Função conta e retorna a quantidade de ocorrencia do numero de entrada em uma matriz.
    int, matriz->int'''
    lista=[]
    for i in range (6): #linhas
        for j in range (10): #colunas
            lista.append(matriz[i][j]) #Insere cada elemento em uma lista só
    melhorVolta=min(lista)
    for i in range (6): #linhas
        for j in range (10): #colunas
            if matriz[i][j]==melhorVolta
            return (i,melhorVolta,j)