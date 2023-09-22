def busca(funcionario, matriz):
    '''Função que busca o nome de um setor da empresa e retorna os dados de todos os funcionários do setor, str, list -> list'''
    lista = []
    for i in range(len(matriz)):
        if funcionario != matriz[i][2]:
            lista = lista + [[matriz[i][0], matriz[i][1], matriz[i][2], matriz[i][3]]]
    return lista