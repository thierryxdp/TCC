def busca(area, matriz):
    '''Essa função tem como objetivo buscar em uma matriz um setor da 
    empresa, e retornar todas as pessoas dentro que trabalham nesse setor. '''
    ''' str, list(list) -> list(list)''' 
    
    
    lista = []
    for i in range(len(matriz)):
    	if area in matriz[i][2]:
            matriz_encontrada = (matriz[i])
            list.remove(matriz_encontrada,area)
            list.append(lista,matriz_encontrada)
    return lista