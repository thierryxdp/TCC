def busca(setor, matriz):
    '''retorna os dados de todos os funcionarios do setor buscado'''
    resultado = []
    for i in range(0, len(matriz)):
        if setor in matriz[i][2]:
            info_funcionario = list.del(matriz[i], 2)
            resultado.append(info_funcionario)
	return resultado