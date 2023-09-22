def busca(setor,matriz):
    '''
    str,list->list
    '''
    local=[]
    for x in range(len(m)):
        if setor in matriz[x]:
            local=local+[matriz[x]]
          
    for y in range(len(local)):
    	if setor in local[y]:
            list.remove(local[y],setor) 
            
    return local