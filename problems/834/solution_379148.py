def media_matriz(matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    lista_soma=[]
    for i in range(nlinhas):
        lista=[]
        for j in range(mcolunas):
            lista_soma.append(matriz[i][j])
    return round(sum(lista_soma)/len(lista_soma),2)