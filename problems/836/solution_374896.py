def busca(setor,matriz):
    '''
    Funçao que dado uma matriz com dados de funcionarios, com as linhas dependendo
    da quantidade de funcionaris, e um setor, retorna os dados de todos os funcionarios
    daquele setor
    string, list(string) -> list
    '''
    busca_setor = []
    for i in range(len(matriz)):
        for setor in matriz[i]:
            list.remove(matriz[i],setor)
            list.append(busca_setor,matriz[i])
    return busca_setor