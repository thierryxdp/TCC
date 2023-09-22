def busca(setor, matriz):
    """ Funcao que recebe uma matriz de funcionarios e um setor.
    	Retorna todos os funcionarios do setor;
        str, list -> list
    """
    funcionarios_setor = []
    for coluna in matriz:
        if coluna[2] == setor:
            funcionarios_setor.append([coluna[0], coluna[1], coluna[3]])
            
    return funcionarios_setor