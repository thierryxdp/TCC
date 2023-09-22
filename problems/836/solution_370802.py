def busca(setor,matriz):
    '''busca os funcionários de um setor específico
    str,list(list) -> list'''
    achados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i][j]:
                list.remove(matriz[i],setor)
                achados.append(matriz[i])
	return achados