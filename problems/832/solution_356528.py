def eh_quadrada(matriz):
    """Função que identifica se a matriz dada é quadrada
       list -> bool"""
    if len(matriz) == 0:
        return True
    numeroLinhas = len(matriz)
    numeroColunas = len(matriz[0])
    if numeroLinhas == numeroColunas:
        return True
    else:
        return False