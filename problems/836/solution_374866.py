def busca(setor,m):
    '''
    funcao que recebe uma matriz com o a do exemplo e faz uma busca por setor, dado um setor da empresa, a funcao retorna os dados
    de todos os funcionários daquele setor
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