def busca(setor,matriz):
    encontra = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor in matriz[i]:
                encontra+=list.pop(matriz,i)
    return encontra