def media_matriz(matriz):
    '''funcao que calcula a media dos termos da matriz. list->float'''
    cont=0
    cont2=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            cont+=1
            cont2+=matriz[i][j]
    return round(cont2/cont,2)