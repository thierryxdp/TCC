def busca(Busca_por_setor, Matriz):
    '''
    Recebe uma matriz contendo dados dos funcionários
    Recebe um termo para a busca
    Retorna os dados de todos os funcionarios daquele setor
    '''
    dados = []
    for Nome, Registro, Setor, Fone in Matriz:
        if Setor == Busca_por_setor:
            dados.append([Nome, Registro, Fone])
    return dados