def media_matriz(matriz):
    entradas=[]
    for i in matriz:
        
        for k in i:
            entradas.append(k)
            return round(sum(entradas)/len(entradas),2)