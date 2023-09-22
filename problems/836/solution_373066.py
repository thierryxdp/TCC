def busca (setor, m):
    '''Recebe uma matriz e um setor, e faz uma busca pelo setor, retornando os respectivos dados de todos os funcionarios daquele setor'''
    '''str,list'''
    
    tupla = []
    
    for n in m:
        for i in n:
            if i == setor:
                indice = list.index (numero,i)
                del n[indice]
                final +=[numero,]
    return tupla