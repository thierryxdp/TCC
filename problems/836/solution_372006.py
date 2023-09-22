def busca (setor, m):
    ''' recebe uma matriz e faz uma busca pelo setor dado de entrada, retornando os dados de todos os funcionarios daquele setor'''
    '''str,list'''
    
    final = []
    
    for i in m:
        for j in i:
            if j == setor:
                indice = list.index (i,j)
                del i[indice]
                final +=[i,]
    return final