def media_matriz(matriz):
    lista=[]
    for i in range(len(matriz)):
        for matriz[i] in matriz:
            lista+=[sum(matriz[i])]
            i+=1
        return lista