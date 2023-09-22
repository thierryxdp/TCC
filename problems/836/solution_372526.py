def busca(setor,matriz):
    '''retorna os dados de todos os funcionarios de um setor da empresa contidos na matriz dada'''
    '''str,list -> list'''
    
    list_set=[]
    i=0
    
    for i in range(matriz):
        if setor in matriz[i]:
            list.append(list_set,matriz[i])
            i=i+1
            
    return list_set