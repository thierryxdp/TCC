def busca(setor, matriz):
    '''Faça uma funcao que receba uma matriz e faça uma busca por setor, ou seja,
    dado um nome de um setor da empresa, retorne os dados de todos os funcionários daquele 
    setor. list-->list.'''
    dados_funcionarios = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            dados_funcionarios += [[matriz[i][0], matriz[i][1], matriz[i][3]]]
    return dados_funcionarios