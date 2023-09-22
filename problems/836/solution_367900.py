def busca(setor,matriz):
    i = 0
    j = 0
    M = []
    while i < len(matriz):
        for j in matriz[i]:
            if setor in matriz:
                list.append(M,matriz[i])
                return M