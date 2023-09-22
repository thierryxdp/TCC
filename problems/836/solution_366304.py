def busca(setor, matriz):
    """ Função que recebe uma mattriz e e um dado nome de um setor e retorna os dados de todos os funcionários de um setor
    	list, str -> list
    """
    
    listaFinal = []
    
    for i in range(0, len(matriz)):
        if setor in matriz[i][2]:
            matriz.remove(matriz,setor)
            listaFinal.append(matriz[i])
    
    return listaFinal