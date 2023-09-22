def media_matriz(matriz):
    """
    Essa função gera a media de uma determinada matriz
    Parametro de entrada: list
    Valor de Retorno: float
    """
    total = 0
    contador = 0
    for i in matriz:
        for k in i:
            total = total + k
            contador = contador + 1
    return round(total/contador,2)