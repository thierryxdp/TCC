def busca(c, m):
    '''
    A função retorna todos os dados de um funcionário
    dado o seu setor
    str, matriz --> matriz
    '''
    mr = []
    for i in range(len(m)):
        if c == m[i][2]:
            mr += m[i]
    return mr