def busca(setor,matriz):
    ''' Recebe uma matriz(list) e faz uma busca por setor, ou seja, dado um nome de um setor da empresa,
    a função retorna os dados de todos os funcionários daquele setor.  '''
    lista=[]
    x=0
	while x < len(matriz):
        pessoa=[]
		if matriz[x][2] == setor:
        	pessoa.append(matriz[x][0])
            pessoa.append(matriz[x][1])
            pessoa.append(matriz[x][3])
            lista.append(pessoa)
		x+=1
    return lista