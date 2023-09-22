def busca(buscado,matriz):
    '''Função que dado uma lista de informações e um nome de setor, retorna as informações referentes à informação dada.
    lista, str -> lista'''
    
    DadosLocalizados = []
    
    for informacao in range (len(matriz)):
        for setor in range (len(matriz[0])):
           	if matriz[informacao][setor] == buscado:
                DadosLocalizados.append(matriz[informacao])
	return DadosLocalizados