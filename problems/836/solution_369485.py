def busca(setor, matriz):
    """ função que recebe uma matriz e o setor ou nome que se deseja buscar e retorna todos os dados dos funcionarios daquele setor
    	entrada: str, lista
        saida: lista
    """
    
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if setor in matriz:
    return matriz[linha]