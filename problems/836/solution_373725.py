def busca (setor,matriz):
    
    '''A função recebe um nome de um setor e uma matriz com as informações
        dos funcionários que fazem parte como parametros de entrada;
        str,list-->list
    '''
    retornoBusca = []

    for i in range(len(matriz)):
        for setores in matriz[i]:
            if setores == setor:
                list.append(retornoBusca,matriz[i])
        for y in range(len(retornoBusca)):
            if setor in retornoBusca[y]:
                retornoBusca[y].remove(setor)
            
    return retornoBusca