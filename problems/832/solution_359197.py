def eh_quadrada(matriz):
    '''
    Função booleana que identifica se uma matriz é quadrada.
    
    list -> bool
    '''
    linhas = len(matriz)
    if linhas == 0:
        return True
    else:
        colunas = len(matriz[0])
        if linhas == colunas:
            return True
        else:
            return False