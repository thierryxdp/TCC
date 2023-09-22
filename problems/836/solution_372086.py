def busca(setor, matriz):
    '''Função que recebe uma string representando um setor de 
    busca uma matriz que representa os dados dos funcionários de
    uma empresa, na qual cada linha da matriz corresponde as 
    informações de um funcionário, as quais são nome, registro, 
    setor e telefone, todas essas informações em string. A função 
    retorna uma nova matriz contendo as informações de cada funcionário
    que pertence a esse setor.
    [list] -> [list]'''
    n_linhas = len(matriz)
    informacoes_funcionarios_setor = []
    for i in range(n_linhas):
        if matriz[i][2] == setor:
            list.remove(matriz[i], setor)
            list.append(informacoes_funcionarios_setor, matriz[i])
    return informacoes_funcionarios_setor