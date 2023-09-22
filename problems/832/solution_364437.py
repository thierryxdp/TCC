def eh_quadrada(matriz):
    '''Função que identifica se a matriz fornecida é q
    e se for quadrada retorna True, mas se não for retorna False
    list(list) -> bool'''
    for ind_linha in range(len(matriz)):
        for indice_coluna in range(len(matriz)):
            if ind_linha==indice_coluna:
                return False
            else:
                ind_linha=0 and ind_coluna=0
                return True
    return True