def busca (setor, m):
    '''Essa função ao recebe uma matriz e um setor como valor de entrada, '''
    '''str,list -> tuple'''
    
    tupla = []
    
    for numero in m:
        for i in numero:
            if i == setor:
                indice = list.index (numero,i)
                del numero[indice]
                final +=[numero,]
    return tupla