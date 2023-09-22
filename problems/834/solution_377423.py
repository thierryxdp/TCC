def media_matriz(matriz):
    for i in matriz:
        entradas=[]
        for k in i:
            entradas.append(k)
        return round(sum(entradas)/len(entradas),2)