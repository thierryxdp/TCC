def busca(setor,matriz):
    '''função que busca por setor os funcionários de uma empresa armanezado na matriz
    str,list->list'''
    i=0
    resultbusca=[]
    while i<len(matriz):
        if matriz[i][2] == setor:
            list.append(resultbusca,matriz[i])
        	i=i+1    
        else:
            i=i+1
    return resultbusca