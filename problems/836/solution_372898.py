def busca(area,matriz):
    '''Funcao que recebe uma matriz e faça uma busca por setor, ou seja, 
    dado um nome de um setor da empresa, a função retorna os dados de todos
    os funcionários daquele setor.
    str,list->list
    '''
    lista=[]
    for x in range(len(matriz)):
        if area== matriz[x][2]:
            for y in range(len(matriz[0])):
                lista+=matriz[x][y]
	return lista