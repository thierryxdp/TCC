def conta_numero(numero, matriz):
    '''Função conta e retorna a quantidade de ocorrencia do numero de entrada em uma matriz.
    int, matriz->int'''
    lista=[]
    for i in range (len(matriz)): #linhas
        for j in range (len(matriz[0])): #colunas
            lista.append(matriz[i][j]) #Insere cada elemento em uma lista só
    return lista.count(numero)