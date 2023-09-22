def busca(setor, matriz):
    j = []
    for i in range(len(matriz)):
        if j in matriz[i]:
            list.append(j, matriz[i])
    for x in range(len(j)):
        if j[x][2] == setor:
            del j[x][2]
    return j