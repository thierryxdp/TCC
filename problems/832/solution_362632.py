def eh_quadrada(matriz):
    '''
    dada uma matriz, verifica se ela é quadrada
    
    array -> bool
    '''
    if matriz == []:
        return True
    else:
        colunas = len(matriz[0])
        linhas = len(matriz)
        output = bool(colunas == linhas)
        return output