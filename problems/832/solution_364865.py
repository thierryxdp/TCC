def eh_quadrada(matriz):
    """ Dado uma matriz verifca se ela é quadrada.
    entrada matriz -> saida bool"""
    
    if matriz == []:
        return matriz == []
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    return linhas == colunas