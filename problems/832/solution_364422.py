def eh_quadrada(matriz):
    '''Função que identifica se a matriz fornecida é q
    e se for quadrada retorna True, mas se não for retorna False
    list(list) -> bool'''
    for ind_linha in range(0, len(matriz)):
        for indice_coluna in range(0, len(matriz)):
            if ind_linha==indice_coluna:
                return False
            else:
                return True