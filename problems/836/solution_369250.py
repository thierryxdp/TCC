def busca(setor_empresa, matriz):
    """Dados um nome de setor da empresa e uma matriz 
    com dados de funcionários retorna os dados de 
    todos os funcionarios de determinado setor; list, list -> list """
    dados = []
    for i in matriz:
        if setor_empresa in i:
            dados += +[[[i[0]]+i[1]]+[i[3]]]
    return dados