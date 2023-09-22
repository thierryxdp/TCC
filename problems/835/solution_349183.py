def melhor_volta(matriz):
    lista = []

    for i in range(6):
        lista.append(min(matriz[i]))

    return lista.index(min(lista)) + 1, min(lista)