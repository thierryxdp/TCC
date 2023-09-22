def busca (setor, m):
    '''Essa função ao recebe uma matriz e um setor como valor de entrada, retorna os dados de todos os funcionarios daquele setor '''
    '''str,list -> tuple'''
    
    tupla = []
    
    for n in m:
        for i in n:
            if i == setor:
                indice = list.index (n,i)
                del n[indice]
                tupla +=[n,]
    return tupla