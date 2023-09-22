def busca(matriz, setor):
    """ Função que recebe uma matriz com os dados dos funcionários e faz uma busca por setor.
    	De modo que, dado o nome de um setor a função retorna os dados de todos os funcionários daquele setor.
        list ->list
    """
    
    busca = []
    for i in range(len(matriz)):
        if matriz[0][2]==setor:
            troca = [matriz[0][0], matriz[0][2], matriz[0][3]]
            busca.append(troca)
    return  busca