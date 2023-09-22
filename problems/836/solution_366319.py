def busca(matriz, setor):
    """ Função que recebe uma matriz com os dados dos funcionários e faz uma busca por setor.
    	De modo que, dado o nome de um setor a função retorna os dados de todos os funcionários daquele setor.
        list ->list
    """
    
    busca = []
    for i in range(0,len(matriz)):
        if setor in matriz[i][2] :
            troca = [matriz[i][0], matriz[i][2], matriz[i][3]]
            busca.append(troca)
    return  busca