def busca(M,setor):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if setor in M[j]:
                return M[i][1],M[i][2],M[i][4]