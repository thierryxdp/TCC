def eh_quadrada(matriz):
    '''Função que identifica se a matriz fornecida é q
    e se for quadrada retorna True, mas se não for retorna False
    list(list) -> bool'''
    for ind_linha in range(len(matriz)):
        for indice_coluna in range(len(matriz)):
            if matriz[ind_linha]!=matriz[indice_coluna]:
                return True
            elif matriz[ind_linha][ind_coluna]==[] :
                return True
    return False