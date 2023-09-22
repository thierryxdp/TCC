def busca(setor,matriz):
    """funcao que, dado um setor de uma emprese e uma matriz com dados dos funcionarios dela, retorna os daados de todos os funcionarios daquele setor
    str,list(list(str))--->list(list(str))"""
    dados=[]
    for i in range(len(matriz)):
        dados_funcionario=[]
        for j in range(len(matriz[0])):
            if setor==matriz[i][j]:
                dados_funcionario=dados_funcionario+ [matriz[i]]
        dados=dados+dados_funcionario[:2][3:]
    return dados