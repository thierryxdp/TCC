def media_matriz(matriz):
    for i in matriz:
        entradas=[]
        for k in i:
            entradas.append(k)
        return sum(entradas)/len(entradas)