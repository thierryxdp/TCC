def busca(setor, matriz):
    '''
    A função retorna todos os dados dos funcionários de uma empresa
    de um determinado setor
    matriz, str --> matriz
    '''
    busca = []
    for i in range(len(matriz)):
        if i[2] == setor:
            list.append(busca, matriz[i])
    return busca