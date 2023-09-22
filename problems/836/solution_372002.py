def busca (m, setor):
    ''' '''
    ''' '''
    final = []
    
    for i in m:
        for j in i:
            if j == setor:
                indice = list.index (i,j)
                del i[indice]
                res +=[i,]
    return res