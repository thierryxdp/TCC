def busca(setor,matriz):
    '''função que receba uma matriz como a do exemplo e faça uma busca por setor, ou seja, dado
    um nome de um setor da empresa, função retorna os dados de todos os funcionarios daquele setor;
    str, mat -> list'''
    informacoes = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.remove(matriz[i],setor)
            informacoes += [matriz[i],]
    return informacoes