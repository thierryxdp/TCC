def eh_quadrada(matriz):
    '''Função que identifica se a matriz fornecida é q
    e se for quadrada retorna True, mas se não for retorna False
    list(list) -> bool'''
    for ind_linha in range(len(matriz)):
        for indice_coluna in range(len(matriz)):
            if len(matriz) == len(matriz[ind_linha]) and len(matriz[indice_coluna]):
                return True
            else:
                return False
    return True