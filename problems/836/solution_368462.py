def busca(setor:str, matriz:list) -> list:
    '''Recebe uma matriz contendo os dados de uma lista de funcionários de 
    uma empresa e busca os funcionários por setor, retornando os dados dos
    funcionários daquele setor.'''
    funcionarios = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                funcionarios.append([matriz[i][0],matriz[i][1], matriz[i][3]])
    return funcionarios