def busca(setor,M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if setor in M[i][j]:
                return M[j]