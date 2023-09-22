def busca(buscado,matriz):
    '''Função que dado uma lista de informações e um nome de setor, retorna as informações referentes à informação dada.
    lista, str -> lista'''
    
    for informacao in range (len(matriz)):
        for setores in range (len(matriz[0])):
           	if matriz[informacao][setores] == buscado:
                return matriz[informacao]