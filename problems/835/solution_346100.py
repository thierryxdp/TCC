def melhor_volta(matriz):
    lista=[]
    for i in range len(matriz):
        for matriz[i] in range(len(matriz)):
            lista+=[min(matriz[i])]
        i+=1
        return (matriz.index(min(lista)),min(lista),matriz[i].index(min(lista)))