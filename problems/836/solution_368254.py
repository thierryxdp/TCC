def busca(setor,M):
    for i in range(M):
        for j in range(M[0]):
            if setor==M[j]:
                return M[j]