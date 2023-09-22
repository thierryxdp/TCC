def busca(palavra,matriz):
    '''função que retorna os dados de todos os funcionarios do setor indicado'''
    lista = []
    for x in range(len(matriz)):
        if matriz[x][2]== palavra:
            lista.append([matriz[x][0], matriz[x][1],matriz[x][3]])
    return lista