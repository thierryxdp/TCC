def busca(setor, matriz):
    '''retorna os dados de todos os funcionarios do setor buscado'''
    resultado = []
    for i in range(0, len(matriz)):
        if setor in matriz[i][2]:
            funcionario = [matriz[i][0], matriz[i][1], matriz[i][3]]
            resultado.append(funcionario)
	return resultado