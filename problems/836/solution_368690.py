def busca(setor, matriz):
    """ Funcao que recebe uma matriz de funcionarios e um setor.
    	Retorna todos os funcionarios do setor;
        str, list -> list
    """
    funcionarios_setor = []
    for coluna in matriz:
        if coluna[2] == setor:
            funcionarios_setor.append(coluna)
            
    return funcionarios_setor