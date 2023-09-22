def eh_quadrada(matriz):
    # lista de lista (matriz) --> bool
    num_linhas = len(matriz)
    for i in range(0,num_linhas):
        if len(matriz[i]) != num_linhas:
            return False     
    return True