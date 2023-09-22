def busca(setor,matriz):
    '''
    Função que recebe uma matriz como a do exemplo e faz uma busca
    por setor e retorna os dados de todos os funcionários daquele setor
    list -> list
    '''
    lista = []
    for linha in matriz:
        if linha[2] == setor:
            lista += [linha[0], linha[1], linha[3], ]
            
    return lista