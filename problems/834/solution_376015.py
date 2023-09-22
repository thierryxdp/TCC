def conta_numero(matriz):
    '''Função que retorna a média de todos os números de uma matriz de entrada.
    int, matriz->int'''
    lista=[]
    for i in range (len(matriz)): #linhas
        for j in range (len(matriz[0])): #colunas
            lista.append(matriz[i][j]) #Insere cada elemento em uma lista só
 	return (sum(lista))/(len(lista))