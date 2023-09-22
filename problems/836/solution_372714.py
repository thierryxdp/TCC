def busca (setor,matriz):
    
    '''A função recebe um nome de um setor e uma matriz com as informações
        dos funcionários que fazem parte como parametros de entrada;
        str,list-->list
    '''
    retornoBusca = []
    i = 0
    for setores in matriz:
        for setores in matriz[i]:
            if setores == setor:
                list.append(retornoBusca,matriz[i])
        		del(retornoBusca[i][2])
    	i+=1
    return retornoBusca