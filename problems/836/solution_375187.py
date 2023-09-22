def busca(setor,M):
    ''' '''
    lista = []
    for i in range(len(M)):
        if setor == M[i][2]:
            lista.append([M[i][0], M[i][1], M[i][3]])
        
    return lista