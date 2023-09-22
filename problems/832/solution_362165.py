def eh_quadrada(matriz):
    """funcao que dada uma matriz de entrada verifica se a
    mesma é quadrada ou não;
    list(list) -> bool"""
    
    matriz_vazia = []
    if matriz == matriz_vazia:
        return True
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    
    else:
        return False