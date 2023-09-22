def busca(buscado,matriz):
    '''Função que dado uma lista de informações e um nome de setor, retorna as informações referentes à informação dada.
    lista, str -> lista'''
    
    i=0
    DadosLocalizados = []
    #cria a lista com as informações de cada funcionário
    for informacao in range (len(matriz)):
        for setor in range (len(matriz[0])):
			if matriz[informacao][setor] == buscado:
				DadosLocalizados.append(matriz[informacao])
                DadosLocalizados[i].remove(buscado)
    return DadosLocalizados