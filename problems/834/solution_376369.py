def media_matriz(matriz):
    lista=[]
    lista2=[]
    for i in range(len(matriz)):
        for matriz[i] in matriz:
            lista+=[sum(matriz[i])]
            i+=1
            for j in range(len(lista)):
                lista2+=[sum(lista[j])]
                j+=1
                return lista2