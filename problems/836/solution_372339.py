def busca(setor, matriz):
    '''Função que dada uma matriz com os dados dos funcionários de uma empresa e um
    setor dessa empresa, retorne uma outra matriz com, apenas, os dados dos
    funcionários dessa determinada área
    str, list -> list'''
    matriz_final = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz_sem_setor = list.remove(matriz[i], setor)
            list.append(matriz_final, matriz_sem_setor)
	return matriz_final