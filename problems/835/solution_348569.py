def volta(matriz):
    l1 = sum(matriz[0])
    l2 = sum(matriz[1])
    l3 = sum(matriz[2])
    l4 = sum(matriz[3])
    l5 = sum(matriz[4])
    l6 = sum(matriz[5])

    resp = min(l1,l2,l3,l4,l5,l6)

    for i in range(len(matriz)):
        if sum(matriz[i]) == resp:
            retorno = (min(matriz[i]),list.index(matriz,[i]))
    return retorno