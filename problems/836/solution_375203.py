def busca(setor,x):
    '''Função recebe uma matriz e um setor e analisa quais funcionários 
    trabalham em determinado setor
    
    str,list->list'''
    
    lista = []
    
    for listas in x:
        if listas[2] == setor:
            del listas[2]
            lista.append(listas)
            
    return lista