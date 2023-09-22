def busca(matriz, setor):
    """ Funcao que recebe uma matriz de funcionarios e um setor.
    	Retorna todos os funcionarios do setor;
        list, str -> list
    """
    funcionarios_setor = []
    for coluna in matriz:
        if coluna[2] == setor:
            funcionarios_setor.append(coluna)
            
    return funcionarios_setor