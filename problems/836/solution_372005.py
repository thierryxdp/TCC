def busca (setor, m):
    ''' '''
    ''' '''
    
    final = []
    
    for i in m:
        for j in i:
            if j == setor:
                indice = list.index (i,j)
                del i[indice]
                final +=[i,]
    return final