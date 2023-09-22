def busca(setor,matriz):
    encontra = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                encontra+=list.pop(matriz,i)
    return encontra