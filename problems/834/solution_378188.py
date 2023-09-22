def media_matriz(matriz):
    'dado uma matriz,retorna a media de todos os números da matriz'
    numeros_da_matriz=[]
    quantidade_de_numeros=len(matriz)*len(matriz[0])
    for linhas in matriz:
        for elementos in linhas:
            list.append(numeros_da_matriz,elementos)
    media_da_matriz=sum(numeros_da_matriz)/quantidade_de_numeros
    return media_da_matriz