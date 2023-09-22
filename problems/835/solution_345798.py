def melhor_volta(matriz):
    "função que recebe uma matriz com tempos dos corredores e retorna uma tupla dizendo quem fez a melhor volta,com qual tempo e em que volta.list->tuple."
    lista1 = []
    lista2 = []
    for i in range(len(matriz)):
        lista1.append(min(matriz[i]))
        for j in range(len(matriz[i])):
            if matriz[i][j] == min(matriz[i]):
                lista2.append(j+1)
    return (lista1.index(min(lista1)))+1, min(lista1),lista2[(lista1.index(min(lista1)))]