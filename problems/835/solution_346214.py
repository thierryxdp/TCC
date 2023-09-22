def melhor_volta(matriz):
    for i in range(len(matriz)):
        lista=list.sort(matriz[i])
        melhor=min(lista[i][0])
        return (i,melhor)