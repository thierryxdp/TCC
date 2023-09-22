def eh_quadrada(matriz):
    """Função que identifica se a matriz dada é quadrada
       list -> bool"""
    numeroLinhas = len(matriz)
    numeroColunas = len(matriz[0])
    for linha in matriz:
        if len(linha) == 0:
            return True
    if numeroLinhas == numeroColunas:
        return True
    else:
        return False