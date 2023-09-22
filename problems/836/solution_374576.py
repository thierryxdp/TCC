def busca(setor,matriz):
    '''Dado uma matriz com informações de funcionários e o nome de um setor, retorna todos os funcionários daquele setor
    list,str->list'''
    
    final=[]
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            final+=[matriz[i]-matriz[i][2]
    return final