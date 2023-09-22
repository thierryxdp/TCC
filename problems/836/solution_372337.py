def busca(setor, matriz):
    '''Função que dada uma matriz com os dados dos funcionários de uma empresa e um
    setor dessa empresa, retorne uma outra matriz com, apenas, os dados dos
    funcionários dessa determinada área
    str, list -> list'''
    matriz_final = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(matriz_final, matriz[i])
	return matriz_final