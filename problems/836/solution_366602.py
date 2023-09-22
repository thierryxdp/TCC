def busca(setor, matriz):
    '''
		Função que retorna os dados dos funcionários pelos dados buscados.
		List => List
    '''
    encontrados = []
    for i in range(len(matriz)):
        if (matriz[i][2] == setor):
            encontrados.append(matriz[i][0:2] + matriz[i][3:4])
    return encontrados