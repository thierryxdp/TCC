def melhor_volta(matriz):
    lista1 = []
    lista2 = []
    for i in range(len(matriz)):
        lista1.append(min(matriz[i]))
        for j in range(len(matriz[i])):
            if matriz[i][j] == min(matriz[i]):
                lista2.append(j+1)
    return (lista1.index(min(lista1)))+1,lista2[lista1.index(min(lista1)))]