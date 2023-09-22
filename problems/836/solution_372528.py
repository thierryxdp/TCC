def busca(setor,matriz):
    '''retorna os dados de todos os funcionarios de um setor da empresa contidos na matriz dada'''
    '''str,list -> list'''
    
    list_set=[]
    i=0
    
    while i < len(matriz):
        if setor in matriz[i][2]:
            list.append(list_set,matriz[i][2])
            i=i+1
            
    return list_set