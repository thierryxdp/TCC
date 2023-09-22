def busca(setor,m):
    '''
    str,list->list
    '''
    local=[]
    for x in range(len(m)):
        if setor in m[x]:
            local=local+[m[x]]
          
    for y in range(len(local)):
    	if setor in local[y]:
            list.remove(local[y],setor) 
            
    return local