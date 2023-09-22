def busca(c, m):
    '''
    A função retorna todos os dados de um funcionário
    dado o seu setor
    str, matriz --> matriz
    '''
    mr = []
    for i in range(len(m)):
        if c == m[i][2]:
            list.appened(mr, m[i][0 : 2] + m[-1])
    return mr