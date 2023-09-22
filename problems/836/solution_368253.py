def busca(setor,M):
    for i in range(M):
        for j in range(M[0]):
            if setor in M[j]:
                return M[j]