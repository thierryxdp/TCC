def eh_quadrada(matriz):
    '''Função que identifica se a matriz fornecida é q
    e se for quadrada retorna True, mas se não for retorna False
    list(list) -> bool'''
    for ind_linha in matriz:
        for indice_coluna in range(len(matriz[ind_linha])):
            if ind_linha==indice_coluna:
                coluna_nova=matriz[ind_linha][coluna]
                return True
            else:
                return False