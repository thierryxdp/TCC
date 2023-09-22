def busca(buscado,matriz):
    '''Função que dado uma lista de informações e um nome de setor, retorna as informações referentes à informação dada.
    lista, str -> lista'''
    
    
    DadosLocalizados = []
    #cria a lista com as informações de cada funcionário
    for informacao in range (len(matriz)):
        for setor in range (len(matriz[0])):
            if matriz[informacao][setor] == buscado:
                DadosLocalizados.append(matriz[informacao].remove(buscado))
                
    return DadosLocalizados