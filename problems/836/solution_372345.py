def busca(setor, matriz):
    '''Função que dada uma matriz com os dados dos funcionários de uma empresa e um
    setor dessa empresa, retorne uma outra matriz com, apenas, os dados dos
    funcionários dessa determinada área
    str, list -> list'''
    matriz_final = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
			matriz_sem_setor = []
            for j in range(len(matriz[0])):
                if j != 1:
                    list.append(matirz_sem_setor, matriz[i][j])
			matriz_final += matriz_sem_setor
	return matriz_final