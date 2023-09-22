def busca (setor, matriz):
    '''Faz uma busca e retorna os dados de funcionários da empresa
    por setor.
    string, lista -> lista'''
    dados_funcionarios= []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str.upper(setor) in str.upper(matriz[i][j]):
         		dados_funcionarios += matriz[i] 
    return dados_funcionarios