def media_matriz(matriz):
    """Função que calcula a média dos elementos de uma matriz"""
    """Parâmetros de entrada:list"""
    """Parâmetros de saída:float"""
    acumulador=0
    for lista_interna in matriz:
        for item in lista_interna:
            acumulador+=item
    return round(acumulador/(len(matriz)*len(matriz[0])),2)