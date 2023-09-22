def busca(setor,matriz):
    ''' Recebe uma matriz(list) e faz uma busca por setor, ou seja, dado um nome de um setor da empresa,
    a função retorna os dados de todos os funcionários daquele setor.  '''
    lista=[]
    x=0
	while x < len(matriz):
		if matriz[x][2] == setor:
        	lista.append(matriz[x][0])
            lista.append(matriz[x][1])
            lista.append(matriz[x][3])
		x+=1
    return lista