def eh_quadrada(matriz):
    '''Função que identifica se a matriz fornecida é q
    e se for quadrada retorna True, mas se não for retorna False
    list(list) -> bool'''
    for indice_linha in matriz:
        for indice_coluna in range(len(matriz[linha])):
            if indice_linha==indice_coluna:
                coluna_nova=matriz[linha][coluna]
                return True
            else:
                return False