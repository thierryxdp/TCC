def busca(setor, matriz):
    """ Função que recebe uma matriz com os dados dos funcionários e faz uma busca por setor.
    	De modo que, dado o nome de um setor a função retorna os dados de todos os funcionários daquele setor.
        list ->list
    """
    
    busca = []
    for i in range(len(matriz)):
        buscado = matriz[i][2]
        if buscado == setor:
            troca = [matriz[i][0], matriz[i][2], matriz[i][3]]
            busca.append(troca)
            
    return  busca