def busca(setor,matriz):
    '''funçao que, ao receber uma matriz e o nome de um setor,
    faz uma busca por setor, retornando os dados de todos os 
    funcionarios daquele setor
    str, matriz -> list'''
	y=[]
	for i in range (len(matriz)):
			if setor in matriz[i]:
				matriz[i].remove(setor)
				y=y+[matriz[i]]
	return y