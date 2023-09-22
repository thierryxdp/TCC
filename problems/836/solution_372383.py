def busca(setor , matriz):
    a = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            del(matriz[i][2])
            list.append( a , matriz[i])
    return a