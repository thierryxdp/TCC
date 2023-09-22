def eh_quadrada(matriz):
    """Função que retirna true se a matriz de entrada é quadrada e retorna false se ela não for quadrada"""
    """Parâmetros de entrada: list"""
    """Parâmetros de saída: bol"""
    q_linhas=len(matriz)
    q_colunas=len(matriz[0])
    if q_linhas==q_colunas:
        return True
    elif q_linhas!=q_colunas:
        return False