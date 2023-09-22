def media_matriz(matriz):
    '''retorna a media de todos os numeros de uma matriz
list-->int'''
    for i in matriz:
        for j in i:
            return sum(j)/len(i)