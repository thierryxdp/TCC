def busca(setor,matriz):
    i = 0
    j = 0
    M = []
    while i < len(matriz):
        for j in matriz[i]:
            if j == setor:
            	list.append(M,matriz[i])
                M[i].pop(2)
        i = i + 1
    return M