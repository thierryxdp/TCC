def busca(setor,matriz):
    '''Função que recebe como entrada uma string com o nome de um setor da
    empresa e uma matriz contendo informações sobre os funcionários e retorna
    uma lista com os dados de todos os funcionários daquele setor. Cada linha da
    matriz tem quatro entradas, representando as informações referentes a nome,
    registro, setor e telefone de um funcionário, nesta ordem. O número de linhas
    depende da quantidade de funcionários. Todas as entradas da matriz estão em
    formato string. str,list(list)->list'''
    resultado=[]
    for i in range(len(matriz)):
        funcionario=[]
        for j in range(len(matriz[0])):
            if matriz[i][2] == setor:
                funcionario.append(matriz[i][j])
    resultado.append(funcionario)
    return resultado