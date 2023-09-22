def conta_numero(numero, matriz):
    '''Retorna quantas vezes o numero apareceu na matriz
    	int, list(list) -> int'''
    ocorrencias = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                ocorrencias = ocorrencias + 1
    return ocorrencias