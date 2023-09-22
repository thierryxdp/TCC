def eh_quadrada(matriz):
    """ Recebe uma matriz e retorna um valor booleano identificando
    se uma matriz é quadrada ou não"""
    quantidade = 0
    linha = 0
    if len(matriz) == 0:
    	return True
    
    for conjunto in matriz:
        for unidade in conjunto:
            quantidade = quantidade + 1
        linha = linha + 1

    coluna = quantidade / linha
    
    if coluna == linha:
        return True
    else:
        return False