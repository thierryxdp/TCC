def busca(setor, matriz):
    """ Função que recebe uma mattriz e e um dado nome de um setor e retorna os dados de todos os funcionários de um setor
    	list, str -> list
    """
    
    listaFinal = []
    
    for i in range(0, len(lista)):
        if setor in lista[i][2]:
            listaFinal.append(lista[i])
    
    return listaRetorno