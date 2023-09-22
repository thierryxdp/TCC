def busca (setor,matriz):
    '''
    Função que, apartir de uma matriz com dados de funcionários, e um setor desejado retorna os funcionários que são desse setor.
    Caso não há funcionários no setor buscado, retorna uma lista vazia.
    str,list-> list
	'''
    lista_setor = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            lista_setor += [matriz[i][0:2]+matriz[i][3:]]
    return lista_setor