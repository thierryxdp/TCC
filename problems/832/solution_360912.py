def eh_quadrada(matriz):
    """Função booleana que identifique se uma matriz é
    quadrada, um matriz vazia também é considerada quadrada
    list-->bool."""
    linhas = len(matriz)
    colunas = int
    if matriz == []:
        colunas = len(matriz)
        return True
    for i in range(linhas):
        colunas = len(matriz[0])
        if (linhas == colunas):
            return True
    if linhas != colunas:
        return False