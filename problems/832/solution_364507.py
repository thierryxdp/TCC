def eh_quadrada(matriz):
    '''Função que identifica se a matriz fornecida é q
    e se for quadrada retorna True, mas se não for retorna False
    list(list) -> bool'''
    for ind_linha in range(len(matriz)):
        for indice_coluna in range(len(matriz)):
            if len(matriz) != len(ind_linha):
                return False
            elif matriz[ind_linha][ind_coluna]==[] :
                return True
    return True