def busca (setor, m):
    '''Essa função ao recebe uma matriz e um setor como valor de entrada, '''
    '''str,list -> tuple'''
    
    tupla = []
    
    for n in m:
        for i in n:
            if i == setor:
                indice = list.index (n,i)
                del n[indice]
                final +=[n,]
    return tupla