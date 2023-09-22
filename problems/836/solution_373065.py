def busca (setor, m):
    ''' recebe uma matriz e faz uma busca pelo setor dado de entrada, retornando os dados de todos os funcionarios daquele setor'''
    '''str,list->tupla'''
    
    final = []
    
    for numero in m:
        for i in numero:
            if i == setor:
                indice = list.index (numero,i)
                del numero[indice]
                final +=[numero,]
    return final